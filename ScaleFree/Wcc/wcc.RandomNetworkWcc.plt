#
# Undirected graph - wcc distribution. G(10000, 14813). Largest component has 0.900200 nodes (Sat Feb 18 15:49:53 2017)
#

set title "Undirected graph - wcc distribution. G(10000, 14813). Largest component has 0.900200 nodes"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Size of weakly connected component"
set ylabel "Number of components"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'wcc.RandomNetworkWcc.png'
plot 	"wcc.RandomNetworkWcc.tab" using 1:2 title "" with linespoints pt 6
