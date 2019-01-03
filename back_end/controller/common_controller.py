#!/usr/bin/env python
# -*- coding: utf-8 -*-


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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
