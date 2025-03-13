#!/usr/bin/env python3
""" Validator module
"""
import re

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def is_valid_email(email):
    """Check if the email follows a valid format.
    """
    return re.match(EMAIL_REGEX, email) is not None
