import sys
from PyQt4 import QtCore, QtGui,uic
from backend import *

class MyWindow(QtGui.QMainWindow):

    nodes = []
    edges = []
    graph = nx.Graph()

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('gui.ui', self)
        self.show()
        self.applyButton.clicked.connect(self.applyButtonClicked)
        self.kValueSlider.valueChanged.connect(self.displayChange)
        self.kValueHolder.setText(str(self.kValueSlider.value()))
        self.actionAdd_Node.triggered.connect(self.nodeOpener)
        self.actionAdd_Edge.triggered.connect(self.edgeOpener)
        self.actionExit.triggered.connect(self.goOut)
        self.actionRemove_Files.triggered.connect(self.clearFiles)
        self.actionSave_as.triggered.connect(self.saveFile)
        self.graph = self.plotNetwork()

    def applyButtonClicked(self):
        kValue = int(self.kValueHolder.text())
        if kValue > len(self.graph):
            kValue = len(self.graph)-1
            print("Exceeded max k value")
        self.kValueSlider.setValue(kValue)
        anonimize(self.graph,kValue)
        self.plotNetwork()

    def displayChange(self, val):
        self.kValueHolder.setText(str(val))

    def nodeOpener(self):
        nodeFile = self.fileOpener()
        self.nodes = nodeReader(nodeFile,self.nodes)
        self.graph = self.plotNetwork()
        self.setMaxSliderValue()

    def edgeOpener(self):
        edgeFile = self.fileOpener()
        self.edges = edgeReader(edgeFile,self.edges)
        self.graph = self.plotNetwork()
        self.setMaxSliderValue()

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
        statstring, avgDegree , avgPathLenght , avgClustering , edgeBetweeness = getstats(graph)
        self.statsHolder.setPlainText(statstring.format(avgDegree,avgPathLenght,avgClustering,edgeBetweeness))
        return graph

    def clearFiles(self):
        self.nodes = []
        self.edges = []
        self.graph = clearNetwork(self.graph)
        self.graph = self.plotNetwork()

    def goOut(self):
        sys.exit()

    def setMaxSliderValue(self):
        if len(self.graph) == 0:
            self.kValueSlider.setMaximum(16)
        else:
            self.kValueSlider.setMaximum(len(self.graph))

    def saveFile(self):
        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        dlg.exec_()
        folderName = dlg.selectedFiles()
        saveToFile(folderName[0],self.graph)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())