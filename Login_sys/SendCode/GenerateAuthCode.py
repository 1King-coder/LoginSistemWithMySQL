from random import randint


def generate_auth_code() -> str:
    """
    Generate a six-numbers random code.
    """
    code = ''
    for _ in range(6):
        code += str(randint(0, 9))

    return code


class Get_Auth_Code:
    """
    Monostate for storing a generated code
    """
    _state: dict = {
        'AuthCode': generate_auth_code()
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, flag=None):
        """
        Flag for saving a code for use
        and after it, generate another.
        """
        if flag is not None:
            self._state['AuthCode'] = generate_auth_code()

    def __str__(self):
        """
        Return the generated code when
        the class is called as a string
        """
        return self._state['AuthCode']
