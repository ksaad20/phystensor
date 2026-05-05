import numpy as np
from phystensor.units.dimensions import Dimensions

class PhysicsFormatter:
    """Handles the visual representation of physical data."""
    
    # Map for generating human-readable SI strings from vectors
    LABELS = ["m", "kg", "s", "A", "K", "mol", "cd"]

    @classmethod
    def to_unit_string(cls, dims: Dimensions) -> str:
        """Converts a (1, 0, -2, ...) vector into 'm/s^2'."""
        pos = []
        neg = []
        
        for label, exp in zip(cls.LABELS, dims.vector):
            if exp == 0: continue
            if exp > 0:
                pos.append(f"{label}^{exp}" if exp != 1 else label)
            else:
                neg.append(f"{label}^{abs(exp)}" if exp != -1 else label)

        num = "*".join(pos) if pos else "1"
        den = "*".join(neg)
        
        return f"{num}/{den}" if den else num

    @staticmethod
    def format_tensor(data: np.ndarray, dims: Dimensions) -> str:
        unit_str = PhysicsFormatter.to_unit_string(dims)
        return f"PhysicalTensor(\n  value={data},\n  unit=[{unit_str}]\n)"
