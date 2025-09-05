
times = {
    'Amogh': 5,
    'Ameya': 10,
    'Grandmother': 20,
    'Grandfather': 25
}

people = tuple(times.keys())
def goalTest(state):
    left, right, umbrella, time = state
    return len(left) == 0 and time <= 60
def moveGen(state):
    left, right, umbrella, time = state
    moves = set()

    if umbrella == 'Left':
        left_side = tuple(left)
        for i in range(len(left_side)):
            for j in range(i + 1, len(left_side)):
                p1 = left_side[i]
                p2 = left_side[j]
                new_left = left.difference([p1, p2])
                new_right = right.union([p1, p2])
                cross_time = max(times[p1], times[p2])
                new_time = time + cross_time
                if new_time <= 60:
                    new_state = (frozenset(new_left), frozenset(new_right), 'Right', new_time)
                    move_desc = f"{p1} and {p2} cross → [{cross_time} mins]"
                    moves.add((new_state, move_desc))
    else:
        right_side = tuple(right)
        for p in right_side:
            new_left = left.union([p])
            new_right = right.difference([p])
            cross_time = times[p]
            new_time = time + cross_time
            if new_time <= 60:
                new_state = (frozenset(new_left), frozenset(new_right), 'Left', new_time)
                move_desc = f"{p} returns ← [{cross_time} mins]"
                moves.add((new_state, move_desc))
    return moves

def dfs(state, visited, path):
    key = (state[0], state[1], state[2])
    if (key, state[3]) in visited:
        return None
    visited.add((key, state[3]))

    if goalTest(state):
        return path + ((state, "Done!"),)

    for new_state, action in moveGen(state):
        result = dfs(new_state, visited, path + ((state, action),))
        if result:
            return result

    return None


initial_state = (frozenset(people), frozenset(), 'Left', 0)
visited = set()
solution = dfs(initial_state, visited, ())


if solution:
    for i, (state, action) in enumerate(solution):
        left, right, umbrella, time = state
        print(f"\nStep {i}:")
        print(f"Left Side: {sorted(tuple(left))}")
        print(f"Right Side: {sorted(tuple(right))}")

