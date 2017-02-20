import os
import snap
import shutil
import numpy as np

import matplotlib.pyplot as plt

def loadGraph(fileDir):
	graph = snap.LoadEdgeList(snap.PUNGraph, fileDir, 0, 1)
	return graph

def saveGraph(graph):
	path = 'temp/'
	# if os.path.exists(path):
	# 	shutil.rmtree(path)

	# os.mkdir(path)

	filePath = path + 'graph.dot'

	snap.SaveGViz(graph, filePath)
	return os.path.abspath(filePath)

def plotClustCf(graph):
	path = 'temp/'

	# if os.path.exists(path):
	# 	shutil.rmtree(path)

	# os.mkdir(path)
	os.chdir(path)

	fileName = 'clust_coeff'

	snap.PlotClustCf(graph, fileName, "Clustering Coefficient")

	base = path + 'ccf.' + fileName

	# ext = ['.plt' , '.tab', '.png']
	# result = [ os.path.abspath(base + i) for i in ext ]

	os.chdir('..')

	# return result
	return os.path.abspath(base + '.png')

def plotSccDistr(graph):
	path = 'temp/'

	# if os.path.exists(path):
	# 	shutil.rmtree(path)

	# os.mkdir(path)
	os.chdir(path)

	fileName = 'scc'
	snap.PlotSccDistr(graph, fileName, "Strongly Connected Component")

	base = path + 'scc.' + fileName

	# ext = ['.plt' , '.tab', '.png']
	# result = [ os.path.abspath(base + i) for i in ext ]

	os.chdir('..')

	# return result
	return os.path.abspath(base + '.png')

def plotWccDistr(graph):
	path = 'temp/'

	# if os.path.exists(path):
	# 	shutil.rmtree(path)

	# os.mkdir(path)
	os.chdir(path)

	fileName = 'wcc'
	snap.PlotWccDistr(graph, fileName, "Weakly Connected Component")

	base = path + 'wcc.' + fileName

	# ext = ['.plt' , '.tab', '.png']
	# result = [ os.path.abspath(base + i) for i in ext ]

	os.chdir('..')

	# return result
	return os.path.abspath(base + '.png')

def plotInDegDistr(graph):
	# path = 'indeg/'

	# if os.path.exists(path):
	# 	shutil.rmtree(path)

	# os.mkdir(path)
	# os.chdir(path)

	# fileName = 'in_deg_distr'
	# snap.PlotInDegDistr(graph, fileName, "In Degree Distribution")

	# base = 'inDeg.' + fileName
	# ext = ['.plt' , '.tab', '.png']

	tmp_arr = []
	out_arr = snap.TIntPrV()
	snap.GetInDegCnt(graph, out_arr)
	for item in out_arr:
		cnt = item.GetVal2()
		deg = item.GetVal1()
		tmp_arr.append((deg, cnt))
	tmp_arr = np.array(tmp_arr)

	out_fname = os.path.join('temp', 'indegdistr.png')

	plt.clf()
	plt.figure(1)
	plt.subplots_adjust(left=0.1, bottom=0.1, right=1., top=1., wspace=0., hspace=0.)
	plt.plot(tmp_arr[:, 0], tmp_arr[:, 1], '-x')
	plt.yscale('log')
	plt.xlim(tmp_arr[:, 0].min(), tmp_arr[:, 0].max())
	plt.ylim(tmp_arr[:, 1].min(), tmp_arr[:, 1].max())
	plt.xlabel('In-degrees')
	plt.ylabel('Number of nodes')
	plt.savefig(out_fname, dpi=300, format='png')

	# os.chdir('..')
	# return [ os.path.abspath(base + i) for i in ext ]

	return os.path.abspath(out_fname)

def plotOutDegDistr(graph):
	outdir = 'temp/'

	# if os.path.exists(outdir):
	# 	shutil.rmtree(outdir)

	# os.mkdir(outdir)
	# os.chdir(outdir)

	# fileName = 'out_deg_distr'
	# snap.PlotOutDegDistr(graph, fileName, "Out Degree Distribution")

	# base = 'outDeg.' + fileName
	# ext = ['.plt' , '.tab', '.png']

	tmp_arr = []
	out_arr = snap.TIntPrV()
	snap.GetOutDegCnt(graph, out_arr)
	for item in out_arr:
		cnt = item.GetVal2()
		deg = item.GetVal1()
		tmp_arr.append((deg, cnt))
	tmp_arr = np.array(tmp_arr)

	out_fname = os.path.join('temp', 'outdegdistr.png')

	plt.clf()
	plt.figure(1)
	plt.subplots_adjust(left=0.1, bottom=0.1, right=1., top=1., wspace=0., hspace=0.)
	plt.plot(tmp_arr[:, 0], tmp_arr[:, 1], '-x')
	plt.yscale('log')
	plt.xlim(tmp_arr[:, 0].min(), tmp_arr[:, 0].max())
	plt.ylim(tmp_arr[:, 1].min(), tmp_arr[:, 1].max())
	plt.xlabel('Out-degrees')
	plt.ylabel('Number of nodes')
	plt.savefig(out_fname, dpi=300, format='png')

	# os.chdir('..')
	# return [ os.path.abspath(base + i) for i in ext ]

	return os.path.abspath(out_fname)

if __name__ == '__main__':
	g = loadGraph('roadNet-CA.txt')
	plotInDegDistr(g)
	plotOutDegDistr(g)
