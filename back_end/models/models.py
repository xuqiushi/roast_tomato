#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import uuid

from models.orm import Model, StringField, BooleanField, FloatField, TextField, IntegerField


def next_id():
    return "%015d%s000" % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):

    __table__ = "users"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    email = StringField(ddl="varchar(50)")
    password = StringField(ddl="varchar(50)")
    admin = BooleanField()
    name = StringField(ddl="varchar(50)")
    image = StringField(ddl="varchar(500)")
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = "blog"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)")
    user_name = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    name = StringField(ddl="varchar(50)")
    summary = StringField(ddl="varchar(200)")
    content = TextField()
    created_at = FloatField(default=time.time)


class Comments(Model):
    __table__ = "comments"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    blog_id = StringField(ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)")
    user_name = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    content = TextField()
    created_at = FloatField(default=time.time)


class Novels(Model):
    __table__ = "novels"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)")
    user_name = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    name = StringField(ddl="varchar(50)")
    summary = StringField(ddl="varchar(200)")
    content = TextField()
    created_at = FloatField(default=time.time)


class NovelTree(Model):
    __table__ = "novels_tree"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    novel_id = StringField(ddl="varchar(50)")
    novel_name = StringField(ddl="varchar(50)")
    novel_level = IntegerField(default=1)
    parent_id = StringField(default="214", ddl="varchar(50)")
    son_id = StringField(default='421', ddl='varchar(50)')
    tree_order = IntegerField(default=1)
    created_at = FloatField(default=time.time)


class NovelComments(Model):
    __table__ = "novel_comments"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    novel_id = StringField(ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)")
    user_name = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    content = TextField()
    created_at = FloatField(default=time.time)


class UserPic(Model):
    __table__ = "user_pic"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    pic_name = StringField(ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)")
    pic_type = StringField(ddl="varchar(50)")
    created_at = FloatField(default=time.time)
