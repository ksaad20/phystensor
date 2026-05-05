from abc import ABC, abstractmethod
import numpy as np
from phystensor.units.dimensions import Dimensions

class PhysicalBase(ABC):
    """
    The primal interface for all physical quantities.
    Enforces the presence of data and SI-base dimensionality.
    """
    
    @property
    @abstractmethod
    def data(self) -> np.ndarray:
        """The underlying numerical value(s)."""
        pass

    @property
    @abstractmethod
    def dimensions(self) -> Dimensions:
        """The 7-tuple SI dimension vector."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
