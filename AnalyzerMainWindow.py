from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QFileDialog, QMessageBox, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from Notifier import Notifier

class AnalyzerMainWindow(QMainWindow):
    #main
    mainWidget = None
    mainLayout = None
    leftLayout = rightLayout = None
    leftWidget = rightWidget = None

    #left
    imageLabel = None
    imageViewer = None
    loadButton = None

    #right
    analysisLabel = None

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle("Image Analyzer")
        self.leftLayout = QVBoxLayout()
        self.rightLayout = QVBoxLayout()

        #left
        self.imageLabel = QLabel("Image")
        self.imageViewer = QLabel()
        self.loadButton = QPushButton("Load Image")
        self.loadButton.clicked.connect(self.loadImage)
        self.leftLayout.addWidget(self.imageLabel)
        self.leftLayout.addWidget(self.imageViewer)
        self.leftLayout.addWidget(self.loadButton)

        #right
        self.analysisLabel = QLabel("Analysis")
        self.rightLayout.addWidget(self.analysisLabel)

        #main widget
        self.leftWidget = QWidget()
        self.rightWidget = QWidget()
        self.leftWidget.setLayout(self.leftLayout)
        self.rightWidget.setLayout(self.rightLayout)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.leftWidget)
        self.mainLayout.addWidget(self.rightWidget)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)


    def loadImage(self):
        fileName = QFileDialog.getOpenFileName(QFileDialog(), "Load Image", "", "Image (*.png, *.jpg)")
        if fileName[0] == '':
            Notifier.Alert(message="No image selected!")
            return
        self.imageViewer.setPixmap(QPixmap(fileName[0]))
