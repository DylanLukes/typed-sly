# sly/ast.py
from __future__ import annotations

import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


class AST(object):
    @classmethod
    def __init_subclass__(cls, **kwargs: Any):
        mod = sys.modules[cls.__module__]
        if not hasattr(cls, '__annotations__'):
            return

        hints = list(cls.__annotations__.items())

        def __init__(self: cls, *args: Any, **kwargs: Any):
            if len(hints) != len(args):
                raise TypeError(f'Expected {len(hints)} arguments')
            for arg, (name, val) in zip(args, hints):
                if isinstance(val, str):
                    val = getattr(mod, val)
                if not isinstance(arg, val):
                    raise TypeError(f'{name} argument must be {val}')
                setattr(self, name, arg)

        cls.__init__ = __init__
