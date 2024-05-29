#!/usr/bin/env python3
"""
 -- first task : 0. Regex-ing: filter_datum
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Regex-ing - Write a function called filter_datum that
        returns the log message obfuscated:

    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character
        is separating all fields in the log line

    Returns:
        a new string where all occurrences of each field in fields
        are replaced by redaction
    '''
    for field in fields:
        '''
        The re.sub function is used to search for a
        pattern in the message and
        replace it with a new string.
        '''
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator,
                         message)
    return message
