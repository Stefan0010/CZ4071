#
# Undirected graph - wcc distribution. G(1965206, 5895612). Largest component has 1.000000 nodes (Fri Mar 03 02:04:35 2017)
#

set title "Undirected graph - wcc distribution. G(1965206, 5895612). Largest component has 1.000000 nodes"
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
set output 'wcc.ScaleFreeWcc.png'
plot 	"wcc.ScaleFreeWcc.tab" using 1:2 title "" with linespoints pt 6
