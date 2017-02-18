#
# Undirected graph - in-degree Distribution. G(10000, 14813). 2561 (0.2561) nodes with in-deg > avg deg (3.0), 812 (0.0812) with >2*avg.deg (Sat Feb 18 15:50:43 2017)
#

set title "Undirected graph - in-degree Distribution. G(10000, 14813). 2561 (0.2561) nodes with in-deg > avg deg (3.0), 812 (0.0812) with >2*avg.deg"
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
