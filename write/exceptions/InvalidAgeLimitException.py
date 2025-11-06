class InvalidAgeLimitException(Exception):
    def __init__(self, message="erreur âge limite"):
        super().__init__(message)