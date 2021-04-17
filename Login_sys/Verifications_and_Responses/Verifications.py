from re import search


class Verifications:
    @staticmethod
    def empty_fields(fields) -> bool:
        for field in fields:
            if field.strip() == '':
                return True

        return False

    @staticmethod
    def is_email(input_) -> bool:
        if search(r'@.*\.com', input_):
            return True

        else:
            return False

    @staticmethod
    def special_characters(inputs) -> bool:
        for input_ in inputs:
            if search(r'.*!.*|.*#.*|.*\$.*|.*%.*'
                      r'|.*¨.*|.*&.*|.*\*.*|.*\+.*|.*".*|.*\'.*',
                      input_):
                return True

        return False
