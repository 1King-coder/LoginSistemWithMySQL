class Responses:
    @staticmethod
    def raise_error(responser, msg):
        responser.setStyleSheet('*{color: red;}')
        responser.setText(msg)

    @staticmethod
    def raise_alert(responser, msg):
        responser.setStyleSheet('*{color: orange;}')
        responser.setText(msg)

    @staticmethod
    def success_message(responser, msg):
        responser.setStyleSheet('*{color: green;}')
        responser.setText(msg)

    @staticmethod
    def clear(responser, inputs):
        for input_ in inputs:
            input_.setText('')
        responser.setText('')
