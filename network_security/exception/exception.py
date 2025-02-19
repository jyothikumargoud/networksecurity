import sys
import logging
from network_security.logging import logger
from network_security.exception import exception

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detail):
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()

        self.lineno = exc_tb.tb_lineno  # gives u the lineno of the error detail
        self.file_name = exc_tb.tb_frame.f_code.co_filename  #  tb_frame --- acts as a stack error indicator and give the error place and co_filename -- gives the errored filename

        def __str__(self):
            return "Error occured in python script name[{0}] line number[{1}] error message [{2}]".format(self.file_name,self.lineno),str(self.error_message)

