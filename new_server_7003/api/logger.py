import warnings
from typing import Literal, Type
"""
Logging Module (Helps decrease or easier formatting)
"""


"Dict For Warning Stuff"
warn_dict = [
    UserWarning,
    DeprecationWarning,
    SyntaxWarning,
    RuntimeWarning,
    FutureWarning,
    ImportWarning,
    ResourceWarning,
    BytesWarning,
    UnicodeWarning
    ]

def module_log(message: str, module_name: str) -> str:
    print(f'[{module_name}] {message}')
    
def warn_log(message: str, module_name: str, warn_type: warn_dict) -> str:
    warnings.warn(
        f'[{module_name}] {message}',
        category=warn_type,
        stacklevel=2
        )

def error_log(message: str, module_name: str) -> str:
    print(f'[Error] [{module_name}] {message}')
