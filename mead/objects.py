from abc import ABCMeta, abstractmethod

class Resource(metaclass=ABCMeta):
    """ Interface for user"""
    @abstractmethod
    def put(self, ctx):
        pass

    @abstractmethod
    def get(self, ctx):
        pass

    @abstractmethod
    def delete(self, ctx):
        pass

    @abstractmethod
    def post(self, ctx):
        pass

class Context(dict):
    pass

class Result(dict):
    pass
