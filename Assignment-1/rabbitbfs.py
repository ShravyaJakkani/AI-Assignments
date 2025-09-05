def goalTest(state):
    return state == ['W', 'W', 'W', '_', 'E', 'E', 'E']

def moveGen(state):
    moves = []
    for i in range(len(state)):
        if state[i] == '_':
           
            if i - 1 >= 0 and state[i - 1] == 'E':
                new_state = state.copy()
                new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                moves.append(new_state)
            if i - 2 >= 0 and state[i - 2] == 'E' and state[i - 1] in ('W', 'E'):
                new_state = state.copy()
                new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                moves.append(new_state)   
            if i + 1 < len(state) and state[i + 1] == 'W':
                new_state = state.copy()
                new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                moves.append(new_state)
   if i + 2 < len(state) and state[i + 2] == 'W' and state[i + 1] in ('W', 'E'):
                new_state = state.copy()
                new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                moves.append(new_state)
    return moves

def dfs(current, path, visited, solutions):
    state_str = ''.join(current)
    if state_str in visited:
        return
    visited.add(state_str)

    path.append(current)

    if goalTest(current):
        solutions.append(path.copy())
        return

    for move in moveGen(current):
        dfs(move, path, visited, solutions)

    path.pop()

start = ['E', 'E', 'E', '_', 'W', 'W', 'W']
visited_states = set()
solution_paths = []
dfs(start, [], visited_states, solution_paths)
if solution_paths:
    for i, step in enumerate(solution_paths[0]):
        print(f"Step {i}: {step}")
else:
    print("No solution found.")

