from __future__ import unicode_literals
import sys


class InvalidParameterError(Exception):
    pass


class ApiMethodError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __repr__(self):
        return self.__str__()

    if sys.version > '3':
        __str__ = __unicode__
    else:
        def __str__(self):
            return self.__unicode__().encode('utf-8')

    def __unicode__(self):
        return '{0} - {1}'.format(self.code, self.message)
