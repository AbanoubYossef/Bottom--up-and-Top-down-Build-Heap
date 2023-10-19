import random  # Import the random module for generating random data
import matplotlib.pyplot as plt  # Import the matplotlib module for plotting graphs

# Define the 'heapify' function, which is used to maintain the heap property
# in a max-heap and returns the number of comparisons and assignments made.
def heapify(my_list, length_mylist, current):
    comparisons = 0  # Initialize the comparison count
    assignments = 0  # Initialize the assignment count
    largest = current
    left = 2 * current + 1
    right = 2 * current + 2

    if left < length_mylist:
        comparisons += 1  # Increment comparison count
        if my_list[left] > my_list[largest]:
            largest = left

    if right < length_mylist:
        comparisons += 1  # Increment comparison count
        if my_list[right] > my_list[largest]:
            largest = right

    if largest != current:
        my_list[current], my_list[largest] = my_list[largest], my_list[current]
        assignments += 2  # Increment assignment count for swap
        comp, assign = heapify(my_list, length_mylist, largest)
        comparisons += comp
        assignments += assign

    return comparisons, assignments

# Define the 'build_heap_bottom_up' function for creating a max-heap
# using the bottom-up approach and return the number of comparisons and assignments made.
def build_heap_bottom_up(my_list):
    length_mylist = len(my_list)
    comparisons = 0  # Initialize the comparison count
    assignments = 0  # Initialize the assignment count

    for i in range(length_mylist // 2 - 1, -1, -1):
        comp, assign = heapify(my_list, length_mylist, i)
        comparisons += comp
        assignments += assign

    return comparisons, assignments

# Define the 'insert_top_down' function for inserting an element into a max-heap
# using the top-down approach and return the number of comparisons and assignments made.
def insert_top_down(my_list, element):
    comparisons = 0  # Initialize the comparison count
    assignments = 0  # Initialize the assignment count
    my_list.append(element)
    n = len(my_list)
    i = n - 1

    while i > 0:
        parent = (i - 1) // 2
        comparisons += 1  # Increment comparison count
        if my_list[i] > my_list[parent]:
            my_list[i], my_list[parent] = my_list[parent], my_list[i]
            assignments += 2  # Increment assignment count for swap
            i = parent
        else:
            break

    return comparisons, assignments

# Define the 'build_heap_top_down' function for creating a max-heap
# using the top-down approach and return the number of comparisons and assignments made.
def build_heap_top_down(my_list):
    heap = []
    comparisons = 0  # Initialize the comparison count
    assignments = 0  # Initialize the assignment count

    for element in my_list:
        comp, assign = insert_top_down(heap, element)
        comparisons += comp
        assignments += assign

    return comparisons, assignments


# Define the 'heap_sort' function for sorting a list using the heap sort algorithm.
# It doesn't return the counts of comparisons and assignments, so no comments are needed here.

def heap_sort(my_list):
    length_of_mylist = len(my_list)
    build_heap_bottom_up(my_list)
    for i in range(length_of_mylist - 1, 0, -1):
        my_list[i], my_list[0] = my_list[0], my_list[i]
        heapify(my_list, 0, i)


# Define the 'generate_random_data' function for generating a list of random data.
# It uses the 'random' module you imported earlier.

def generate_random_data(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

# Define the 'average_case_analysis' function for analyzing the average case performance
# of the heap construction methods and plotting the results.

def average_case_analysis():
    dimensions = list(range(100, 10001, 100))
    m = 5  # Number of repetitions

    bottom_up_comparisons_avg = []
    bottom_up_assignments_avg = []
    top_down_comparisons_avg = []
    top_down_assignments_avg = []
    top_down_total_avg = []
    bottom_up_total_avg = []

    for dimension in dimensions:
        bottom_up_comparisons_sum = 0
        bottom_up_assignments_sum = 0
        top_down_comparisons_sum = 0
        top_down_assignments_sum = 0

        for _ in range(m):
            my_list = generate_random_data(dimension, 1, 10000)

            # Measure operations for bottom-up build heap
            comparisons, assignments = build_heap_bottom_up(my_list.copy())
            bottom_up_comparisons_sum += comparisons
            bottom_up_assignments_sum += assignments

            # Measure operations for top-down build heap
            comparisons, assignments = build_heap_top_down(my_list.copy())
            top_down_comparisons_sum += comparisons
            top_down_assignments_sum += assignments

        # Calculate the average for the current dimension and repetition
        bottom_up_comparisons_avg.append(bottom_up_comparisons_sum / m)
        bottom_up_assignments_avg.append(bottom_up_assignments_sum / m)
        top_down_comparisons_avg.append(top_down_comparisons_sum / m)
        top_down_assignments_avg.append(top_down_assignments_sum / m)
        top_down_total_avg.append(
            (top_down_comparisons_sum + top_down_assignments_sum) / m
        )
        bottom_up_total_avg.append(
            (bottom_up_comparisons_sum + bottom_up_assignments_sum) / m
        )

    # Create subplots
    fig, axs = plt.subplots(3, 1, figsize=(6, 10))

    data = [
        (bottom_up_comparisons_avg, 'Bottom-Up Comparisons (Average)', 'Total Comparisons'),
        (top_down_comparisons_avg, 'Top-Down Comparisons (Average)', 'Total Comparisons'),
        (bottom_up_assignments_avg, 'Bottom-Up Assignments (Average)', 'Total Assignments'),
        (top_down_assignments_avg, 'Top-Down Assignments (Average)', 'Total Assignments'),
        (bottom_up_total_avg, 'Bottom-Up Total Operations (Average)', 'Total Operations'),
        (top_down_total_avg, 'Top-Down Total Operations (Average)', 'Total Operations'),
    ]

    for i in range(0, 6, 2):  # Increment by 2 to group every two figures
        row = i // 2
        ax = axs[row]

        ax.plot(dimensions, data[i][0], label=data[i][1])
        ax.plot(dimensions, data[i + 1][0], label=data[i + 1][1])
        ax.set_xlabel('Input Size (n)')
        ax.set_ylabel('Total Operations')
        ax.legend()
        ax.set_title(f'Heap Construction Comparison (Average Case)')

    plt.tight_layout()
    plt.show()

# Define the 'worst_case_analysis' function for analyzing the worst-case performance
# of the heap construction methods and plotting the results.


def worst_case_analysis():
    dimensions = list(range(100, 10001, 100))
    worst_case_comparisons_bottom_up = []
    worst_case_assignments_bottom_up = []
    worst_case_comparisons_top_down = []
    worst_case_assignments_top_down = []

    for dimension in dimensions:
        # Generate worst-case input data for both methods
        # my_list_1 = generate_worst_case_bottom_up(dimension)  # Worst-case for bottom-up
        my_list_2 = list(range(0, dimension))  # Worst-case for top-down

        # Measure operations for bottom-up build heap in worst case
        comparisons, assignments = build_heap_bottom_up(my_list_2.copy())
        worst_case_comparisons_bottom_up.append(comparisons)
        worst_case_assignments_bottom_up.append(assignments)

        # Measure operations for top-down build heap in worst case
        comparisons, assignments = build_heap_top_down(my_list_2.copy())
        worst_case_comparisons_top_down.append(comparisons)
        worst_case_assignments_top_down.append(assignments)

    # Create subplots for worst-case comparisons and assignments
    fig, axs = plt.subplots(2, 1, figsize=(6, 10))

    data = [
        (worst_case_comparisons_bottom_up, 'Bottom-Up Worst Case Comparisons', 'Total Comparisons (Worst Case)'),
        (worst_case_comparisons_top_down, 'Top-Down Worst Case Comparisons', 'Total Comparisons (Worst Case)'),
        (worst_case_assignments_bottom_up, 'Bottom-Up Worst Case Assignments', 'Total Assignments (Worst Case)'),
        (worst_case_assignments_top_down, 'Top-Down Worst Case Assignments', 'Total Assignments (Worst Case)')
    ]

    for i in range(0, 4, 2):  # Increment by 2 to group every two figures
        row = i // 2
        ax = axs[row]

        ax.plot(dimensions, data[i][0], label=data[i][1])
        ax.plot(dimensions, data[i + 1][0], label=data[i + 1][1])
        ax.set_xlabel('Input Size (n)')
        ax.set_ylabel('Total Operations')
        ax.legend()
        ax.set_title(f'Heap Construction Comparison (Worst Case)')

    plt.tight_layout()
    plt.show()
# Check if the script is being run as the main program.

if __name__ == "__main__":
    average_case_analysis()
    worst_case_analysis()
