from collections import namedtuple
from typing import Any, Optional

PY2: Any

_Writer = namedtuple('_Writer', 'writerow writerows')
unichr = unichr
text_type = unicode
string_types: Any

def to_native(source: Any, encoding: str = ..., falsy_empty: bool = ...): ...

integer_types: Any

def implements_to_string(cls): ...
def implements_iterator(cls): ...
def csv_reader(stream: Any, **params: Any) -> None: ...
def csv_writer(stream: Any, **params: Any): ...
unichr = chr
text_type = str
imap = map
izip = zip
ifilter = filter

def reraise(tp: Any, value: Any, tb: Optional[Any] = ...) -> None: ...

_reader: Any
_writer: Any

def to_text(source: Any): ...
