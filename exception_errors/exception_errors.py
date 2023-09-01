import __init__

class Error(Exception):
    """Base class for other exceptions"""
    pass

class TestFailed(Error):
    pass

class NotEnoughQuantity(Error):
    pass

class NotInPositions(Error):
    pass

class TickerNotExist(Error):
    pass

class InvalidPayload(Error):
    pass

class InvalidParameters(Error):
    pass

class UserDoesNotExistError(Error):
    pass

