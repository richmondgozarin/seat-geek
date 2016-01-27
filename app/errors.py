class SeatNowError(Exception):
    def __init__(self, code, desc):
        self.code = code
        self.description = desc

    def __str__(self):
        return self.description


class clientBadRequestError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 400
        self.description = "Bad Request" if desc is None else desc


class clientUnauthorizedError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 401
        self.description = "Unauthorized" if desc is None else desc


class clientPaymentRequiredError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 402
        self.description = "Payment Required" if desc is None else desc


class clientForbiddenError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 403
        self.description = "Forbidden" if desc is None else desc


class clientNotFoundError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 404
        self.description = "Not Found" if desc is None else desc


class clientMethodNotAllowedError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 405
        self.description = "Method Not Allowed" if desc is None else desc


class clientNotAcceptableError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 406
        self.description = "Not Acceptable" if desc is None else desc


class clientProxyAuthenticationRequiredError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 407
        self.description = "Proxy Authentication Required" if desc is None else desc


class clientRequestTimeoutError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 408
        self.description = "Request Timeout" if desc is None else desc


class clientConflictError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 409
        self.description = "Conflict" if desc is None else desc


class clientGoneError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 410
        self.description = "Gone" if desc is None else desc


class clientLengthRequiredError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 411
        self.description = "Length Required" if desc is None else desc


class clientPreconditionFailedError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 412
        self.description = "Precondition Failed" if desc is None else desc


class clientRequestEntityTooLargeError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 413
        self.description = "Request Entity Too Large" if desc is None else desc


class clientRequestURITooLongError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 414
        self.description = "Request-URI Too Long" if desc is None else desc


class clientUnsupportedMediaTypeError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 415
        self.description = "Unsupported Media Type" if desc is None else desc


class clientRequestedRangeNotSatisfiableError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 416
        self.description = "Requested Range Not Satisfiable" if desc is None else desc


class clientExpectationFailedError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 417
        self.description = "Expectation Failed" if desc is None else desc


class serverInternalServerError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 500
        self.description = "Internal Server Error" if desc is None else desc


class serverNotImplementedError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 501
        self.description = "Not Implemented" if desc is None else desc


class serverBadGatewayError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 502
        self.description = "Bad Gateway" if desc is None else desc


class serverServiceUnavailableError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 503
        self.description = "Service Unavailable" if desc is None else desc


class serverGatewayTimeoutError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 504
        self.description = "Gateway Timeout" if desc is None else desc


class serverHTTPVersionNotSupportedError(SeatNowError):
    def __init__(self, desc=None):
        self.code = 505
        self.description = "HTTP Version Not Supported" if desc is None else desc

