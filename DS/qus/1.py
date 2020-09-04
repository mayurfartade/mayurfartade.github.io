With lockdown in effect, the youth of this country have started playing a lot of video games.

There are n teenagers, each of them is playing a unique game. At the end of any day, the i-th teenager will give his game to the ai-th teenager (in case of i=ai the teenager will give his game to himself). It is guaranteed that all values of ai are distinct integers from 1 to n (i.e. a is a permutation). The sequence of a doesn't change from day to day, it is fixed.

For example, if n=6 and a=[4,6,1,3,5,2] then at the end of the first day the game of the 1-st teenager will belong to the 4-th teenager, the 2-nd teenager will belong to the 6-th teenager and so on. At the end of the second day the game of the 1-st teenager will belong to the 3-th teenager, the 2-nd teenager will belong to the 2-th teenager and so on.

Your task is to determine the number of the day the game of the i-th teenager is returned back to him for the first time for every i from 1 to n.

Consider the following example: a=[5,1,2,4,3]. The book of the 1-st teenager will be passed to the following teenagers:

after the 1-st day it will belong to the 5-th teenager,
after the 2-nd day it will belong to the 3-rd teenager,
after the 3-rd day it will belong to the 2-nd teenager,
after the 4-th day it will belong to the 1-st teenager.
So after the fourth day, the game of the first teenager will return to its owner. The book of the fourth teenager will return to him for the first time after exactly one day.

Input Format
The first line of the input contains one integer t (1≤t≤1000) — the number of test cases. Then t test cases follow.

The first line of the query contains one integer n (1≤n≤2 x 105) — the number of teenagers. The second line of the query contains n integers a1,a2,…,an (1≤ai≤n, all ai are distinct, i.e. a is a permutation), where ai is the teenager which will get the book of the i-th kid.

It is guaranteed that sum of n over all queries does not exceed 2 x 105.

 

Output Format
For each query, print the answer on it: n integers q1,q2,…,qn, where qi is the number of the day the game of the i-th teenager is returned back to him for the first time in the test case.



Sample Testcase #0
Testcase Input
6
5
1 2 3 4 5
3
2 3 1
6
4 6 2 1 5 3
1
1
4
3 4 1 2
5
5 1 2 4 3
Testcase Output
1 1 1 1 1 
3 3 3 
2 3 3 2 1 3 
1 
2 2 2 2 
4 4 4 1 4 

