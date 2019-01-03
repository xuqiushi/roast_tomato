#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuration
"""
import config_default
import logging

logging.basicConfig(
    level=logging.NOTSET,
    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
)


class ClassDict(dict):
    """
    Simple dict but support access as x.y style.
    """

    def __init__(self, names=(), values=(), **kw):
        super(ClassDict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'ClassDict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def to_class_dict(d):
    class_dict = ClassDict()
    for k, v in d.items():
        class_dict[k] = to_class_dict(v) if isinstance(v, dict) else v
    return class_dict


configs = config_default.configs

try:
    import config_override

    configs = merge(configs, config_override.configs)
except ImportError:
    config_override = None
    logging.info("You don't have a config_override file.")

configs = to_class_dict(configs)
