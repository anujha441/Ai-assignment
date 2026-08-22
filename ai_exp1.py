class StateSpaceProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def is_goal(self, state):
        """Check if the current state is the goal state."""
        return state == self.goal_state

    def get_successors(self, state):
        """Generate all possible successor states."""

        successors = []
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        # Find the blank space (0)
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    x, y = i, j

        # Generate new states
        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]

                # Swap blank with adjacent tile
                new_state[x][y], new_state[nx][ny] = (
                    new_state[nx][ny],
                    new_state[x][y],
                )

                successors.append(new_state)

        return successors


# Initial and Goal States
initial = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 0],
    [6, 7, 8]
]

# Create Problem
problem = StateSpaceProblem(initial, goal)

# Print Initial State
print("Initial State:")
for row in problem.initial_state:
    print(row)

# Print Goal State
print("\nGoal State:")
for row in problem.goal_state:
    print(row)

# Print Successor States
print("\nSuccessor States:")
successors = problem.get_successors(problem.initial_state)

for index, state in enumerate(successors, start=1):
    print(f"\nSuccessor {index}:")
    for row in state:
        print(row)

# Check Goal State
print("\nIs Initial State Goal?", problem.is_goal(problem.initial_state))
print("Is Goal State Goal?", problem.is_goal(problem.goal_state))