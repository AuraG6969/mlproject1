import sys
import logging

def error_message_detail(error,error_detail:sys): #this error_detail stored inside the sys
    _,_,exc_tb=error_detail.exc_info() #this exc_info() provide info about error konse file m ,konse line me
    file_name=exc_tb.tb_frame.f_code.co_filename # for getting file name
    error_message='error occured in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name,exc_tb.tb_lineno,str(error)
        
        )
    return error_message

class CustomException(Exception):
    def  __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
