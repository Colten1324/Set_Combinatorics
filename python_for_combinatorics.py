from itertools import combinations

def set_combos(arr, r):
    return list(combinations(arr, r))

def main():
    try:
        w = int(input("Enter number of possible integers w: "))  # Take input from the user
        s = int(input("Enter the distance of the set s: "))
        
        arr = list(range(1, w + 1))  # Creating a list of numbers from 1 to w
        
        combinations_list = set_combos(arr, s)
        
        with open("combinations.txt", "w") as file:
            for combo in combinations_list:
                file.write(str(combo) + '\n')

        num_sets = len(combinations_list)
        print("Number of sets:", num_sets)
        
        print("Combinations written to 'combinations.txt'")
    except ValueError:
        print("Invalid input. Please enter valid numbers and length.")

if __name__ == "__main__":
    main()
