import threading
import networkx as nx
import matplotlib.pyplot as plt

class fileReaderThread (threading.Thread):
   def __init__(self, threadID, name , function, fileName):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.function = function
      self.fileName = fileName
   def run(self):
      # print ("Starting " + self.name)
      # self.function(self.fileName)
      # print ("Exiting " + self.name)
      pass

# nodes = []
# edges = []

def nodeReader(fileName , nodes):
   try:
      with open(fileName,"r") as file:
         for line in file:
            try:
               nodes.append(int(line))
            except ValueError as v:
               print ("file found an invalid node : ", v)
               continue
      return nodes
   except FileNotFoundError as e :
      print("file was not found : ", e)

def edgeReader(fileName,edges):
   try:
      with open(fileName, "r") as file:
         for line in file:
            try:
               v1,v2 = line.split(',')
               edges.append((int(v1),int(v2)))
            except ValueError as v:
               print("file has an invalid edge : ",v)
               continue
      return edges
   except FileNotFoundError as e :
      print("file was not found : ", e)

def generateNetwork(nodes,edges):
   G = nx.Graph()
   G.add_nodes_from(nodes)
   G.add_edges_from(edges)
   nx.draw(G)
   plt.savefig("plot.png")
   return G

def clearNetwork():
   G = nx.Graph()
   nx.draw(G)
   plt.savefig("plot.png")

# print(nodes, edges)
# Create new threads

# thread1 = fileReaderThread(1, "nodeInputThread", nodeReader, "nodeList.txt")
# thread2 = fileReaderThread(2, "edgeInputThread", edgeReader, "edgeList.txt")

# Start new Threads
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# print(nodes, edges)
# G = nx.Graph()
# G.add_nodes_from(nodes)
# G.add_edges_from(edges)
# nx.draw(G)
# plt.savefig("plot.png")
# plt.show()