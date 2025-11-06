class InvalidGenreException(Exception):
    def __init__(self, message="Genre du film invalide."):
        super().__init__(message)