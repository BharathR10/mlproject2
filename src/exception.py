import sys
from src.logger import logging  # Ensure this module exists

def error_message_detail(error, error_detail):
    """
    Extract detailed error message including filename, line number, and error message.
    """
    _, _, exc_tb = sys.exc_info()  # Correct usage of sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script: [{0}], Line Number: [{1}], Error Message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        """
        Custom Exception class that formats error messages.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message


        

