
class InvalidTitleException(Exception):
    def __init__(self, message="Titre du film invalide."):
        super().__init__(message)