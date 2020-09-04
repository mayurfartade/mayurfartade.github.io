Problem Statement
Billy loves to play video games but could not get time for those earlier, now since he has a lot of free time during the lockdown because of the current COVID pandemic, he tries to play a new game “Reach The End”. But in the first stage of the game itself, Billy got stuck. So he needs your help.

In the game, initially, there are N buildings (numbered from 1 to N) placed along a line, the heights of the buildings are in increasing order such that the first building is the shortest and last building is the tallest. The main character of the game, the ‘Prince’ stands on top of the first building and he has to reach the last building, he has to do so by jumping from one building to another and he must jump on each building at least once. The amount of ‘Health’ which he needs to reach the end is the maximum difference between any two consecutive jumps. Now since he is a Prince, he is given a superpower such that in each usage of this superpower, he can grow a building of any integer height between any two consecutive buildings and he must use this superpower exactly K times. As you might have heard, with great powers, come some limitations and that is the case here too. The player of the game (Billy) needs to select a starting health ‘H’ for the Prince which should be minimum possible such that it is possible for the Prince to reach the end. At any point in time, ‘H’ should never become less than 0 or Prince will die there. (For eg: He is alive at H=1 or H=0 but dies at H=-1 ). Billy, being innocent tries to guess the value of ‘H’. Let his guess be ‘x’.

You need to tell how close Billy was to the actual ‘H’.

NOTE: The health replenishes to the initial health ‘H’ after jumping to the top of the building each time as the Prince can rest for some time on the building.

For eg: If H=5 and there are buildings [1, 3, 8]. Then initially he is on the building of height 1, he makes a jump to the second building of height 3, H becomes ‘3’ because he made a jump of 2 (3-1=2) but the Prince can rest on the second building so that H again becomes 5, now he makes a jump from the second building to the third building and H becomes 0 (8-3 = 5). He somehow reached the last building, hence it is possible in this case for the Prince to reach the end

If H=1 and buildings=[1, 3, 8], then on making the first jump his health becomes -1, hence not possible in this case.

Input Format
The first line of the input contains N, K and x. N denotes the number of buildings, K denotes the no. of times the superpower must be used and x denotes the Billy’s guess.

The second line contains N space separated integers buildings[i] denoting the heights of the i-th building.

Constraints:

2 <= N <= 10^5

0 <= K <= 10^5

1 <= building[i] <= 10^9

Initially, building[1] < building[2] <…… < building[N]

Output Format
Print a single integer, the minimum absolute value of the difference between ‘H’ and ‘x’ after optimally using the superpower exactly K times



Sample Testcase #0
Testcase Input
3 6 3
40 50 60
Testcase Output
0
Explanation
N=3 and K=6, buildings=[40, 50, 60]. The prince needs to use his superpower 6 times, he grows the 3 buildings of heights 43, 46, 49 between buildings of heights 40 and 50,

and can grow 3 buildings of height 53, 56, 59 between buildings of heights 50 and 60

So after this, buildings=[40, 43, 46, 49, 50, 53, 56, 59, 60]. If Billy selects H=3 initially, then the Prince can reach the end without dying. Now since H=3 and his guess x=3, then the difference between them is 0

Sample Testcase #1
Testcase Input
3 1 25
1 52 150
Testcase Output
26
Explanation
N=3 and K=1, buildings=[1, 52, 150]. The Prince needs to use his superpower 1 time, he can grow a building of height 100 between second and third building. So buildings=[1, 52, 100, 150], here H=51.
