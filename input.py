import threading
import networkx as nx
import matplotlib.pyplot as plt
from random import randrange

class fileReaderThread (threading.Thread):
   def __init__(self, threadID, name , function, fileName):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.function = function
      self.fileName = fileName
   def run(self):
      # print ("Starting " + self.name)
      self.function(self.fileName)
      # print ("Exiting " + self.name)

nodes = []
edges = []

def nodeReader(fileName):
   try:
      with open(fileName,"r") as file:
         for line in file:
            try:
               nodes.append(int(line))
            except ValueError as v:
               print ("file found an invalid node : ", v)
               continue
   except FileNotFoundError as e :
      print("file was not found : ", e)

def edgeReader(fileName):
   try:
      with open(fileName, "r") as file:
         for line in file:
            try:
               v1,v2 = line.split(',')
               edges.append((int(v1),int(v2)))
            except ValueError as v:
               print("file has an invalid edge : ",v)
               continue
   except FileNotFoundError as e :
      print("file was not found : ", e)

def kAnonimizer ( degreeSequence , nodeId , n , k):
    originalDegreeSequence = degreeSequence
    anonymizedDegreeSequence = degreeSequence
    k_constant = k
    for i in range(n):
        if i < k :
            if i == 0:
                anonymizedDegreeSequence[i] = originalDegreeSequence[i]
            else:
                anonymizedDegreeSequence[i] = anonymizedDegreeSequence[i-1]
        else:
            if ( ( k + k_constant) < n ):
                d_ik = anonymizedDegreeSequence[i - k_constant]
                d_i = anonymizedDegreeSequence[i]
                idk1 = 0 
                idk2 = 0 
                for _len in range(k+2,k+k_constant+2):
                    idk1 = idk1 + anonymizedDegreeSequence[k+2] - anonymizedDegreeSequence[_len]
                c_merge = d_ik - d_i + idk1
                for _len in range(k+1,k+k_constant+1):
                    idk2 = idk2 + anonymizedDegreeSequence[k+1] - anonymizedDegreeSequence[_len]
                c_new = idk2
                if c_new >= c_merge:
                    anonymizedDegreeSequence[i] = anonymizedDegreeSequence[i-1]
                    k += 1
                else:
                    k = i + k_constant + 1
            else:
                if ( k+k_constant == n ):
                    k = n
                else:
                    k = n
                    i-=1
    return anonymizedDegreeSequence 


# print(nodes, edges)
# Create new threads

thread1 = fileReaderThread(1, "nodeInputThread", nodeReader, "nodeList.txt")
thread2 = fileReaderThread(2, "edgeInputThread", edgeReader, "edgeList.txt")

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()

# print(nodes, edges)
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
view = nx.degree(G)
view = sorted(view, key= lambda x: x[1] , reverse= True)
degreeSequence = list(value for key,value in view)
nodeId = list(key for key,value in view)
initialView = {}
for key,value in view:
    initialView[key] = value
# nx.draw(G)
# plt.savefig("plot.png")
# plt.show()    
# print ("corresponding nodes :",nodeId)
# print ("originalDegreeSequence: ",degreeSequence)
degreeSequence = (kAnonimizer(degreeSequence,nodeId,len(nodeId),2))
# print("anonymizedDegreeSequence : ", degreeSequence)
finalView = {}
for i in range(len(nodeId)):
    finalView[nodeId[i]] = degreeSequence[i]
print ("initial view : ", initialView)
print ("final view   : ",finalView)

def removeValues( nodes ):
    keylist = list(key for key in nodes)
    for i in range(len(keylist)):
        if nodes[keylist[i]] == 0:
            nodes.pop(keylist[i])
    return nodes

remaining = {}
for key in initialView:
    if initialView[key] != finalView[key]:
        remaining[key] = finalView[key] - initialView[key]


print(remaining)


while len(remaining) > 1:
    for i in range(len(remaining)):
        remaining = removeValues(remaining)
        keylist = list(key for key in remaining)
        if len(remaining) == 1:
            break
        for j in range(i+1,len(remaining)):
            if (keylist[i], keylist[j]) not in G.edges():
                G.add_edge(keylist[i],keylist[j])
                remaining[keylist[i]]-=1
                remaining[keylist[j]]-=1
            else:
                randomIndex = randrange(0,len(keylist))
                while (keylist[i],keylist[randomIndex]) not in G.edges():
                    randomIndex= randrange(0,len(keylist))
                G.add_edge(keylist[i],keylist[j])
                remaining[keylist[i]]-=1
                remaining[keylist[randomIndex]]-=1
            remaining = removeValues(remaining)
            keylist = list(key for key in remaining)
nx.draw(G)
plt.show()