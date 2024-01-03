__author__ = 'Graham'


class ResponseObject():
    def __init__(self,request,status,information,data,dict):
            self.status = False  #  status to be sent back True=OK False=Bad
            self.information = None  #  any messages etc
            self.data = None  #  data to which this pertains e.g. userid
            self.dict = {}  #  dictionary of errors
