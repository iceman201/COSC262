COSC262
=======
In this assignment II, you will implement methods for computing the convex hulls of twodimensional
points, and evaluate their performance using point data sets. For
comparative analysis and testing of the methods, three programs are required to be
developed as outlined below

i. giftwrap.py: This program should contain the implementation of the
“Simplified Gift-Wrap” algorithm based on the method given on Slide [1.1]-23

ii. grahamscan.py: This program should contain a stack-based implementation
of the Graham-Scan algorithm as outlined on Slide [1.1]-28.

iii. amethod.py: This could be any other non-naïve method for computing the
convex hull of a set of points (eg., insertion hull, quick hull), or a suggested
improvement of the methods in (i) or (ii).

Each of the three programs must be able to read up to 12000 points from an input file,
and output a single line containing the indices of the convex hull vertices. The programs
should be able to read the input file name specified as the command line argument, eg.,

python giftwrap.py A_500.dat

For this, you will need to use the sys module (import sys) in the program as
shown below. The file name will then be available in sys.argv[1]

Algorithm&amp;Computer Graphic 
