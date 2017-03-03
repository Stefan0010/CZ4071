import os
import snap
import shutil
import numpy as np

import matplotlib.pyplot as plt
from subprocess import Popen, PIPE

import scipy.stats

plt.rcParams['figure.figsize'] = (16, 9)
MAX_XTICKS_NUM = 25

def loadGraph(fileDir):
	if not os.path.isfile(fileDir):
		return None

	try:
		graph = snap.LoadEdgeList(snap.PUNGraph, fileDir, 0, 1)
	except Exception as e:
		graph = None

	return graph

def genScaleFree(N=5000, gamma=2.5):
	return snap.GenRndPowerLaw(N, gamma)

def genRandomGraph(N=5000, prob=0.002):
	return snap.GenRndGnm(snap.PUNGraph, N, int(prob * N * (N - 1) / 2), False)

def genScaleFreeBA(N=5000, k=2):
	return snap.GenPrefAttach(N, k)

def saveGraph(graph):
	path = 'temp/'
	# if os.path.exists(path):
	# 	shutil.rmtree(path)

	# os.mkdir(path)

	filePath = path + 'graph.dot'

	snap.SaveGViz(graph, filePath)
	return os.path.abspath(filePath)

def plotGraph(graph):
	if graph.GetNodes() + graph.GetEdges() > 200000:
		return None

	filename = saveGraph(graph)
	outfname = 'temp/graph.png'
	p_args = ['sfdp', '-Tpng', '-Gsize="10,10!"', '-Gdpi=72',
		'-Npenwidth=0.2', '-Nwidth=0.01', '-Nheight=0.01',
		'-Epenwidth=0.1', '-Nshape=ellipse', '-Nlabel=',
		'-Gsplines=false', '-Goverlap=false', filename, '-o' + outfname]

	print ' '.join(p_args)
	p = Popen(p_args)
	retcode = p.wait()

	return os.path.abspath(outfname)

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
	plt.subplots_adjust(left=0.075, bottom=0.075, right=1., top=1., wspace=0., hspace=0.)


	if knn[:, 0].max() > MAX_XTICKS_NUM:
		skip = int(knn[:, 0].max()) / MAX_XTICKS_NUM
		plt.xticks( np.arange(0, knn[:, 0].max() + 1 + skip, skip) )
	else:
		plt.xticks(np.arange(knn[:, 0].max() + 1))

	plt.xlim(0, knn[:, 0].max())
	plt.ylim(knn[:, 1].min(), knn[:, 1].max())
	plt.xlabel('Degree', fontsize=16)
	plt.ylabel('k_nn', fontsize=16)
	plt.yscale('log')
	plt.grid(True)
	plt.savefig(out_fname, dpi=300, format='png')
	# plt.show()

	return os.path.abspath(out_fname)

def plotSPDistr(graph):
	if graph.GetNodes() * graph.GetEdges() > 100000000:
		return

	filepath = os.path.join('temp', 'temp_graph.txt')
	snap.SaveEdgeList(graph, filepath)
	p_args = [os.path.join('.', 'spdistr'), filepath]
	p = Popen(p_args, stdout=PIPE)

	temp_list = []
	while True:
		line = p.stdout.readline()
		if line == '':
			break

		line_splits = line.split(',')

		dst = int(line_splits[0])
		num = int(line_splits[1])
		temp_list.append((dst, num))

	spdistr_arr = np.array(temp_list, dtype=float)
	spdistr_arr[:, 1] /= 2.

	plt.clf()
	plt.figure(1)
	plt.plot(spdistr_arr[:, 0], spdistr_arr[:, 1], '-x')
	plt.xlim([0, spdistr_arr[:, 0].max()])
	plt.ylim([0, spdistr_arr[:, 1].max()])
	plt.xticks( np.arange(spdistr_arr[:, 0].max()+1) )
	plt.xlabel('Shortest path length', fontsize=16)
	plt.ylabel('Number of nodes', fontsize=16)
	plt.subplots_adjust(left=0.075, bottom=0.075, right=1., top=1., wspace=0., hspace=0.)
	plt.grid(True)
	out_fname = os.path.join('temp', 'spdistr.png')
	plt.savefig(out_fname, dpi=300, format='png')

	return os.path.abspath(out_fname), spdistr_arr[-1, 0]

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
	plt.xlabel('In-degrees', fontsize=16)
	plt.ylabel('Number of nodes', fontsize=16)
	plt.grid(True)
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

	# os.chdir('..')
	# return [ os.path.abspath(base + i) for i in ext ]

	return os.path.abspath(out_fname)

def getDegCentr(graph):
	# CD(n)
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

		# DON'T LET kmin = 0
		# BECAUSE log(0) = INF
		kmin = max(1, min(kmin, deg))
		kmax = max(kmax, deg)

	# kmax = kmin * N ^ (1 / (gamma - 1))
	# kmax / kmin = N ^ (1 / (gamma - 1))
	# log(kmax) - log(kmin) = log(N) / (gamma - 1)
	# (gamma - 1) / log(N) = 1 / (log(kmax) - log(kmin))
	# gamma = 1 + log(N) / (log(kmax) - log(kmin))
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

def numOfTriangles(graph):
 	TriadCntV = snap.TIntPrV()
 	snap.GetTriadParticip(graph,TriadCntV)
 	result = 0
 	for pair in TriadCntV:
 		result += pair.Val1()
 	return result

if __name__ == '__main__':
	# g = loadGraph('roadNet-CA.txt')
	g = loadGraph('dumbell.txt')
	# g = genScaleFree(N=5000, gamma=2.1111)
	# g = genRandomGraph(N=5000, prob=0.0005)
	# print snap.GetTriads(g, -1)
