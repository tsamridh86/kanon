# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from backend import *
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

    nodes = []
    edges = []
    graph = nx.Graph()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(933, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.kValueSlider = QtGui.QSlider(self.centralwidget)
        self.kValueSlider.setGeometry(QtCore.QRect(10, 40, 181, 41))
        self.kValueSlider.setAutoFillBackground(True)
        self.kValueSlider.setMinimum(2)
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
        self.kanonText.setGeometry(QtCore.QRect(50, 10, 101, 27))
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
        self.statsHolder = QtGui.QPlainTextEdit(self.centralwidget)
        self.statsHolder.setGeometry(QtCore.QRect(20, 150, 171, 391))
        self.statsHolder.setObjectName(_fromUtf8("statsHolder"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Node = QtGui.QAction(MainWindow)
        self.actionAdd_Node.setObjectName(_fromUtf8("actionAdd_Node"))
        self.actionAdd_Edge = QtGui.QAction(MainWindow)
        self.actionAdd_Edge.setObjectName(_fromUtf8("actionAdd_Edge"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDocs = QtGui.QAction(MainWindow)
        self.actionDocs.setObjectName(_fromUtf8("actionDocs"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionRemove_Files = QtGui.QAction(MainWindow)
        self.actionRemove_Files.setObjectName(_fromUtf8("actionRemove_Files"))
        self.menuFile.addAction(self.actionAdd_Node)
        self.menuFile.addAction(self.actionAdd_Edge)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionRemove_Files)
        self.menuHelp.addAction(self.actionDocs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.kValueSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.kValueHolder.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # custom code
        self.applyButton.clicked.connect(self.applyButtonClicked)
        self.kValueSlider.valueChanged.connect(self.displayChange)
        self.kValueHolder.setText(str(self.kValueSlider.value()))
        self.actionAdd_Node.triggered.connect(self.nodeOpener)
        self.actionAdd_Edge.triggered.connect(self.edgeOpener)
        self.actionExit.triggered.connect(self.goOut)
        self.actionRemove_Files.triggered.connect(self.clearFiles)
        self.graph = self.plotNetwork()

    def applyButtonClicked(self):
        print("Apply button pressed ",self.kValueSlider.value())
        kValue = int(self.kValueHolder.text())
        self.kValueSlider.setValue(kValue)
        anonimize(self.graph,kValue)
        self.plotNetwork()
        statstring = getstats(self.graph)
        self.statsHolder.setText(statstring)

    def displayChange(self, val):
        self.kValueHolder.setText(str(val))

    def nodeOpener(self):
        nodeFile = self.fileOpener()
        self.nodes = nodeReader(nodeFile,self.nodes)
        self.graph = self.plotNetwork()

    def edgeOpener(self):
        edgeFile = self.fileOpener()
        self.edges = edgeReader(edgeFile,self.edges)
        self.graph = self.plotNetwork()

    def fileOpener(self):
        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        dlg.exec_()
        fileNames = dlg.selectedFiles()
        return (fileNames[0])

    def plotNetwork(self):
        graph = generateNetwork(self.nodes,self.edges,self.graph)
        self.imageHolder.setPixmap(QtGui.QPixmap('plot.png'))
        return graph

    def clearFiles(self):
        self.nodes = []
        self.edges = []
        self.graph = clearNetwork(self.graph)
        self.graph = self.plotNetwork()

    def goOut(self):
        sys.exit()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.applyButton.setText(_translate("MainWindow", "Apply", None))
        self.kanonText.setText(_translate("MainWindow", "k-anonimizer", None))
        self.statsHolder.setPlainText(_translate("MainWindow", "Stats:\n"
"No. of Nodes :\n"
"No. of Edges  :\n"
"Avg Degree in graph :\n", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionAdd_Node.setText(_translate("MainWindow", "Add Node", None))
        self.actionAdd_Edge.setText(_translate("MainWindow", "Add Edge", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionDocs.setText(_translate("MainWindow", "Docs", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionRemove_Files.setText(_translate("MainWindow", "Remove Files", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

