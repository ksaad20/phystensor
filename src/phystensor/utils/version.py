import platform
import sys
from phystensor.io.version import __version__

def get_system_report() -> dict:
    """
    Generates a comprehensive diagnostic report of the environment.
    Essential for 'Xylema Private Limited' internal auditing and 
    professional API support.
    """
    return {
        "phystensor_version": __version__,
        "python_version": sys.version.split()[0],
        "numpy_version": __import__("numpy").__version__,
        "os": platform.system(),
        "arch": platform.machine(),
        "status": "Operational"
    }

def print_banner():
    """Outputs the library's identity to the console/logs on initialization."""
    report = get_system_report()
    banner = (
        f"--- Phystensor Engine ---\n"
        f"Version: {report['phystensor_version']}\n"
        f"Platform: {report['os']} ({report['arch']})\n"
        f"Logic: Century-Proof SI-Base\n"
        f"-------------------------"
    )
    print(banner)
