# HW 3

Algorithm:

Every bowling league may define the way handicap is calculated with their own methodology. However, most typical leagues use a formula such as the following:

       handicap = (200 - average) * 80%
where the bowler's average (a floating-point number) is truncated to the next lower integer, and the handicap is also truncated to the next lower integer.

For example: if a bowler in the above league had a 147.8 average, you would calculate her handicap as:

       average = 147 (147.8 truncated)
       handicap = (200 - average) * 80%
                = (200 - 147) * 80%
                = 53 * 80% = 42.4
which is then truncated to 42.

Assignment:

Write a complete Python program that calculates a bowler's average and handicap after three games. Prompt the user to enter three bowling games (integers between zero and 300 inclusive) one at a time, and calculate the bowler's average and handicap. Print out the average and handicap, truncated to integers.