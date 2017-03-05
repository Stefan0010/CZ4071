import snap
import os
import shutil
import matplotlib.pyplot as plt	
import numpy as np

plt.rcParams['figure.figsize'] = (16, 9)
MAX_XTICKS_NUM = 25

def Scc():
	return snap.PlotSccDistr(Graph, "ScaleFreeScc", "Undirected graph - scc distribution")

def Wcc():
	return snap.PlotWccDistr(Graph, "ScaleFreeWcc", "Undirected graph - wcc distribution")

def ShortPath():
	return snap.PlotShortPathDistr(Graph, "ScaleFreeShortestPath", "Undirected graph - shortest path")

def computeDegCorr(graph):
	knn = {}
	for u in graph.Nodes():
		ki = u.GetDeg()

		# Isolated nodes
		if ki == 0:
			continue

		ksum = 0.
		for i in range(ki):
			vid = u.GetNbrNId(i)
			ksum += graph.GetNI(vid).GetDeg()
		ksum = ksum / ki

		if ki not in knn:
			knn[ki] = []
		knn[ki].append(ksum)

	knn_arr = []
	for ki in knn:
		# Is this correct?
		knn_arr.append( (ki, sum(knn[ki]) / len(knn[ki])) )
	knn_ndarr = np.array(knn_arr, dtype=float)

	sorted_ks = np.argsort(knn_ndarr[:, 0])
	knn_ndarr = knn_ndarr[sorted_ks]
	return knn_ndarr

def plotDegCorr(graph):
	out_fname = os.path.join('temp', 'degcorrdistr.png')
	knn = computeDegCorr(graph)
	plt.clf()
	plt.figure(1)
	plt.plot(knn[:, 0], knn[:, 1], '-x')
	plt.subplots_adjust(left=0.1, bottom=0.075, right=1., top=1., wspace=0., hspace=0.)


	if knn[:, 0].max() > MAX_XTICKS_NUM:
		skip = int(knn[:, 0].max()) / MAX_XTICKS_NUM
		plt.xticks( np.arange(0, knn[:, 0].max() + 1 + skip, skip) )
	else:
		plt.xticks(np.arange(knn[:, 0].max() + 1))

	plt.ylim(knn[:, 1].min(), knn[:, 1].max())
	plt.xlabel('Degree', fontsize=16)
	plt.ylabel('Degree Correlation', fontsize=16)
	plt.yscale('log')
	plt.xscale('log')
	plt.grid(True)
	plt.savefig(out_fname, dpi=300, format='png')

	return os.path.abspath(out_fname)

def OutDeg(graph):
	outdir = 'temp/'

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
	plt.subplots_adjust(left=0.075, bottom=0.075, right=1., top=1., wspace=0., hspace=0.)
	plt.plot(tmp_arr[:, 0], tmp_arr[:, 1], '-x')
	plt.yscale('log')

	if tmp_arr[:, 0].max() > MAX_XTICKS_NUM:
		skip = int(tmp_arr[:, 0].max()) / MAX_XTICKS_NUM
		plt.xticks( np.arange(0, tmp_arr[:, 0].max() + 1 + skip, skip) )
	else:
		plt.xticks(np.arange(tmp_arr[:, 0].max() + 1))

	plt.xlim(0, tmp_arr[:, 0].max())
	plt.ylim(0, tmp_arr[:, 1].max())
	plt.xlabel('Out-degrees', fontsize=16)
	plt.ylabel('Number of nodes', fontsize=16)
	plt.grid(True)
	plt.savefig(out_fname, dpi=300, format='png')

def InDeg():
	return snap.PlotInDegDistr(Graph, "ScaleFreeInDeg", "Undirected graph - in-degree Distribution")

def Clust():
	return snap.PlotClustCf(Graph, "ScaleFreeClustCf", "Undirected graph - clustering coefficient")

def switcher(arg):
	switcher = {
		'Scc':Scc,
		'Wcc':Wcc,
		'DegCorr':plotDegCorr,
		'ShortPath':ShortPath,
		'OutDeg':OutDeg,
		'InDeg':InDeg,
		'Clust':Clust,

	}
	func = switcher.get(arg)
	return func()

def createFile(path,fileName,arg):
	print arg + 'starts'
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

def getDegCentr(graph):
	nid = snap.GetMxDegNId(graph)
	CDn = snap.GetDegreeCentr(graph, nid)
	n = graph.GetNodes()

	freeman_nom = 0.

	for NI in graph.Nodes():
		CDi = snap.GetDegreeCentr(graph, NI.GetId())
		freeman_nom += CDn - CDi

	return freeman_nom / (n - 2)

def getGamma(graph):
	kmin = float('inf')
	kmax = -float('inf')

	out_arr = snap.TIntPrV()
	snap.GetDegCnt(graph, out_arr)
	for item in out_arr:
		deg = item.GetVal1()
		num = item.GetVal2()

		kmin = max(1, min(kmin, deg))
		kmax = max(kmax, deg)

	return 1. + np.log(graph.GetNodes()) / (np.log(kmax) - np.log(kmin))

def getBasicProps(graph):
	# Assuming unweighted undirected graph
	return {
		'num_nodes': graph.GetNodes(),
		'num_edges': graph.GetEdges(),
		'avg_deg': 2. * graph.GetEdges() / graph.GetNodes(),
		'gamma': getGamma(graph),
		'deg_centr': getDegCentr(graph),
		'num_tris': snap.GetTriads(graph, -1),
		'global_cc': snap.GetClustCf(graph, -1),
	}

Graph = snap.GenRndGnm(snap.PUNGraph, 1965206,2766607, False)

prop = ['Scc','Wcc','InDeg','Clust']
for item in prop:
	createFile(item,item,item)

OutDeg(Graph)
plotDegCorr(Graph)

print getBasicProps(Graph)
