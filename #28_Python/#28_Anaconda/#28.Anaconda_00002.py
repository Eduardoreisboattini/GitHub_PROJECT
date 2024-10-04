# Data Analysis Example
if __name__ == "__main__":
    import random
    import statistics

    random_list = get_random_list(100)
    print(f"Average: {get_list_average(random_list)}")
    print(f"Median: {get_list_median(random_list)}")
    print(f"Mode: {get_list_mode(random_list)}")

