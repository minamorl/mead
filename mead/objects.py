from abc import ABCMeta

class Resource(metaclass=ABCMeta):
    """ Interface for user"""

    def put(self, ctx):
        pass

    def get(self, ctx):
        pass

    def put(self, ctx):
        pass

    def delete(self, ctx):
        pass

    def post(self, ctx):
        pass

class Context(dict):
    pass

class Result(dict):
    pass
