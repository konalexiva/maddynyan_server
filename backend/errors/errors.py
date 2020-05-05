from enum import IntEnum


class Errors(IntEnum):
    NOT_AUTHORIZED = 401
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500
    ACCESS_DENIED = 403
    NOT_FOUND = 404
    INVALID_ACCESS_TOKEN = 520


class ClientErrors(IntEnum):
    USER_NOT_FOUND = 1004
