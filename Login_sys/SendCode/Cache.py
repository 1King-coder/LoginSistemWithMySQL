class Cache:
    _state: dict = {
        'Data': ''
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, data=None):
        if data is None:
            return
        self._state['Data'] = data

    def __call__(self):
        return self._state['Data']
