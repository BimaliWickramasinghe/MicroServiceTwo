from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ["file_contents", "file_name"]
    FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_contents: bytes
    file_name: str
    def __init__(self, file_name: _Optional[str] = ..., file_contents: _Optional[bytes] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
