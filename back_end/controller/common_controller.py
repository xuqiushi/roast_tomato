#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Callable
import re
import json
import datetime


def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError:
        pass
    if p < 1:
        p = 1
    return p


def text2html(text):
    lines = map(
        lambda s: "<p>%s</p>"
        % s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"),
        filter(lambda s: s.strip() != "", text.split("\n")),
    )
    return "".join(lines)


class Page(object):
    """
    Page object for display pages.

    """

    def __init__(self, item_count, page_index=1, page_size=10):
        """
        Init Pagination by item_count, page_index and page_size.
        >>> p1 = Page(100, 1)
        >>> p1.page_count
        10
        >>> p1.offset
        0
        >>> p1.limit
        10
        >>> p2 = Page(90, 9, 10)
        >>> p2.page_count
        9
        >>> p2.offset
        80
        >>> p2.limit
        10
        >>> p3 = Page(91, 10, 10)
        >>> p3.page_count
        10
        >>> p3.offset
        90
        >>> p3.limit
        10
        """
        self.item_count = item_count
        self.page_size = page_size
        if self.item_count != 0:
            self.page_count = item_count // page_size + (
                1 if item_count % page_size > 0 else 0
            )
        else:
            self.page_count = 1
        if (item_count == 0) or (page_index > self.page_count):
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            self.page_index = page_index
            self.offset = self.page_size * (page_index - 1)
            self.limit = self.page_size
        self.has_next = self.page_index < self.page_count
        self.has_next2 = self.page_index < self.page_count - 1
        self.has_next3 = self.page_index < self.page_count - 2
        self.has_previous = self.page_index > 1
        self.has_previous2 = self.page_index - 1 > 1
        self.has_previous3 = self.page_index - 2 > 1
        self.is_last_button = 1 if (self.page_index < self.page_count - 3) else 0
        self.is_second = 1 if (self.page_index > 4) else 0

    def __str__(self):
        return (
            "item_count: %s, page_count: %s, page_index: %s, page_size: %s, offset: %s, limit: %s"
            % (
                self.item_count,
                self.page_count,
                self.page_index,
                self.page_size,
                self.offset,
                self.limit,
            )
        )

    __repr__ = __str__


class JSONEncoder(json.JSONEncoder):
    """
    将json格式的题目中不符合规范的数值类型进行转换
    """

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


class BackDataKeyConvention(object):

    def __call__(self, back_doc):
        changed_key_doc = self.change_naming_convention(back_doc, self._underline_to_camel)
        changed_type_doc = json.loads(JSONEncoder().encode(changed_key_doc))
        return changed_type_doc

    @classmethod
    def change_naming_convention(cls, origin, convert_function: Callable):
        if isinstance(origin, list):
            new_list = []
            for info in origin:
                new_list.append(cls.change_naming_convention(info, convert_function))
            return new_list
        elif isinstance(origin, dict):
            new_dict = {}
            for k, v in origin.items():
                if isinstance(v, dict):
                    new_v = cls.change_naming_convention(v, convert_function)
                elif isinstance(v, list):
                    new_v = [cls.change_naming_convention(x, convert_function) for x in v]
                else:
                    new_v = v
                new_dict[convert_function(k)] = new_v
            return new_dict
        else:
            return origin

    @classmethod
    def _underline_to_camel(cls, name):
        under_pat = re.compile(r"_([0-9a-z])")
        return under_pat.sub(lambda x: x.group(1).upper(), name)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
