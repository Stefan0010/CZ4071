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

# Plot the ranks of the first 10 eigenvalues
# NOTE: Random graphs are likely to thwart the calculation of eigenvalues
# def EigRank():
# 	return snap.PlotEigValRank(Graph, 10, "ScaleFreeEigValRank", "Random Graph Eigenvalue Rank")

# def EigDistr():
# 	return snap.PlotEigValDistr(Graph, 10, "ScaleFreeEigValDistr", "Random Graph Eigenvalue Distribution")

def ShortPath():
	return snap.PlotShortPathDistr(Graph, "ScaleFreeShortestPath", "Undirected graph - shortest path")

# def ShortPath():
# 	if Graph.GetNodes() * Graph.GetEdges() > 100000000:
# 		return

# 	filepath = os.path.join('temp', 'temp_graph.txt')
# 	snap.SaveEdgeList(Graph, filepath)
# 	p_args = [os.path.join('.', 'spdistr'), filepath]
# 	p = Popen(p_args, stdout=PIPE)

# 	temp_list = []
# 	while True:
# 		line = p.stdout.readline()
# 		if line == '':
# 			break

# 		line_splits = line.split(',')

# 		dst = int(line_splits[0])
# 		num = int(line_splits[1])
# 		temp_list.append((dst, num))

# 	spdistr_arr = np.array(temp_list, dtype=float)
# 	spdistr_arr[:, 1] /= 2.

# 	plt.clf()
# 	plt.figure(1)
# 	plt.plot(spdistr_arr[:, 0], spdistr_arr[:, 1], '-x')
# 	plt.xlim([0, spdistr_arr[:, 0].max()])
# 	plt.ylim([0, spdistr_arr[:, 1].max()])
# 	plt.xticks( np.arange(spdistr_arr[:, 0].max()+1) )
# 	plt.xlabel('Shortest path length', fontsize=16)
# 	plt.ylabel('Number of nodes', fontsize=16)
# 	plt.subplots_adjust(left=0.075, bottom=0.075, right=1., top=1., wspace=0., hspace=0.)
# 	plt.grid(True)
# 	out_fname = os.path.join('temp', 'spdistr.png')
# 	plt.savefig(out_fname, dpi=300, format='png')

# 	return os.path.abspath(out_fname), spdistr_arr[-1, 0]


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

def DegCorr(graph):
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
# def Hops():
# 	return snap.PlotHops(Graph, "ScaleFreeHops", "Undirected graph - hops", False,1024)

def OutDeg(graph):
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

def InDeg():
	return snap.PlotInDegDistr(Graph, "ScaleFreeInDeg", "Undirected graph - in-degree Distribution")

def Clust():
	return snap.PlotClustCf(Graph, "ScaleFreeClustCf", "Undirected graph - clustering coefficient")

def switcher(arg):
	switcher = {
		'Scc':Scc,
		'Wcc':Wcc,
		'DegCorr':DegCorr,
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

Graph = snap.GenRndPowerLaw (1965206, 2.5)

# prop = ['Scc','Wcc','InDeg','Clust']
prop = ['ShortPath']
for item in prop:
	createFile(item,item,item)
# 'ShortPath',
# OutDeg(Graph)
# DegCorr(Graph)

# print getBasicProps(Graph)

# X =[]

# for NI in Graph.Nodes():
#     DegCentr = snap.GetDegreeCentr(Graph, NI.GetId())
#     X.append(DegCentr)

# Y = np.arange(10000)

# fig,gr = plt.subplots()

# gr.fill(Y,X,'r')
# plt.show()


