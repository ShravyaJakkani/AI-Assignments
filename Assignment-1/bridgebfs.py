
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
    successors = set()

    if umbrella == 'Left':
        left_people = tuple(left)
        for i in range(len(left_people)):
            for j in range(i + 1, len(left_people)):
                p1 = left_people[i]
                p2 = left_people[j]
                new_left = left.difference([p1, p2])
                new_right = right.union([p1, p2])
                crossing_time = max(times[p1], times[p2])
                new_time = time + crossing_time
                if new_time <= 60:
                    desc = f"{p1} and {p2} cross → [{crossing_time} mins]"
                    new_state = (frozenset(new_left), frozenset(new_right), 'Right', new_time)
                    successors.add((new_state, desc))
    else:
        right_people = tuple(right)
        for p in right_people:
            new_left = left.union([p])
            new_right = right.difference([p])
            crossing_time = times[p]
            new_time = time + crossing_time
            if new_time <= 60:
                desc = f"{p} returns ← [{crossing_time} mins]"
                new_state = (frozenset(new_left), frozenset(new_right), 'Left', new_time)
                successors.add((new_state, desc))

    return successors

def dfs(state, visited, path):
    if (state[0], state[1], state[2], state[3]) in visited:
        return None
    visited.add((state[0], state[1], state[2], state[3]))

    if goalTest(state):
        return path + [(state, "Done!")]

    for next_state, action in moveGen(state):
        result = dfs(next_state, visited, path + [(state, action)])
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
        print(f"Umbrella: {umbrella}")
        print(f"Time: {time} mins")
        print(f"Action: {action}")
else:
    print("No solution found within 60 minutes.")

