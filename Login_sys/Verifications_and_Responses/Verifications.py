import re


class Verifications:
    @staticmethod
    def empty_fields(fields) -> bool:
        for field in fields:
            if field.strip() == '':
                return True
        return False

    @staticmethod
    def is_email(input_):
        return re.search(r'.*@.*\.com', input_)

    @staticmethod
    def special_characters(inputs):
        for input_ in inputs:
            if re.search(r'.*!.*|.*#.*|.*\$.*|.*%.*'
                         r'|.*¨.*|.*&.*|.*\*.*|.*\+.*|.*".*|.*\'.*',
                         input_):
                return True
        return False
