# -*- coding: utf-8 -*-
class LemonWayInvalidParameterError(Exception):
    pass


class LemonWayApiMethodError(Exception):
    def __init__(self, code, message, priority):
        self.code = code
        self.message = message
        self.priority = priority