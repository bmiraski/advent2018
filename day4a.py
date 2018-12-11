"""Determine solution for first problem on Day 4."""
from collections import Counter


def mostsleep(dataset):
    """Find the most numbers of sleep cycles per guard."""
    mostsleep = 0
    for line in dataset:
        if '#' in line:
            sleep = 0
        else:
            sleep += 1
            if sleep > mostsleep:
                mostsleep = sleep


def getguardlist(dataset):
    """Determine the set of all guard numbers."""
    guards = []
    for line in dataset:
        if '#' in line:
            parts = line.split()
            for sec in parts:
                if '#' in sec:
                    if sec not in guards:
                        guards.append(sec)
    return guards


def detsleepforguard(guard, dataset):
    """Build a list of the minute values guard was asleep."""
    sleep_min = []
    for x in range(len(dataset)):
        if guard in dataset[x]:
            sleep_min = processsleepcycle(dataset[x+1], dataset[x+2],
                                          sleep_min)
            if x+3 < len(dataset):
                if '#' not in dataset[x+3]:
                    sleep_min = processsleepcycle(
                        dataset[x+3], dataset[x+4], sleep_min
                        )
                    if x+5 < len(dataset):
                        if '#' not in dataset[x+5]:
                            sleep_min = processsleepcycle(
                                dataset[x+5], dataset[x+6], sleep_min
                                )
                            if x+7 < len(dataset):
                                if '#' not in dataset[x+7]:
                                    sleep_min = processsleepcycle(
                                        dataset[x+7], dataset[x+8], sleep_min
                                    )
    return sleep_min


def processsleepcycle(str1, str2, sleep_min):
    """Build a list of the minute values a guard was asleep."""
    start_sleep = int(str1[15:17])
    end_sleep = int(str2[15:17])
    for x in range(start_sleep, end_sleep):
        sleep_min.append(x)
    return sleep_min


def findbestminute(dataset):
    """Determine the top minute across all guards."""
    guard = ""
    max_min = 0
    max_min_times = 0
    for item in dataset:
        sleep = item[1]
        maxi = sleep.most_common(1)
        if maxi[0][1] > max_min_times:
            guard, max_min, max_min_times = item[0], maxi[0][0], maxi[0][1]
    return (guard, max_min, max_min_times)


with open('inputday4.txt') as f:
    dataset = f.readlines()

dataset.sort()

# print(dataset)

guards = getguardlist(dataset)

# print(guards)

compiled = []

for guard in guards:
    sleep = detsleepforguard(guard, dataset)
    # print(guard, sleep)
    sleep_dict = Counter(sleep)
    compiled.append((guard, sleep_dict))

for item in compiled:
    sleep = item[1]
    total_asleep = sum(sleep.values())
    max_min = 0
    for key in sleep.keys():
        times = sleep[key]
        if max_min == 0:
            max_min = key
        else:
            if times > sleep[max_min]:
                max_min = key

    print(f"""
        Guard: {item[0]}, Total Asleep: {total_asleep}, Top Min: {max_min}"""
         )

maximum_minute = findbestminute(compiled)
print("Guard {} was asleep {} times in minute {}".format(
    maximum_minute[0], maximum_minute[2], maximum_minute[1]
    ))
