class PhystensorError(Exception):
    """Base exception for the library."""
    pass

class DimensionalityError(PhystensorError):
    """Raised when an operation violates the laws of physics."""
    def __init__(self, message: str):
        self.message = f"Physical Law Violation: {message}"
        super().__init__(self.message)

class UnitNotFoundError(PhystensorError):
    """Raised when a unit symbol is not in the registry."""
    pass

class RegistrationError(PhystensorError):
    """Raised when attempting to register an invalid unit or constant."""
    pass
