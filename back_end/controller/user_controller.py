import asyncio
import hashlib
import logging
import re
import time

from back_end.exceptions import APIPermissionError
from back_end.models.models import User
from config import configs

COOKIE_NAME = "roast_tomato_session"
_COOKIE_KEY = configs.session.secret


def check_admin(request):
    if request.__user__:
        logging.info(request.__user__.admin)
    else:
        logging.info('visitor coming')
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError()


def user2cookie(user, max_age):
    """
    Generate cookie str by user.
    """
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = "%s-%s-%s-%s" % (user.id, user.password, expires, _COOKIE_KEY)
    l_str = [user.id, expires, hashlib.sha1(s.encode("utf-8")).hexdigest()]
    return "-".join(l_str)


@asyncio.coroutine
def cookie2user(cookie_str):
    """
    Parse cookie and load user if cookie is valid.
    """
    if not cookie_str:
        return None
    try:
        l_str = cookie_str.split("-")
        if len(l_str) != 3:
            return None
        uid, expires, sha1 = l_str
        if int(expires) < time.time():
            return None
        user = yield from User.find(uid)
        if user is None:
            return None
        s = "%s-%s-%s-%s" % (uid, user.password, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode("utf-8")).hexdigest():
            logging.info("invalid sha1")
            return None
        user.password = "******"
        return user
    except Exception as e:
        logging.exception(e)
        return None


_RE_EMAIL = re.compile(r"^[a-z0-9.\-_]+@[a-z0-9\-_]+(\.[a-z0-9\-_]+){1,4}$")
_RE_SHA1 = re.compile(r"^[0-9a-f]{40}$")