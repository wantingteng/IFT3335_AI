# Purpose of the Project

1. Learn how to use heuristics for state-space research
2. Compare the performance of different algorithms
3. Develop heuristics for this game

# Submission Date:

The deadline for submission is <span style="color:red;">February 16, before 23:59</span>.

# Evaluation:

This project counts for <span style="color:red;">15%</span> of the total grade.


# The Sudoku Game

This game from Japan is represented in a 9*9 grid, divided into 9 squares of 9 boxes. Some boxes already contain a number from 1 to 9. The goal is to fill the empty boxes so that each square, each row, and each column contain the numbers 1-9 without repetition. In other words, we should not find 2 identical numbers in the same square, the same row, or the same column.

# Work to be Done:

- [ ] (10%) Run Norvig's program (in Python) on a set of Sudoku cases (see the 100 test configurations on Studium).
    
- [ ] (20%) Implement at least one other heuristic, in addition to Norvig's 3rd criterion. You can choose which heuristics to use. You can look for heuristics to implement in web articles or on Studium. These heuristics should improve the performance of the implemented algorithms (you must confirm this in your tests).
      
- [ ] (20%) Implement the Hill-Climbing algorithm for this problem. Starting from the initial configuration, fill each 3x3 square with randomly possible digits, but check the constraints for the same square. This will cause conflicts on the rows and columns. Then, use Hill-Climbing to try to improve the configuration as much as possible, by swapping two of the filled digits in a square.
      
- [ ] (20%) Use simulated annealing. Hill-Climbing can get stuck on a local optimum without being able to arrange all the digits correctly. This algorithm can be improved by using simulated annealing. You are asked to implement a simplified version of the algorithm described by Lewis. You use the same strategy to decrease the temperature: ti+1 = α · ti with α=0.99. Normally, the use of simulated annealing should improve the success rate on Hill-climbing.
      
- [ ] (20%) Compare the algorithms by running them on 100 starting configurations (see the list of configurations on Studium). Compare the percentage of successful games (for which the algorithm finds the solution), as well as the time used. Make your personal analysis to see if what you observe corresponds well to the analyses made in the course. Your comparisons and analyses must be described in a short 2-3 page report.

# To Submit:

- [ ] A 2-3 page report containing:
    1. A brief description of what has been accomplished in this project
    2. An explanation of the heuristic that has been implemented for question 3
    3. A comparison of the performance of different methods
    4. Include in the report the program corresponding to each algorithm that has been implemented. Describe in the report how these programs should operate.
- [ ] The programs that have been implemented (integrated into Norvig's program).

# Web Resources:

- 1000 starting configurations on the Sudoku Garden site (from where the 100 test configurations are taken). Each configuration occupies a line, composed of 81 digits, corresponding to the 81 squares, with the 9 lines concatenated. 0 means the square is empty (to be filled by your program).
- practice online : [http://www.websudoku.com](http://www.websudoku.com/)
