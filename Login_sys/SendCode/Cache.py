class Cache:
    """
    Class used for storing a data
    from one instance and allow
    a different class instance to
    access this data.
    """
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
        """Return the data by calling this class"""
        return self._state['Data']
