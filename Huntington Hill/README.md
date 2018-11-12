# Learning-Python---Huntington-Hill-Method
An exercise from Python class

The United States counts its citizens every ten years, and the result of that census is used to allocate the 435 congressional seats in the House of Representatives to the 50 states. Since 1940, that allocation has been done using a method devised by Edward Vermilye Huntington and Joseph Adna Hill.

The Huntington-Hill method begins by assigning one representative to each state. Then each of the remaining representatives is assigned to a state in a succession of rounds by computing

g(n,p)=p/√n(n+1)

for each state, where n is the current number of representatives (initially 1) and p is the population of the state. This way, the value g(n,p) represents the state's population divided by the geometric mean of the current number of representatives and the number of representatives that the state would have if it was assigned the next representative. The geometric mean g(n,p) is calculated for each state at each round and the next representative is assigned to the state with the highest geometric mean g(n,p).

For instance, once a state has been assigned one representative, the geometric mean g(n,p) for each state is its population divided the square root of 2. Since California has the biggest population, it gets the 51st representative. Then its geometric mean g(n,p) is recalculated as its population divided by the square root of 2×3=6, and in the second round the 52nd representative is assigned to Texas, which has the second-highest population, since it now has the largest geometric mean g(n,p). This continues for 435−50=385 rounds until all the representatives have been assigned.

Assignment

In this assignment we will work with comma-separated values files (CSV-files) that contain the results of one or more censuses. The first column contains the names of the regions (e.g. the states of the United States) whose population counts are reported. Each remaining column contains the population count per region for the census in the year indicated in the column header. As an example, here are the first few lines of such a CSV-file:
