# Define a function to generate a random list of a given size
    # Initialize an empty list
def get_random_list(size):
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(0, 100))
    return random_list

def get_list_average(random_list):
    return sum(random_list) / len(random_list)

def get_list_median(random_list):
    sorted_list = sorted(random_list)
    if len(random_list) % 2 == 0:
        return (sorted_list[len(random_list)//2] + sorted_list[len(random_list)//2 - 1]) / 2
    else:
        return sorted_list[len(random_list)//2]

def get_list_mode(random_list):
    list_count = {}
    for item in random_list:
        if item in list_count:
            list_count[item] += 1
        else:
            list_count[item] = 1
    max_count = 0
    modes = []
    for key, value in list_count.items():
        if value > max_count:
            max_count = value
            modes = [key]
        elif value == max_count:
            modes.append(key)
    return modes

