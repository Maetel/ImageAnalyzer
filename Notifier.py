from PyQt5.QtWidgets import QMessageBox

class Notifier:
    @staticmethod
    def Alert(title="Alert", message=""):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()