"""
enum.py

Enum types for the ACE program
"""

class ModeEnum():
    MENU = 0
    STATS = 1
    TRAINER = 2
    GENERATOR = 3
    
class FileEnum():
    SESSION_COUNT = 0
    ERROR_SUM = 1
    SESSION_LIST = 2
    LOG_ERR_LIST = 3
    TOTAL_ESTIMATES = 4
    
class SessionCol():
    STATUS = 0
    ESTIMATE = 1
    ACTUAL = 2
    EXACT = 3
    LOG_ERROR = 4
    IMAGE = 5
