# CUSTOM ERROR USAGE EXAMPLE
class CustomError(Exception):
    pass


class ValueTooHighError(CustomError):
    def __init__(self, value, max_value):
        self.value = value
        self.max_value = max_value
        super().__init__(f"Value {value} is too high. Maximum allowed value is {max_value}")


class ValueTooLowError(CustomError):
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value
        super().__init__(f"value {value} is too low. minimum value required is {min_value}")


def process_value(value):
    min_allowed = 0
    max_allowed = 100

    try:
        if value < min_allowed:
            raise ValueTooLowError(value, min_allowed)
        elif value > max_allowed:
            raise ValueTooHighError(value, max_allowed)
        else:
            print(f"Value {value} is within the allowed range.")
    except CustomError as e:
        print(f"Caught custom error : {e}")


##############################################

try:
    process_value(150)
except CustomError as ce:
    print(f"Caught a custom error {ce}")

try:
    process_value(-10)
except CustomError as ce:
    print(ce)

try:
    process_value(50)
except CustomError as ce:
    print(ce)
