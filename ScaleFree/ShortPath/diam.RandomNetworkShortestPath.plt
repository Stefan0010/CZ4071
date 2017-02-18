#
# Undirected graph - shortest path. G(10000, 14813). Diam: avg:4.72  eff:5.94  max:17 (Sat Feb 18 15:50:36 2017)
#

set title "Undirected graph - shortest path. G(10000, 14813). Diam: avg:4.72  eff:5.94  max:17"
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
