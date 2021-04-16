from random import randint


def generate_auth_code():
    code = ''
    for i in range(6):
        code += str(randint(0, 9))
    return code


class Get_Auth_Code:
    _state: dict = {
        'AuthCode': generate_auth_code()
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, flag=None):
        if flag is not None:
            self._state['AuthCode'] = generate_auth_code()

    def __str__(self):
        return self._state['AuthCode']
