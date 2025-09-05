
initial_state = ('B', 'B', 'B', ' ', 'W', 'W', 'W')
goal_state =    ('W', 'W', 'W', ' ', 'B', 'B', 'B')
def goal_test(state):
    return state == goal_state

def movegen(state):
    moves = set()
    empty = state.index(' ')

    positions = (0, 1, 2, 3, 4, 5, 6)

    for i in positions:

        if state[i] == 'B':
            if i + 1 <= 6 and state[i + 1] == ' ':
                new_state = list(state)
                new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                moves.add((tuple(new_state), f"B at {i} → {i+1}"))
            elif i + 2 <= 6 and state[i + 2] == ' ' and state[i + 1] == 'W':
                new_state = list(state)
                new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                moves.add((tuple(new_state), f"B jumps from {i} → {i+2}"))

        if state[i] == 'W':
            if i - 1 >= 0 and state[i - 1] == ' ':
                new_state = list(state)
                new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                moves.add((tuple(new_state), f"W at {i} → {i-1}"))
            elif i - 2 >= 0 and state[i - 2] == ' ' and state[i - 1] == 'B':
                new_state = list(state)
                new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                moves.add((tuple(new_state), f"W jumps from {i} → {i-2}"))

    return moves

def dfs(state, visited, path):
    if state in visited:
        return None
    visited.add(state)

    if goal_test(state):
        return path + ((state, "Done!"),)

    next_moves = movegen(state)
    for new_state, action in next_moves:
        result = dfs(new_state, visited, path + ((state, action),))
        if result:
            return result

    return None

visited = set()
solution = dfs(initial_state, visited, ())

if solution:
    for i in range(len(solution)):
        state, action = solution[i]
        print(f"\nStep {i}:")
        print("".join(state))
        print(f"Action: {action}")
else:
    print("No solution found.")

