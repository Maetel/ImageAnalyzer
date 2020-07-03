import sys
from PyQt5.QtWidgets import QApplication
from AnalyzerMainWindow import AnalyzerMainWindow

if __name__ == "__main__":
    theApp = QApplication(sys.argv)
    ex = AnalyzerMainWindow()
    sys.exit(theApp.exec_())