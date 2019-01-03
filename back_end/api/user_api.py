import hashlib
import json
import logging
import os

from aiohttp import web

from back_end.controller.router_register import post, get
from back_end.exceptions import APIValueError, APIError
from back_end.models.models import User, Blog, Novels, Comments, NovelComments, UserPic, next_id
from back_end.controller.common_controller import get_page_index, Page
from back_end.controller.user_controller import COOKIE_NAME, check_admin, user2cookie, _RE_EMAIL, _RE_SHA1


@post("/api/authenticate")
async def authenticate(*, email, password):

    if not email:
        raise APIValueError("email", "Invalid email.")
    if not password:
        raise APIValueError("password", "Invalid password.")
    users = await User.find_all("email=?", args=[email])
    if len(users) == 0:
        raise APIValueError("email", "Email not exist.")
    user = users[0]
    # check password:
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode("utf-8"))
    sha1.update(b":")
    sha1.update(password.encode("utf-8"))
    if user.password != sha1.hexdigest():
        raise APIValueError("password", "Invalid password.")
    # authenticate ok, set cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly="true")
    user.password = "******"
    r.content_type = "application/json"
    r.body = json.dumps(user, ensure_ascii=False).encode("utf-8")
    return r


@post("/api/users/{user_id}/update")
async def api_users_update(user_id, request, *, name, image):
    user_ls = await User.find_all(where="id = '%s'" % user_id)
    user = user_ls[0]
    user.name = name.strip()
    user.image = image.strip()
    # 分段操作
    r = web.StreamResponse(status=200)
    await r.prepare(request)
    # r.content_type = "text/plain"
    r.enable_chunked_encoding()
    #
    await user.update()
    blog_list = await Blog.find_all(where="user_id = '%s'" % user_id)
    if blog_list:
        for blog in blog_list:
            blog.user_image = image.strip()
            blog.user_name = name.strip()
            await blog.update()
    await r.write(b"1")
    novels = await Novels.find_all(where="user_id = '%s'" % user_id)
    if novels:
        for novel in novels:
            novel.user_image = image.strip()
            novel.user_name = name.strip()
            await novel.update()
    await r.write(b"2")
    comments = await Comments.find_all(where="user_id = '%s'" % user_id)
    if comments:
        for comment in comments:
            comment.user_image = image.strip()
            comment.user_name = name.strip()
            await comment.update()
    await r.write(b"3")
    novel_comments = await NovelComments.find_all(where="user_id = '%s'" % user_id)
    if novel_comments:
        for novel_comment in novel_comments:
            novel_comment.user_image = image.strip()
            novel_comment.user_name = name.strip()
            await novel_comment.update()
    await r.write(b"4")
    await r.write_eof()
    return r


@get("/api/users")
async def api_get_users(*, page="1"):
    page_index = get_page_index(page)
    num = await User.find_number("count(id)")
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, users=())
    users = await User.find_all(orderBy="created_at desc", limit=(p.offset, p.limit))
    for u in users:
        u.password = "******"
    return dict(page=p, users=users)


@get("/api/user_pic")
async def api_user_pic(request, *, page="1"):
    user_id = request.__user__.id
    page_index = get_page_index(page)
    num = await UserPic.find_number(
        select_field="count(id)", where="user_id = '%s'" % user_id
    )
    page = Page(num, page_index)
    if num == 0:
        return dict(page=page, pics=())
    pics = await UserPic.find_all(
        where="user_id = '%s'" % user_id,
        orderBy="created_at desc",
        limit=(page.offset, page.limit),
    )
    return dict(page=page, pics=pics)


@post("/api/user_pic/{pic_id}/delete")
async def api_delete_user_id(request, *, pic_id):
    check_admin(request)
    pic = await UserPic.find(pic_id)
    await pic.remove()
    if os.path.exists(
        "%s/user_pic/%s.%s" % (os.path.dirname(os.getcwd()), pic.id, pic.pic_type)
    ):
        os.remove(
            "%s/user_pic/%s.%s" % (os.path.dirname(os.getcwd()), pic.id, pic.pic_type)
        )
    return dict(id=pic.id)


@get("/signout")
def signout(request):
    referer = request.headers.get("Referer")
    r = web.HTTPFound(referer or "/")
    r.set_cookie(COOKIE_NAME, "-deleted-", max_age=0, httponly="true")
    logging.info("user signed out.")
    return r


@post("/api/users")
async def api_register_user(*, email, name, password):
    if not name or not name.strip():
        raise APIValueError("name")
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError("email")
    if not password or not _RE_SHA1.match(password):
        raise APIValueError("password")
    # users = await User.find_all('email=?', [email])
    users = await User.find_all(where='email="%s"' % email)
    if len(users) > 0:
        raise APIError("register:failed", "email", "Email is already in use.")
    uid = next_id()
    sha1_password = "%s:%s" % (uid, password)
    user = User(
        id=uid,
        name=name.strip(),
        email=email,
        password=hashlib.sha1(sha1_password.encode("utf-8")).hexdigest(),
        image="http://www.gravatar.com/avatar/%s?d=mm&s=120"
        % hashlib.md5(email.encode("utf-8")).hexdigest(),
    )
    await user.save()
    # make session cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly="true")
    user.pass_word = "******"
    r.content_type = "application/json"
    r.body = json.dumps(user, ensure_ascii=False).encode("utf-8")
    return r


@post("/api/upload_pic")
async def api_upload_pic(request):
    check_admin(request)
    data = await request.post()
    pic = data["files[]"]
    filename = pic.filename
    pic_name = filename[1: filename.rfind(".")]
    pic_type = filename[filename.rfind(".") + 1: len(filename)]
    pic_file = data["files[]"].file
    if not pic_name or not pic_name.strip():
        raise APIValueError("name", "name cannot be empty.")
    content = pic_file.read()
    user_pic = UserPic(
        pic_name=pic_name, user_id=request.__user__.id, pic_type=pic_type
    )
    await user_pic.save()
    logging.info(user_pic)
    if os.path.exists("%s/user_pic" % (os.path.dirname(os.getcwd()))):
        # if os.path.exists('/user_pic/%s' % (request.__user__.id)):
        with open(
            "%s/user_pic/%s.%s"
            % (os.path.dirname(os.getcwd()), user_pic["id"], pic_type),
            "wb",
        ) as f:
            f.write(content)
    else:
        original_umask = os.umask(0)
        os.makedirs("%s/user_pic" % (os.path.dirname(os.getcwd())), 0o777)
        os.umask(original_umask)
        with open(
            "%s/user_pic/%s.%s"
            % (os.path.dirname(os.getcwd()), user_pic["id"], pic_type),
            "wb",
        ) as f:
            f.write(content)
    logging.info(user_pic)
    return "/api/get_pic/%s" % (user_pic["id"])


@get("/api/get_pic/{pic_id}")
async def api_get_pic(*, pic_id):
    user_pic = await UserPic.find_all(where="id = '%s'" % pic_id)
    road = "%s/user_pic/%s.%s" % (
        os.path.dirname(os.getcwd()),
        user_pic[0].id,
        user_pic[0].pic_type,
    )
    with open(road, "rb") as f:
        data = f.read()
        return {"data": data, "file_type": "picture", "pic_type": user_pic[0].pic_type}