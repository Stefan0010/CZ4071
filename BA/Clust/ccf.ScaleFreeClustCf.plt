#
# Undirected graph - clustering coefficient. G(1965206, 5895612). Average clustering: 0.0001  OpenTriads: 168012934 (1.0000)  ClosedTriads: 1926 (0.0000) (Fri Mar 03 02:04:47 2017)
#

set title "Undirected graph - clustering coefficient. G(1965206, 5895612). Average clustering: 0.0001  OpenTriads: 168012934 (1.0000)  ClosedTriads: 1926 (0.0000)"
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
set output 'ccf.ScaleFreeClustCf.png'
plot 	"ccf.ScaleFreeClustCf.tab" using 1:2 title "" with linespoints pt 6
