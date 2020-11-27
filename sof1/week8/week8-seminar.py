def find_infulencer(following,
                    person_index=0,
                    follower_index=0,
                    first_run=True):
    follower_index = (follower_index + 1) % len(following)
    # First item does not check prev item so can't be included in the +1
    if person_index == follower_index + 1 or person_index == follower_index == 0:
        return person_index
    elif person_index == 0 and not first_run:
        return -1

    # Not following next person
    if following[person_index][follower_index] == 0:
        # Next person following current
        if following[follower_index][person_index] == 1:
            # Current person could be infulencer
            infulencer = find_infulencer(following,
                                         person_index,
                                         follower_index,
                                         False)
        else:
            # Neither can be infulencers (as not following next person)
            infulencer = find_infulencer(following,
                                         follower_index + 1,
                                         follower_index + 1,
                                         False)

    # Next person not following current person (and current person following next person)
    elif following[person_index + 1][person_index] == 0:
        # Next person could be infulencer
        infulencer = find_infulencer(following,
                                     follower_index,
                                     follower_index,
                                     False)

    # Both following each other so neither infulencers
    else:
        infulencer = find_infulencer(following,
                                     follower_index + 1,
                                     follower_index + 1,
                                     False)
    return infulencer


def connection_degree(network, source, target):
    queue = [{'name': source, 'weight': 0}]
    visited = []
    while queue:
        connection = queue.pop(0)
        visited.append(connection['name'])
        if connection['name'] == target:
            if connection['weight'] > 3:
                return 0
            return connection['weight']
        for vertex in network[connection['name']]:
            if vertex not in [x['name'] for x in queue] + visited:
                queue.append({
                    'name': vertex, 'weight': connection['weight'] + 1
                })
    return 0


following = [[0, 1, 1, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0], [0, 1, 1, 0, 0]]
infulencer = find_infulencer(following)
print(infulencer)

network = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

connection_degree = connection_degree(network, 'A', 'E')
print(connection_degree)
