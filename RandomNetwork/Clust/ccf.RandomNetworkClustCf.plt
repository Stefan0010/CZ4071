#
# Undirected graph - clustering coefficient. G(10000, 10000). Average clustering: 0.0001  OpenTriads: 19739 (0.9999)  ClosedTriads: 1 (0.0001) (Sat Feb 18 14:43:55 2017)
#

set title "Undirected graph - clustering coefficient. G(10000, 10000). Average clustering: 0.0001  OpenTriads: 19739 (0.9999)  ClosedTriads: 1 (0.0001)"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Node degree"
set ylabel "Average clustering coefficient"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'ccf.RandomNetworkClustCf.png'
plot 	"ccf.RandomNetworkClustCf.tab" using 1:2 title "" with linespoints pt 6
