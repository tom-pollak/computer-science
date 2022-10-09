import random


def get_runs():
    for n in [0, 1]:
        if n == 0:
            complement_bit = 1
        else:
            complement_bit = 0
        runs = filter(
            lambda x: x > 1,
            map(len, "".join(map(str, state)).split(str(complement_bit))),
        )
        for run in runs:
            assert run <= 15, f"Run should not be greater than 15: {run} {state}"
            dict_item = runs_dict[n].get(run)
            if dict_item is None:
                runs_dict[n][run] = 1
            else:
                runs_dict[n][run] += 1


state = [random.randint(0, 1) for i in range(15)]
zeros = ones = 0
runs_dict = {0: {}, 1: {}}
previous_states = []
for i in range(2**15 - 1):
    # get_runs()
    if state in previous_states:
        print(f"Loop on state {state}, {previous_states.index(state), i}")
        break
    else:
        previous_states.append(state[:])

    num_zeros = len(list(filter(lambda x: x == 0, state)))
    num_ones = 15 - num_zeros
    zeros += num_zeros
    ones += num_ones

    output = state.pop()
    new_bit = state[0] ^ state[-1]
    state.insert(0, new_bit)
    print(f"{i} | {state} | {output}")
else:
    print("No loops found!")

print(f"Zeros: {zeros}, Ones: {ones}")
print(runs_dict)
