import sys
import os
from Cyber_intro.logging.logger import logging

class CyberException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message
        _, _, exe_tb = error_details.exc_info()

        self.line_no = exe_tb.tb_lineno
        self.file_name = exe_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in python script name [{0}] at line number [{1}] with error message [{2}]".format(
            self.file_name, self.line_no, str(self.error_message)
        )


