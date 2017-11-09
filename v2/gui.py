# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(933, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.kValueSlider = QtGui.QSlider(self.centralwidget)
        self.kValueSlider.setGeometry(QtCore.QRect(10, 40, 181, 41))
        self.kValueSlider.setAutoFillBackground(True)
        self.kValueSlider.setMinimum(4)
        self.kValueSlider.setMaximum(16)
        self.kValueSlider.setSliderPosition(6)
        self.kValueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.kValueSlider.setInvertedControls(False)
        self.kValueSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.kValueSlider.setTickInterval(1)
        self.kValueSlider.setObjectName(_fromUtf8("kValueSlider"))
        self.applyButton = QtGui.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(80, 100, 99, 27))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.kanonText = QtGui.QLineEdit(self.centralwidget)
        self.kanonText.setGeometry(QtCore.QRect(30, 10, 101, 27))
        self.kanonText.setMaxLength(15)
        self.kanonText.setFrame(False)
        self.kanonText.setEchoMode(QtGui.QLineEdit.Normal)
        self.kanonText.setReadOnly(True)
        self.kanonText.setObjectName(_fromUtf8("kanonText"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(203, 0, 16, 561))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.kValueHolder = QtGui.QLineEdit(self.centralwidget)
        self.kValueHolder.setGeometry(QtCore.QRect(20, 100, 31, 27))
        self.kValueHolder.setObjectName(_fromUtf8("kValueHolder"))
        self.imageHolder = QtGui.QLabel(self.centralwidget)
        self.imageHolder.setGeometry(QtCore.QRect(240, 20, 640, 480))
        self.imageHolder.setText(_fromUtf8(""))
        self.imageHolder.setObjectName(_fromUtf8("imageHolder"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.kValueSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.kValueHolder.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # custom code
        self.imageHolder.setPixmap(QtGui.QPixmap('plot.png'))
        self.applyButton.clicked.connect(self.applyButtonClicked)
        self.kValueSlider.valueChanged.connect(self.displayChange)

    def applyButtonClicked(self):
        print("Apply button pressed ",self.kValueSlider.value())

    def displayChange(self, val):
        print(val)
        self.kValueHolder.setText(str(val))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.applyButton.setText(_translate("MainWindow", "Apply", None))
        self.kanonText.setText(_translate("MainWindow", "k-anonimizer", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

