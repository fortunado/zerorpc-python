from datetime import datetime
from zerorpc import Context

__author__ = 'nemo'

from nose.tools import assert_raises
import gevent
import zerorpc
from testutils import random_ipc_endpoint


def test_kwargs():

    class Srv(object):
        def echo(self, *args, **kwargs):
            return args, kwargs

    endpoint = random_ipc_endpoint()

    context = Context()
    context.register_serializer("pickle")

    module = Srv()
    server = zerorpc.Server(module, context=context)
    server.bind(endpoint)
    gevent.spawn(server.run)

    client = zerorpc.Client(context=context)
    client.connect(endpoint)

    args = 1,2,3
    kwargs = {'a':7, 'b':8, 'now': datetime.now()}
    res = client.echo(*args, **kwargs)
    assert len(res) == 2
    assert res[0] == args
    assert len(res[1]) == 3
    assert 'a' in res[1] and 'b' in res[1] and isinstance(res[1]['now'], datetime)

    client.close()
    server.close()
