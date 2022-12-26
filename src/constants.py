
"""This module defines project-level constants"""
import string

CODE_STRUCTURE = string.digits + string.ascii_letters
"""This constsnt defines the structure of the generated random codes. 
    For now the structure consists of letters and digits"""
CODE_LENGTH: int = 6
"""This constant defines the length of the generated random code"""
BASE_URL: str = "http://short.est/"
"""the base url is the url that will be used for creating short links"""

