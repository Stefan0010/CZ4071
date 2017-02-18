#
# Random Graph Eigenvalue Distribution. G(10000, 14813). Largest eig val = 31.215448 (Sat Feb 18 15:49:53 2017)
#

set title "Random Graph Eigenvalue Distribution. G(10000, 14813). Largest eig val = 31.215448"
set key bottom right
set autoscale
set grid
set xlabel "Eigen value"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'eigDistr.RandomNetworkEigValDistr.png'
plot 	"eigDistr.RandomNetworkEigValDistr.tab" using 1:2 title "" with linespoints pt 6
