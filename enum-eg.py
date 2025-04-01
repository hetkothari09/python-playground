from enum import Enum

class Department(Enum):
    HR = "hr"
    MARKETING = "marketing"
    SALES = "sales"
    TECH = "tech"
    ACCOUNTS = "accounts"

# print(Department.HR)
# print(Department.HR.name)
# print(Department.HR.value)


'''
Basically Enum is used when you want to bind some values to specific strings.
This helps the code to be more readable and proves to be efficient.
You can use specific strings instead of magical numbers, which proves beneficial
'''
class ErrorCode(Enum):
    NOT_FOUND = 404
    BAD_REQUEST = 415
    UNAUTHORIZED = 400
    SERVER_ERROR = 512

def catch_error(code):

    # Converting the integer code to enum
    if isinstance(code, int):
        code = ErrorCode(code)

    if code == ErrorCode.NOT_FOUND:
        print("The resource is unable to reach!")
    elif code == ErrorCode.BAD_REQUEST:
        print("The mentioned parameters are wrong!")
    elif code == ErrorCode.UNAUTHORIZED:
        print("You are unauthorized to access this resource!")
    elif code == ErrorCode.SERVER_ERROR:
        print("The server is down currently! Please Try Again Later!")
    else:
        print("Unknown Code!")


if __name__ == '__main__':
    catch_error(512)