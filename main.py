import ChessBoard

# 1. Assignment
lst = [(0, 0), (2, 1), (4, 2), (6, 3), (1, 4), (3, 5), (7, 7), (5, 6)]
transit = [(2, 1), (5, 2)]
#
b1 = ChessBoard.EightQueens(lst)
b1.show_board()
print("Heuristic: " + str(b1.heuristic()))
print("________________________")
b2 = ChessBoard.EightQueens(lst, transit)
b2.show_board()
print("Heuristic: " + str(b2.heuristic()))
print("------------------------")
b2.move_queen((1, 1), (3, 1))
b2.move_queen((6, 3), (6, 2))
b2.show_board()
print("Heuristic: " + str(b2.heuristic()))
print("________________________")
b3 = ChessBoard.EightQueens()
b3.show_board()
print("Heuristic: " + str(b3.heuristic()))

# 2. Assignment
b = ChessBoard.EightQueens()
b.genetic_algorithm(100)

# # 3. Assignment
solver = ChessBoard.EightQueensBacktrackingProblem()
solver.runner()
solver.print_all_states()
