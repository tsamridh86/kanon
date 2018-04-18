import networkx as nx
import matplotlib.pyplot as plt
from random import randrange
import time
def timeIt(function):
	def wrapper (*args , **kwargs ):
		start = time.time()
		result = function(*args,**kwargs)
		end = time.time()
		print(function.__name__," took ",str((end-start)*1000), "mil sec")
		return result
	return wrapper


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

@timeIt
def edgeReader(fileName,edges):
   try:
      with open(fileName, "r") as file:
         for line in file:
            try:
               v1,v2 = line.split(' ')
               edges.append((int(v1),int(v2)))
            except ValueError as v:
               print("file has an invalid edge : ",v)
               continue
      return edges
   except FileNotFoundError as e :
      print("file was not found : ", e)

def drawGraph(graph):
   nx.draw(graph,node_size=100)
   plt.savefig("plot.png")
   plt.gcf().clear()

def generateNetwork(nodes,edges,graph):
   graph.add_nodes_from(nodes)
   graph.add_edges_from(edges)
   drawGraph(graph)
   return graph

def clearNetwork(graph):
   graph.clear()
   drawGraph(graph)
   return graph

def kAnonimizer ( degreeSequence , nodeId , n , k):
    originalDegreeSequence = degreeSequence
    anonymizedDegreeSequence = degreeSequence
    k_constant = k
    c_total = 0
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
                for _len in range(k+2,k+k_constant):
                    idk1 = idk1 + anonymizedDegreeSequence[k+2] - anonymizedDegreeSequence[_len]
                c_merge = d_ik - d_i + idk1
                for _len in range(k+1,k+k_constant):
                    idk2 = idk2 + anonymizedDegreeSequence[k+1] - anonymizedDegreeSequence[_len]
                c_new = idk2
                if c_merge > c_new:
                	c_total += c_new
                else:
                	c_total += c_merge
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
    print ("\n\n\n\n Total Cost : ",c_total)
    return anonymizedDegreeSequence

def removeValues( nodes ):
    keylist = list(key for key in nodes)
    for i in range(len(keylist)):
        if nodes[keylist[i]] == 0:
            nodes.pop(keylist[i])
    return nodes

@timeIt
def anonimize(graph, kValue):
   view = nx.degree(graph)
   view = sorted(view, key= lambda x: x[1] , reverse= True)
   degreeSequence = list(value for key,value in view)
   nodeId = list(key for key,value in view)
   initialView = {}

   # initial degree sequence
   for key,value in view:
       initialView[key] = value
   # anonimized sequence
   degreeSequence = (kAnonimizer(degreeSequence,nodeId,len(nodeId),kValue))
   extra = len(nodeId) % kValue
   while extra != 0 :
       degreeSequence[-extra] = degreeSequence[-extra-1]
       extra -= 1
   
   finalView = {}
   for i in range(len(nodeId)):
       finalView[nodeId[i]] = degreeSequence[i]
   remaining = {}
   for key in initialView:
       if initialView[key] != finalView[key]:
           remaining[key] = finalView[key] - initialView[key]
   # final Compensated view
   totalIterations = sum(remaining.values())
   for _ in range(totalIterations):
        target = list(remaining.keys())[0] # choose the node to be anonimized
        print(target, remaining[target])
        print(remaining)
        
        # find friends and friend of friend
        neighbors = list(graph.neighbors(target))
        doubleNeighbours = set()
        for neighbor in neighbors:
            temp = set(list(graph.neighbors(neighbor)))
            doubleNeighbours = doubleNeighbours | temp
        neighbors = set(neighbors)
        
        # subtract those sets
        possiblePartners = list(doubleNeighbours - neighbors)
        possiblePartners.remove(target)
        # connect the nearest one possible
        if len(possiblePartners) > 0:
            print("partner",possiblePartners[0],target)
            graph.add_edge(target,possiblePartners[0])
        remaining[target] -= 1 # been processed, remove from the list
        # removes from the dict when it is empty 
        if remaining[target] == 0:
            remaining = { __ : remaining[__] for __ in remaining if __ != target }
   drawGraph(graph)
   return graph
   # z = 1          
   # # node connector
   
   # while len(remaining) > 1:
   #    if z > len(remaining):
   #      break
   #    i=0  
   #    while i < len(remaining): 
   #    #for i in range(len(remaining)):
      
   #       remaining = removeValues(remaining)
   #       keylist = list(key for key in remaining)
   #       print("remaining key list",keylist)
   #       j = i + 1
   #       print("i -j-",i,j)
   #       x = len(keylist)
   #       print("x--",x)
   #       while j < x:
      
   #          if (keylist[i], keylist[j]) not in graph.edges():
   #             graph.add_edge(keylist[i],keylist[j])
   #             remaining[keylist[i]]-=1
   #             remaining[keylist[j]]-=1
   #             remaining = removeValues(remaining)
   #             keylist = list(key for key in remaining)
   #             print("remaining in if ",remaining)
   #             break
   #          else:
   #             print("in else") 
   #             randomIndex = randrange(0,len(keylist))
   #             if((keylist[i],keylist[randomIndex]) not in graph.edges() and i != randomIndex):     
   #                 print("randomIndex",randomIndex)
   #                 print("in else connected with", keylist[randomIndex])
   #                 graph.add_edge(keylist[i],keylist[randomIndex])
   #                 remaining[keylist[i]]-=1
   #                 remaining[keylist[randomIndex]]-=1 
   #                 remaining = removeValues(remaining)
   #                 keylist = list(key for key in remaining)
   #                 break  
   #          print("in while remaining", remaining)
   #          print("keylist",keylist)
   #          x = len(keylist)
   #          j+=1

   #       print("after while i ",i)
   #       i+=1

   #    z+=1
            
         
   # remaining = removeValues(remaining)
   # keylist = list(key for key in remaining)
   # keyseq = readyToConnect(graph, kValue)
   # s=0
   # while(len(remaining)>0):
   #    if(s>len(remaining)):
   #      print("there is still remaining nodes")
   #      break
   #    # if (checkAlldegree(graph,kValue)):
   #    #   print("all satisfied")
   #    #   break
   #    i=0
   #    if(keylist[i] in remaining and len(keylist)>=i):
   #      print("key[i] is in remainning-",keylist[i])
   #      print("i",i)
   #      print("keyseq",keyseq)
   #      print("remain",remaining)
   #      if len(keyseq)==0:
   #        print("there no node avail to connect with remainings")
   #        break
   #      for p in keyseq:

   #        if((keylist[i], p) not in graph.edges() and keylist[i] != p):
   #          graph.add_edge(keylist[i], p)
   #          remaining[keylist[i]]-=1
   #          keyseq.remove(p)
   #          remaining = removeValues(remaining)
   #          keylist = list(key for key in remaining)
   #          print("connected  with",p)
   #          break
 
   #    #s+=1
   # oo = readyToConnect(graph,kValue)  #to print degree,val deictionary
   # drawGraph(graph)
   # return graph


def checkAlldegree(graph, kValue):
  oldDict = nx.degree(graph)
  newDict = {}
  for key,value in oldDict:
    if value not in newDict:
      newDict[value] = 1
    else:
      newDict[value]+=1
  for key, value in newDict.items():
     if value < kValue:
        return False    
  return True
def readyToConnect(graph, kValue):
  oldDict = nx.degree(graph)
  newDict = {}
  remain2 = []
  nseq = []
  keyseq = []
  for key,value in oldDict:
    if value not in newDict:
      newDict[value] = 1
    else:
      newDict[value]+=1
  print("graph node,degree",oldDict)     
  print("new dect-deg,sum",newDict)

                 # #ki is deg
                 # #vi is total nodes having ki same deg 
  for key, value in newDict.items():                  
    if value > kValue :
      for z in range(1,value-kValue+1):
         nseq.append(key)
    else:
      for m in range(1,kValue-value+1):
         remain2.append(key)
  #newDict[value+1] >= kValue-1 
  for key,value in oldDict:
     if value in nseq:
        keyseq.append(key)
  print("nseq",nseq)    
  print("keyseq",keyseq)
  return keyseq

def nodeDegreeLessThanK(k, val, graph):
  dict1 = nx.degree(graph)


def getstats(graph):
  mainstring = "Stats:\n"
  mainstring += "No of Nodes : "+str(len(graph))+"\n"
  mainstring += "No of Edges : "+str(graph.number_of_edges())+"\n"
  degree_list=[]
  for key,value in nx.degree(graph):
    degree_list.append(value) 
  try:
    avgDegree = sum(degree_list)/len(degree_list)
    avgPathDegree = 0
    avgClustering = 0
    edgeBetweeness = 0
    temp = {}
    if nx.is_connected(graph):
        avgPathDegree = nx.average_shortest_path_length(graph)
        avgClustering = nx.average_clustering(graph)
        temp = nx.edge_betweenness_centrality(graph)
    mainstring += "Avg Degree : {0:.4f} \n"
    mainstring += "Avg path len: {1:.4f} \n"
    mainstring += "Avg Clustering : {2:.4f} \n"
    mainstring += "Avg Betweeness : {3:.4f} \n"
    if len(temp) > 0:
        for key, value in temp:
            edgeBetweeness += value
        edgeBetweeness /= len(temp)
    return mainstring , avgDegree , avgPathDegree , avgClustering, edgeBetweeness
  except ZeroDivisionError:
    mainstring += "Avg Degree : - \n"
    mainstring += "Avg Path len: - \n"
    mainstring += "Avg Clustering: - \n"
    mainstring += "Betweeness Centraility : {3:.4f} \n"
    return mainstring , 0 , 0 , 0 , 0
  except Exception as e:
    print(e)
    return mainstring

def saveToFile(directory,graph):
   with open(directory+"/nodeList.txt","w") as nodeFile:
      for node in graph.nodes():
         nodeFile.write(str(node)+"\n")
   with open(directory+"/edgeList.txt","w") as edgeFile:
      for v1,v2 in graph.edges():
         edgeFile.write(str(v1)+" "+str(v2)+"\n")
   with open(directory+"/clustering.txt","w") as clusterFile:
        clusterFile.write(str(nx.clustering(graph)))
   with open(directory+"/betweenness.txt","w") as betweenFile:
        betweenFile.write(str(nx.edge_betweenness_centrality(graph)))
   with open(directory+"/degrees.txt","w") as degreeFile:
        degreeFile.write(str(nx.degree(graph)))

# print(nodes, edges)
# Create new threads

# thread1 = fileReaderThread(1, "nodeInputThread", nodeReader, "nodeList.txt")
# thread2 = fileReaderThread(2, "edgeInputThread", edgeReader, "edgeList.txt")

# Start new Threads
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()


# G.add_nodes_from(nodes)
# G.add_edges_from(edges)
# nx.draw(G)
# plt.savefig("plot.png")
# plt.show()
