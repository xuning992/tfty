# API Backwards compatibility

from .base import Client  # noqa
from .base import PooledClient  # noqa

from ..exceptions import MemcacheError  # noqa
from ..exceptions import MemcacheClientError  # noqa
from ..exceptions import MemcacheUnknownCommandError  # noqa
from ..exceptions import MemcacheIllegalInputError  # noqa
from ..exceptions import MemcacheServerError  # noqa
from ..exceptions import MemcacheUnknownError  # noqa
from ..exceptions import MemcacheUnexpectedCloseError  # noqa
