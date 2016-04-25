class JotiHuntException(Exception):
    pass


class NoSuchTypeException(JotiHuntException):
    pass


class RetrieveException(JotiHuntException):
    pass
