TOTAL_ELEMENTS = 0
OVERALL_MEAN = 0.0
dataset_1d = []
dataset_2d = []
is_2d = False

def display_summary_built_in():
    """Display basic statistics using built-in functions."""
    global TOTAL_ELEMENTS, OVERALL_MEAN
    if not is_2d and not dataset_1d:
        print("\n[Error] Please input data first using option 1!")
        return
    elif is_2d and not dataset_2d:
        print("\n[Error] Please input data first using option 1!")
        return

    print("\nData Summary:")
    if not is_2d:
        total = len(dataset_1d)
        minimum = min(dataset_1d)
        maximum = max(dataset_1d)
        elements_sum = sum(dataset_1d)
        avg = elements_sum / total if total > 0 else 0
        
        TOTAL_ELEMENTS = total
        OVERALL_MEAN = avg
        
        print(f" - Total elements: {total}")
        print(f" - Minimum value: {minimum}")
        print(f" - Maximum value: {maximum}")
        print(f" - Sum of all values: {elements_sum}")
        print(f" - Average value: {avg:.2f}")
    else:
        flat_list = [item for row in dataset_2d for item in row]
        total = len(flat_list)
        minimum = min(flat_list)
        maximum = max(flat_list)
        elements_sum = sum(flat_list)
        avg = elements_sum / total if total > 0 else 0
        
        TOTAL_ELEMENTS = total
        OVERALL_MEAN = avg
        
        print("\nFormatted Grid Structure:")
        for row in dataset_2d:
            print(" ".join(map(str, row)))
            
        print(f"\n - Total elements: {total}")
        print(f" - Minimum value: {minimum}")
        print(f" - Maximum value: {maximum}")
        print(f" - Sum of all values: {elements_sum}")
        print(f" - Average value: {avg:.2f}")

def calculate_factorial_recursive(n):
    """Calculate factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial_recursive(n - 1)

def filter_data_lambda():
    """Filter dataset based on threshold using a lambda function."""
    if not is_2d and not dataset_1d:
        print("\n[Error] Please input data first!")
        return
        
    try:
        threshold = float(input("Enter a threshold value to filter out data above this value:\n"))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    working_data = dataset_1d if not is_2d else [item for row in dataset_2d for item in row]
    filtered_list = list(filter(lambda x: x >= threshold, working_data))
    
    print(f"\nFiltered Data (values >= {int(threshold)}):")
    if filtered_list:
        print(", ".join(map(str, filtered_list)))
    else:
        print("No values found matching the threshold.")

def sort_dataset():
    """Sort 1D list or 2D list rows."""
    global dataset_1d, dataset_2d
    if not is_2d and not dataset_1d:
        print("\n[Error] Please input data first!")
        return
        
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ")
    
    is_reverse = True if choice == '2' else False

    if not is_2d:
        dataset_1d.sort(reverse=is_reverse)
        order_str = "Descending" if is_reverse else "Ascending"
        print(f"\nSorted Data in {order_str} Order:")
        print(", ".join(map(str, dataset_1d)))
    else:
        new_sorted_2d = []
        for row in dataset_2d:
            sorted_row = sorted(row, reverse=is_reverse)
            new_sorted_2d.append(sorted_row)
            
        print("\nSorted 2D Grid Structure:")
        for row in new_sorted_2d:
            print(" ".join(map(str, row)))

def get_dataset_statistics():
    """Return multiple statistical values from the dataset."""
    if not is_2d and not dataset_1d:
        return None
        
    working_data = dataset_1d if not is_2d else [item for row in dataset_2d for item in row]
    minimum = min(working_data)
    maximum = max(working_data)
    elements_sum = sum(working_data)
    avg = elements_sum / len(working_data) if len(working_data) > 0 else 0
    
    return minimum, maximum, elements_sum, avg

def print_dataset_characteristics(*args, **kwargs):
    """Demonstrate the use of *args and **kwargs."""
    if args:
        for arg in args:
            pass
    if kwargs:
        for key, value in kwargs.items():
            pass

def main_menu():
    """Main function to handle menu navigation."""
    global dataset_1d, dataset_2d, is_2d
    
    print("Welcome to the Data Analyzer and Transformer Program")
    
    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")
        
        choice = input("Please enter your choice: ")
        
        if choice == '1':
            print("\nStep 1: Input Data")
            print("Select Data Type:")
            print("1. 1D Array")
            print("2. 2D Array")
            type_choice = input("Enter choice: ")
            
            if type_choice == '1':
                is_2d = False
                raw_input = input("Enter data for a 1D array (separated by spaces):\n")
                try:
                    dataset_1d = [int(x) for x in raw_input.split()]
                    print("\nData has been stored successfully!")
                except ValueError:
                    print("[Error] Please enter valid integers separated by spaces.")
            elif type_choice == '2':
                is_2d = True
                try:
                    rows = int(input("Enter number of rows: "))
                    dataset_2d = []
                    for i in range(rows):
                        row_input = input(f"Enter values for row {i+1} (separated by spaces): ")
                        row_data = [int(x) for x in row_input.split()]
                        dataset_2d.append(row_data)
                    print("\nData has been stored successfully!")
                except ValueError:
                    print("[Error] Invalid data format entered.")
                
        elif choice == '2':
            print("\nStep 2: Display Data Summary (Built-in Functions)")
            display_summary_built_in()
            
        elif choice == '3':
            print("\nStep 3: Calculate Factorial (Recursion)")
            try:
                num = int(input("Enter a number to calculate its factorial: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    result = calculate_factorial_recursive(num)
                    print(f"\nFactorial of {num} is: {result}")
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
        elif choice == '4':
            print("\nStep 4: Filter Data by Threshold (Lambda Function)")
            filter_data_lambda()
            
        elif choice == '5':
            print("\nStep 5: Sort Data")
            sort_dataset()
            
        elif choice == '6':
            print("\nStep 6: Display Dataset Statistics (Return Multiple Values)")
            stats = get_dataset_statistics()
            if stats is None:
                print("\n[Error] Please input data first!")
            else:
                minimum, maximum, elements_sum, avg = stats
                print("\nDataset Statistics:")
                print(f" - Minimum value: {minimum}")
                print(f" - Maximum value: {maximum}")
                print(f" - Sum of all values: {elements_sum}")
                print(f" - Average value: {avg:.2f}")
                print_dataset_characteristics(total_items=TOTAL_ELEMENTS, global_mean=OVERALL_MEAN)
                
        elif choice == '7':
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option between 1 and 7.")

if __name__ == "__main__":
    main_menu()
