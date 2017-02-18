#
# Random Graph Eigenvalue Rank. G(10000, 14813). Largest eig val = 31.215448 (Sat Feb 18 15:49:53 2017)
#

set title "Random Graph Eigenvalue Rank. G(10000, 14813). Largest eig val = 31.215448"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Rank"
set ylabel "Eigen value"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'eigVal.RandomNetworkEigValRank.png'
plot 	"eigVal.RandomNetworkEigValRank.tab" using 1:2 title "" with linespoints pt 6
