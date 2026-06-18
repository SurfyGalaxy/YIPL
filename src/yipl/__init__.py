__version__ = "1.0.1"

from .functions import (
    variables,
    program_list,
    pc,
    init,
    printy,
    set,
    equality,
    greater,
    less,
    ory,
    andy,
    noty,
    add,
    minus,
    multiply,
    divide,
    goto,
    ify,
    inputy,
    cast,
    blahaj,
    list_length,
    list_read_index,
    list_delete,
    list_append,
    list_replace_index
)

from .index import findfunc

# Define what's available when someone does "from yipl import *"
__all__ = [
    'variables',
    'program_list',
    'pc',
    'init',
    'printy',
    'set',
    'equality',
    'greater',
    'less',
    'ory',
    'andy',
    'noty',
    'add',
    'minus',
    'multiply',
    'divide',
    'goto',
    'ify',
    'inputy',
    'cast',
    'blahaj',
    'list_length',
    'list_read_index',
    'list_delete',
    'list_append',
    'list_replace_index',
    'findfunc'
]