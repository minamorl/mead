from abc import ABCMeta, abstractmethod


class Resource(metaclass=ABCMeta):
    """Interface for user"""
    @abstractmethod
    def put(self, ctx=None):
        pass

    @abstractmethod
    def get(self, ctx=None):
        pass

    @abstractmethod
    def delete(self, ctx=None):
        pass

    @abstractmethod
    def post(self, ctx=None):
        pass


class Context(dict):
    pass


class Result(dict):
    pass


class Session(dict):
    pass
