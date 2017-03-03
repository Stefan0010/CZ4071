#
# Undirected graph - in-degree Distribution. G(1965206, 3930409). 588955 (0.2997) nodes with in-deg > avg deg (4.0), 163588 (0.0832) with >2*avg.deg (Fri Mar 03 16:13:38 2017)
#

set title "Undirected graph - in-degree Distribution. G(1965206, 3930409). 588955 (0.2997) nodes with in-deg > avg deg (4.0), 163588 (0.0832) with >2*avg.deg"
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
set output 'inDeg.ScaleFreeInDeg.png'
plot 	"inDeg.ScaleFreeInDeg.tab" using 1:2 title "" with linespoints pt 6
