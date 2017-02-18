#
# Undirected graph - in-degree Distribution. G(10000, 10000). 3195 (0.3195) nodes with in-deg > avg deg (2.0), 503 (0.0503) with >2*avg.deg (Sat Feb 18 14:43:55 2017)
#

set title "Undirected graph - in-degree Distribution. G(10000, 10000). 3195 (0.3195) nodes with in-deg > avg deg (2.0), 503 (0.0503) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.RandomNetworkInDeg.png'
plot 	"inDeg.RandomNetworkInDeg.tab" using 1:2 title "" with linespoints pt 6
