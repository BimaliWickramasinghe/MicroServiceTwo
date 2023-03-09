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

class DeleteFileRequest(_message.Message):
    __slots__ = ["file_name"]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class DeleteFileResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ["file_path"]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ["error_message", "file_contents", "success"]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    file_contents: str
    success: bool
    def __init__(self, success: bool = ..., file_contents: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ["data", "file_name"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    file_name: str
    def __init__(self, file_name: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
