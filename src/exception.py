"""We are writing our now custom exeception"""

import sys
from src.logger import logging
#The error_details parameter is annotated with the type sys, indicating that it expects an object from the sys module.

def error_massage_detail(error,error_details:sys):
#_, _, exc_tb = error_details.exc_info(), it is used to discard the first two elements of the tuple returned by error_details.exc_info().
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename  
    error_massage ="Error occured in the python script name [{0}] line number [{1}] error massage [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    
    return error_massage




class CustomException(Exception):
    def __init__(self,error_massage,error_detail:sys):
        super().__init__(error_massage)
        self.error_massage=error_massage_detail(error_massage,error_details=error_detail)
        
    def __str__(self):
        return self.error_massage 