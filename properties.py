import snap
import os
import shutil

def loadGraph(fileDir):
	graph = snap.LoadEdgeList(snap.PUNGraph, fileDir, 0, 1)
	return graph

def saveGraph(graph):
	path = 'dot/'
	if os.path.exists(path):
		shutil.rmtree(path)

	os.mkdir(path)

	filePath = path + 'graph.dot'

	snap.SaveGViz(graph, filePath)
	return os.path.abspath(filePath)

def plotClustCf(graph):
	path = 'cf/'

	if os.path.exists(path):
		shutil.rmtree(path)

	os.mkdir(path)
	os.chdir(path)

	fileName = 'clust_coeff'
	snap.PlotClustCf(graph, fileName, "Clustering Coefficient")

	base = 'ccf.' + fileName
	ext = ['.plt' , '.tab', '.png']

	result = [ os.path.abspath(base + i) for i in ext ]
	os.chdir('..')
	return result

def plotSccDistr(graph):
	path = 'scc/'

	if os.path.exists(path):
		shutil.rmtree(path)

	os.mkdir(path)
	os.chdir(path)

	fileName = 'scc'
	snap.PlotSccDistr(graph, fileName, "Strongly Connected Component")

	base = 'scc.' + fileName
	ext = ['.plt' , '.tab', '.png']

	result = [ os.path.abspath(base + i) for i in ext ]
	os.chdir('..')
	return result

def plotWccDistr(graph):
	path = 'wcc/'

	if os.path.exists(path):
		shutil.rmtree(path)

	os.mkdir(path)
	os.chdir(path)

	fileName = 'wcc'
	snap.PlotSccDistr(graph, fileName, "Weakly Connected Component")

	base = 'wcc.' + fileName
	ext = ['.plt' , '.tab', '.png']

	result = [ os.path.abspath(base + i) for i in ext ]
	os.chdir('..')
	return result

def plotInDegDistr(graph):
	path = 'indeg/'

	if os.path.exists(path):
		shutil.rmtree(path)

	os.mkdir(path)
	os.chdir(path)

	fileName = 'in_deg_distr'
	snap.PlotInDegDistr(graph, fileName, "In Degree Distribution")

	base = 'inDeg.' + fileName
	ext = ['.plt' , '.tab', '.png']

	result = [ os.path.abspath(base + i) for i in ext ]
	os.chdir('..')
	return result

def plotOutDegDistr(graph):
	path = 'outdeg/'

	if os.path.exists(path):
		shutil.rmtree(path)

	os.mkdir(path)
	os.chdir(path)

	fileName = 'out_deg_distr'
	snap.PlotOutDegDistr(graph, fileName, "Out Degree Distribution")

	base = 'outDeg.' + fileName
	ext = ['.plt' , '.tab', '.png']

	result = [ os.path.abspath(base + i) for i in ext ]
	os.chdir('..')
	return result
