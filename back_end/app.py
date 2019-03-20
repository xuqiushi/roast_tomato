#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

import asyncio
import os
import json
import time
from datetime import datetime

from aiohttp import web
from aiohttp.web import middleware
from jinja2 import Environment, FileSystemLoader

from config import configs
from models import orm
from controller.router_register import add_routes, add_static

from controller.user_controller import COOKIE_NAME, cookie2user


def init_jinja2(app, **kw):
    logging.info("init jinja2...")
    options = dict(
        autoescape=kw.get("autoescape", True),
        block_start_string=kw.get("block_start_string", "{%"),
        block_end_string=kw.get("block_end_string", "%}"),
        variable_start_string=kw.get("variable_start_string", "{{"),
        variable_end_string=kw.get("variable_end_string", "}}"),
        auto_reload=kw.get("auto_reload", True),
    )
    path = kw.get("path", None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    logging.info("set jinja2 template path: %s" % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get("filters", None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app["__templating__"] = env


@middleware
async def logger_factory(request, handler):
    logging.info("Request: %s %s" % (request.method, request.path))
    return await handler(request)


@middleware
async def auth_factory(request, handler):
    logging.info("check user: %s %s" % (request.method, request.path))
    request.__user__ = None
    cookie_str = request.cookies.get(COOKIE_NAME)
    if cookie_str:
        user = await cookie2user(cookie_str)
        if user:
            logging.info("set current user: %s" % user.email)
            request.__user__ = user
    if request.path.startswith("/manage/") and (
        request.__user__ is None or not request.__user__.admin
    ):
        # if not request.path.startswith('/signin'):
        return web.HTTPFound("/signin")
    return await handler(request)


@middleware
async def data_factory(request, handler):
    if request.method == "POST":
        if request.content_type.startswith("application/json"):
            request.__data__ = await request.json()
            logging.info("request json: %s" % str(request.__data__))
        elif request.content_type.startswith("application/x-www-form-urlencoded"):
            request.__data__ = await request.post()
            logging.info("request form: %s" % str(request.__data__))
    return await handler(request)


async def response_factory(app, handler):
    async def response(request):
        logging.info("Response handler...")
        r = await handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = "application/octet-stream"
            return resp
        if isinstance(r, str):
            if r.startswith("redirect:"):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode("utf-8"))
            resp.content_type = "text/html;charset=utf-8"
            return resp
        if isinstance(r, dict):
            if "file_type" in r:
                if r["file_type"] == "picture":
                    resp = web.Response(body=r["data"])
                    resp.content_type = "image/%s" % r["pic_type"]
                    return resp
            else:
                template = r.get("__template__")
                if template is None:
                    resp = web.Response(
                        body=json.dumps(
                            r, ensure_ascii=False, default=lambda o: o.__dict__
                        ).encode("utf-8")
                    )
                    resp.content_type = "application/json;charset=utf-8"
                    return resp
                else:
                    r["__user__"] = request.__user__
                    resp = web.Response(
                        body=app["__templating__"]
                        .get_template(template)
                        .render(**r)
                        .encode("utf-8")
                    )
                    resp.content_type = "text/html;charset=utf-8"
                    return resp
        if isinstance(r, int) and 100 <= r < 600:
            return web.Response(text=str(r))
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and 100 <= t < 600:
                return web.Response(text=str(r))
        # default:
        resp = web.Response(body=str(r).encode("utf-8"))
        resp.content_type = "text/plain;charset=utf-8"
        return resp

    return response


def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u"1分钟前"
    if delta < 3600:
        return u"%s分钟前" % (delta // 60)
    if delta < 86400:
        return u"%s小时前" % (delta // 3600)
    if delta < 604800:
        return u"%s天前" % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u"%s年%s月%s日" % (dt.year, dt.month, dt.day)


async def init(event_loop):
    await orm.create_pool(loop=event_loop, **configs.db)
    app = web.Application(
        loop=event_loop, middlewares=[logger_factory, auth_factory, data_factory, response_factory]
    )
    init_jinja2(app, filters=dict(datetime=datetime_filter))
    add_routes(app, '.', 'views')
    add_routes(app, '.', 'api')
    add_static(app)
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    srv = await event_loop.create_server(app_runner.server, host="127.0.0.1", port=8000)
    logging.info("server started at http://127.0.0.1:8000...")
    return srv

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
