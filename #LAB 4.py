#LAB 4

import csv

def main():
    # Path to the CSV file.
    file_path = "budget_data-1.csv"
    # Loads the dataset.
    data = load_csv(file_path)

    # Displays the original dataset.
    display_data(data, "Original Dataset")

    # Applies selection sort.
    sorted_data_selection = selection_sort(data.copy())
    display_data(sorted_data_selection, "Dataset after Selection Sort")

    # Applies insertion sort.
    sorted_data_insertion = insertion_sort(data.copy())
    display_data(sorted_data_insertion, "Dataset after Insertion Sort")


# Selection sort implementation.
def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j][0] < data[min_idx][0]:  # Compares dates as strings.
                min_idx = j
        # Swaps the found minimum element with the first element.
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

# Insertions sort implementation.
def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        # Compares dates as strings.
        while j >= 0 and data[j][0] > key[0]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Loads the dataset from CSV file.
def load_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)[1:]  # Skips header row
    return data

# Displays the first few records.
def display_data(data, title):
    print(f"{title}:")
    for row in data[:5]:
        print(row)
    print()

# Calls the main function.
main()


