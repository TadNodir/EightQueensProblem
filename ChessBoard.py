import random


class EightQueens:
    def __init__(self, init_state=None, transition_model=None):
        self.board = [['-'] * 8 for _ in range(8)]
        if init_state:
            self.state = init_state
        else:
            self.state = [(i, 0) for i in range(8)]

        for col, row in self.state:
            self.board[col][row] = 'Q'

        if transition_model and len(transition_model) == 2:
            current_pos = transition_model[0]
            aiming_pos = transition_model[1]
            self.move_queen(current_pos, aiming_pos)

    def show_board(self):
        board = self.board.copy()
        for row in board:
            print(' '.join(row))

    def move_queen(self, cur_position, new_position):
        a, b = cur_position
        c, d = new_position
        if cur_position not in self.state:
            return "queen not found"

        self.board[a][b] = '-'
        self.board[c][d] = 'Q'
        self.set_state(a, b, new_position)

    def heuristic(self, state_p=None):
        collisions = 0
        state = self.state.copy()
        if state_p:
            state = state_p
        for i, (q1_row, q1_col) in enumerate(state):
            for j, (q2_row, q2_col) in enumerate(state):
                if i < j:
                    if q1_col == q2_col or q1_row == q2_row or abs(q1_col - q2_col) == abs(q1_row - q2_row):
                        collisions += 1
        return collisions

    def cost(self):
        return self.heuristic()

    def set_state(self, row2, col2, new_pos):
        for i, (row1, col1) in enumerate(self.state):
            if row1 == row2 and col1 == col2:
                self.state[i] = new_pos

    def fitness_func(self, state):
        fitness = 28 - self.heuristic(state)
        return fitness

    def reproduce(self, x, y):
        c = random.randint(1, 6)
        str1 = x[:c] + y[c:]
        str2 = y[:c] + x[c:]
        return str1, str2

    def mutate(self, individual):
        mutated = state_toTuple(individual)
        tuple_index = random.choice(range(8))
        old_row, old_col = mutated[tuple_index]
        new_col = random.choice([i for i in range(8) if i != old_col])
        new_tuple = old_row, new_col
        mutated[tuple_index] = new_tuple
        mutation_str = state_toString(mutated)
        return mutation_str

    def find_best_offspring(self, population):
        max_fit = 0
        best_child = ''
        for individual in population:
            state = state_toTuple(individual)
            fitness = self.fitness_func(state)
            if fitness > max_fit:
                max_fit = fitness
                best_child = state
        return max_fit, best_child

    def genetic_algorithm(self, iterations):
        fitness_res = 0
        iters = 0
        while fitness_res != 28 or iters == 100:
            population = random_population(iterations)
            fitnesses = [self.fitness_func(state_toTuple(state)) for state in population]
            total_fitnesses = sum(fitnesses)
            probability = [fitness / total_fitnesses for fitness in fitnesses]
            new_population = set()
            for _ in population:
                x = random.choices(population, probability)[0]
                y = random.choices(population, probability)[0]
                child1, child2 = self.reproduce(x, y)
                mutated1 = self.mutate(child1)
                mutated2 = self.mutate(child2)
                new_population.add(mutated1)
                new_population.add(mutated2)
            population = new_population
            best_offspring = self.find_best_offspring(population)
            fit, state_b = best_offspring
            fitness_res = fit
            iters += 1
            self.__init__(state_b)
            self.show_board()
            print("Fitness: " + str(fit))
            print("Iterations: " + str(iters))
            print()


class EightQueensBacktrackingProblem:
    def __init__(self):
        self.states = []

    # Run the function to find solutions by calling backtracking method
    def runner(self):
        board = [[0] * 8 for _ in range(8)]
        self.backtrack(board, 0)

    # Find the solution for the 8 queens problem with backtracking
    # and append the solution to the list of solutions
    def backtrack(self, board, col):
        if col >= 8:
            self.states.append([row[:] for row in board])
            return

        for row in range(8):
            if self.check_attacks(board, row, col):
                board[row][col] = 1
                self.backtrack(board, col + 1)
                board[row][col] = 0

    # Check if the position is valid by testing collisions horizontally, upper diagonally
    # and lower diagonally
    def check_attacks(self, board, row, col):
        # Check if the current position is under attack
        # Check horizontally
        for c in range(col):
            if board[row][c] == 1:
                return False

        # Check upper diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == 1:
                return False
            r -= 1
            c -= 1

        # Check lower diagonal
        r, c = row, col
        while r < 8 and c >= 0:
            if board[r][c] == 1:
                return False
            r += 1
            c -= 1
        return True

    # Print all the solutions
    def print_all_states(self):
        for i, solution in enumerate(self.states):
            print('Solution: ' + str(i + 1))
            for row in solution:
                print(' '.join('Q' if cell == 1 else '-' for cell in row))
            print()


def random_individual():
    digits = [str(i) for i in range(8)]
    random.shuffle(digits)
    return ''.join(digits)


def random_population(amount):
    states = []
    for _ in range(amount):
        states.append(random_individual())
    return states


def state_toString(state):
    state.sort(key=lambda x: x[0])
    result = ''
    for i, (row, col) in enumerate(state):
        result += str(col)
    return result


def state_toTuple(state):
    result = []
    for i, num in enumerate(state):
        result.append((i, int(num)))
    return result
