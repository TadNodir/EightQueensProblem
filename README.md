## 8 Queens Problem

This repository contains solutions for the 8 Queens problem implemented in different approaches.

### Class for Encoding the 8 Queens Problem

The `EightQueens` class provides an implementation for encoding the 8 Queens problem. It includes the following members:

- **Initial state**: The initial arrangement of the queens on the chessboard. The user can choose a custom initial state or use the default one.
- **Actions**: The possible moves that can be performed on the current state, following the rules of the problem.
- **Transition model**: The function that generates a new state based on the current state and a chosen action.
- **Heuristic**: The heuristic function used to estimate the "goodness" of a state.
- **Visualization**: ASCII visualization of the chessboard, displaying the current state, heuristic values, and cost function.

### 8 Queens Problem Solver using Genetic Algorithms

The `genetic_algorithm` method solves the 8 Queens problem using a genetic algorithm approach. It follows the method introduced in the lecture, including the fitness function. The algorithm starts with a fixed random initial population and outputs the best individual in each iteration. It terminates after 100 iterations.

### Random Number Generation

Random numbers in the interval [0, 1) are generated using the `random` function. This method provides a simple and widely used approach for generating random numbers. However, if there are specific requirements or better alternatives for generating random numbers, it's recommended to explore other libraries or methods suitable for your use case.

### Solve the 8 Queens Problem by Backtracking Search

The `EightQueensBacktrackingProblem` class solves the 8 Queens problem using a backtracking search approach. It prints all possible solutions to the screen.

Please refer to the individual source files for more detailed documentation and implementation details.

Feel free to explore the code, modify it according to your needs, and contribute to this repository. Happy problem-solving!
