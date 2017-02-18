#
# Undirected graph - hops. Hop plot. EffDiam: 16.6381, G(10000, 10000) (Sat Feb 18 14:43:54 2017)
#

set title "Undirected graph - hops. Hop plot. EffDiam: 16.6381, G(10000, 10000)"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of pairs of nodes"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'hop.RandomNetworkHops.png'
plot 	"hop.RandomNetworkHops.tab" using 1:2 title "" with linespoints pt 6
