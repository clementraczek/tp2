class InvalidYearException(Exception):
    def __init__(self, message="Année de production invalide."):
        super().__init__(message)