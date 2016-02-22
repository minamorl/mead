import pytest
from unittest.mock import Mock
from mead.router import Router, Route
from mead.exceptions import RoutingException


@pytest.fixture
def router():
    return Router()


def test_router_allow_appending_route_object(router):
    router.append(Route(Mock(), Mock(), Mock()))
    assert len(router) == 1


@pytest.mark.xfail(raises=RoutingException)
def test_router_deny_appending_not_route_object(router):
    router.append((Mock(), Mock(), Mock()))


def test_router_add_route(router):
    _method = Mock()
    _path = Mock()
    _object = Mock()

    router.add_route(_method, _path, _method)
    assert len(router) == 1
    assert router[0].method == _method
    assert router[0].path == _path
    assert router[0].object != _object


def test_router_route(router):
    func = Mock()
    path = Mock()
    router.route(path)(func)
    assert len(router) == 1
