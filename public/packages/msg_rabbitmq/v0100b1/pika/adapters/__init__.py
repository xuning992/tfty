# ***** BEGIN LICENSE BLOCK *****
#
# For copyright and licensing please refer to COPYING.
#
# ***** END LICENSE BLOCK *****
"""Pika provides multiple adapters to connect to RabbitMQ:

- adapters.select_connection.SelectConnection: A native event based connection
  adapter that implements select, kqueue, poll and epoll.
- adapters.tornado_connection.TornadoConnection: Connection adapter for use
  with the Tornado web framework.
- adapters.blocking_connection.BlockingConnection: Enables blocking,
  synchronous operation on top of library for simple uses.
- adapters.twisted_connection.TwistedConnection: Connection adapter for use
  with the Twisted framework
- adapters.libev_connection.LibevConnection: Connection adapter for use
  with the libev event loop and employing nonblocking IO

"""
from ..adapters.base_connection import BaseConnection
from ..adapters.blocking_connection import BlockingConnection
from ..adapters.select_connection import SelectConnection
from ..adapters.select_connection import IOLoop

# Dynamically handle 3rd party library dependencies for optional imports
try:
    from ..adapters.tornado_connection import TornadoConnection
except ImportError:
    TornadoConnection = None

try:
    from ..adapters.twisted_connection import TwistedConnection
    from ..adapters.twisted_connection import TwistedProtocolConnection
except ImportError:
    TwistedConnection = None
    TwistedProtocolConnection = None

try:
    from ..adapters.libev_connection import LibevConnection
except ImportError:
    LibevConnection = None
