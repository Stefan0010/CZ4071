#
# Undirected graph - shortest path. G(10000, 10000). Diam: avg:12.55  eff:15.59  max:33 (Sat Feb 18 14:43:47 2017)
#

set title "Undirected graph - shortest path. G(10000, 10000). Diam: avg:12.55  eff:15.59  max:33"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'diam.RandomNetworkShortestPath.png'
plot 	"diam.RandomNetworkShortestPath.tab" using 1:2 title "" with linespoints pt 6
