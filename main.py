class CustomException1(BaseException):
    pass

class CustomException2(BaseException):
    pass

class CustomException3(BaseException):
    pass




class CustomException1(BaseException):
    def __init__(self, message):
        self.message = message

class CustomException2(BaseException):
    def __init__(self, code):
        self.code = code

class CustomException3(BaseException):
    def __init__(self, details):
        self.details = details



try:

except CustomException1 as e:
    print(e.message)



