import snap
import os
import shutil

def Scc():
	return snap.PlotSccDistr(Graph, "RandomNetworkScc", "Undirected graph - scc distribution")

def Wcc():
	return snap.PlotWccDistr(Graph, "RandomNetworkWcc", "Undirected graph - wcc distribution")

def EigRank():
	return snap.PlotEigValRank(Graph, 10, "RandomNetworkEigValRank", "Random Graph Eigenvalue Rank")

def EigDistr():
	return snap.PlotEigValDistr(Graph, 10, "RandomNetworkEigValDistr", "Random Graph Eigenvalue Distribution")

def ShortPath():
	return snap.PlotShortPathDistr(Graph, "RandomNetworkShortestPath", "Undirected graph - shortest path")

def Hops():
	return snap.PlotHops(Graph, "RandomNetworkHops", "Undirected graph - hops", False,1024)

def OutDeg():
	return snap.PlotOutDegDistr(Graph, "RandomNetworkOutDeg", "Undirected graph - out-degree Distribution")

def InDeg():
	return snap.PlotInDegDistr(Graph, "RandomNetworkInDeg", "Undirected graph - in-degree Distribution")

def Clust():
	return snap.PlotClustCf(Graph, "RandomNetworkClustCf", "Undirected graph - clustering coefficient")

def switcher(arg):
	switcher = {
		'Scc':Scc,
		'Wcc':Wcc,
		'EigRank':EigRank,
		'EigDistr':EigDistr,
		'ShortPath':ShortPath,
		'Hops':Hops,
		'OutDeg':OutDeg,
		'InDeg':InDeg,
		'Clust':Clust,

	}
	func = switcher.get(arg)
	return func()

def createFile(path,fileName,arg):

	path =  path + '/'
	if os.path.exists(path):
		shutil.rmtree(path)

	os.mkdir(path)
	os.chdir(path)

	switcher(arg)

	base = path+'.' + fileName
	ext = ['.plt' , '.tab', '.png']

	os.chdir('..')
	return [ os.path.abspath(base + i) for i in ext ]

Graph = snap.GenRndPowerLaw (10000, 2.5)

prop = ['Scc','Wcc','EigRank','EigDistr','ShortPath','Hops','OutDeg','InDeg','Clust']

for item in prop:
	createFile(item,item,item)
# createFile('Scc','Scc','Scc')
# createFile('Wcc','Wcc','Wcc')
# createFile('EigRank','EigRank','EigRank')
# createFile('EigDistr','EigDistr','EigDistr')
# createFile('ShortPath','ShortPath','ShortPath')
# createFile('Hops','Hops','Hops')
# createFile('OutDeg','OutDeg','OutDeg')
# createFile('InDeg','InDeg','InDeg')
# createFile('Clust','Clust','Clust')


# Plot the ranks of the first 10 eigenvalues
# NOTE: Random graphs are likely to thwart the calculation of eigenvalues










