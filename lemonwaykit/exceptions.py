# -*- coding: utf-8 -*-
class LemonWayInvalidParameterError(Exception):
    pass


class LemonWayApiMethodError(Exception):

    def __init__(self, code, message, priority):
        self.code = code
        self.message = message
        self.priority = priority

    def __unicode__(self):
        return 'Error {1} : {0}'.format(self.message, self.code)

    def __str__(self):
        return 'Error {1} : {0}'.format(self.message, self.code)
