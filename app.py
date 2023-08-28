import sys


def find_pairs_with_sum(nums, target_sum):
    """
    Finds pairs of integers from a list that sum to a given value.

    Args:
        nums (list[int]): List of integers.
        target_sum (int): Target sum for pairs.

    Returns:
        list[tuple[int, int]]: List of pairs that sum to the target.
    """
    seen_numbers = set()
    result = []

    for num in nums:
        complement = target_sum - num
        if complement in seen_numbers:
            pair = (min(num, complement), max(num, complement))
            result.append(pair)
        seen_numbers.add(num)

    return result


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python app.py <filename>")
            sys.exit(1)
    
        filename = sys.argv[1]
        
        with open(filename, 'r') as file:
            for line in file:
                input_str, target_sum_str = map(str.strip, line.strip().split(' '))

                nums = list(map(int, input_str.split(',')))
                target_sum = int(target_sum_str)
                
                pairs = find_pairs_with_sum(nums, target_sum)
                
                if pairs:
                    print(f"############### {target_sum} #################")
                    for num in pairs:
                        print(f"{num[0]},{num[1]}")
                else:
                    print("No pairs found that sum to", target_sum)
    
    except FileNotFoundError:
        print("File not found. Please provide a valid filename.")
    except ValueError:
        print("Invalid input in the file. Please provide a valid list of integers and a target sum.")



"""
The time complexity of the find_pairs_with_sum function is O(n), where n is the number of elements in the input list.

Here's a breakdown of the complexity:

Iterating through the List (O(n)): The function iterates through the given list of numbers exactly once. For each number, it performs constant time operations like addition, subtraction, set lookup, and set insertion. Since these operations take constant time on average, the overall time complexity of this loop is O(n).

Set Operations (O(1)): The set operations involved in checking for the complement and adding numbers to the set both take constant time on average, assuming a reasonably well-distributed hash function. Since these operations are executed once for each number in the list, their contribution to the overall complexity is also O(n).

Combining these factors, the dominant factor in the time complexity is the iteration through the list, making the overall time complexity of the function O(n).

The space complexity of the function is also O(n), as the function uses a set to store seen numbers, which can potentially hold up to n unique numbers. Therefore, the auxiliary space used by the function grows linearly with the input size.
"""