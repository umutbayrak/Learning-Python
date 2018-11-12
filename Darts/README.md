# Learning-Python---Darts
An exercise from Python class

Scoring
The dartboard is divided in rings and sections. The numbers at the rim indicate the amount of points you receive for throwing a dart in that particular section. In this assignment, the sectors are numbered clockwise from 1 starting at the top section. The sections are further subdivided in a number of smaller partitions.

in the middle is the double bull or bull's eye (red), 50 points

around the double bull is the single bull (green), 25 points

around that a wide ring, the bed (black and white), for which the amount of points that is indicated on the rim of the board is granted

around that a smaller ring, the triple (or treble) ring (red and green); this yields a triple score of the bed

around that is another bed

around that is the double ring (red en green) yields a double score of the bed

If you throw a dart in the outer black rim (where the numbers are) or next to the board, you don't get any points. A bouncer — a dart that bounces back from the board — doesn't give a score neither. You also won't receive any points if one of your darts falls from the board before you were able to take your darts out (please note, officially this isn't called a bouncer). If a player throws in one of his previously thrown darts (a Robin Hood), the last dart doesn't receive a score.

Assignment
We consider a Cartesian coordinate scale with its origin in the center of the bull's eye of a dartboard. A player throws a dart to the board that lands on coordinates (x,y), with coordinates expressed in millimeters. Determine the score that is obtained by this dart. In order to do so, it is best to first convert the Cartesian coordinates (x,y) of the position where the dart has landed into polar coordinates (r,θ), and then to determine the score of the corresponding sector based on the angle θ.


Input
The input contains the numbers x,y∈R, each on a separate line. These numbers represent the position (x,y) of the point P in the Cartesian coordinate scale with its origin in the center of the bull's eye of a dartboard. The units of the coordinate scale are expressed in millimeters.

Output
The output contains the score that is awarded to a dart thrown at position P on the dartboard.
