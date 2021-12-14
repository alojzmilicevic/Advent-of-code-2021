import linereader
import time

initial_state = [int(x) for x in linereader.read_line('6.input.txt', ',')]


def simulate_bad():
    to_add = 0
    for fish in range(0, len(initial_state)):
        if initial_state[fish] > 0:
            initial_state[fish] -= 1
        elif initial_state[fish] == 0:
            initial_state[fish] = 6
            to_add += 1

    for k in range(0, to_add):
        initial_state.append(8)


def sim_good(fish, days):
    fish_age = {key: 0 for key in range(0, 9)}
    for age in fish:
        fish_age[age] += 1

    for day in range(0, days):
        new_fish = fish_age[0]
        fish_age = {key - 1: value for (key, value) in fish_age.items() if key > 0}
        fish_age[6] += new_fish
        fish_age[8] = new_fish
    return sum(fish_age.values())


start_time = time.time()

print(sim_good(initial_state, 256))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(0, 256):
    simulate_bad()

print("--- %s seconds ---" % (time.time() - start_time))
print(len(initial_state))
