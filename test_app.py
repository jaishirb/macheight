import unittest
from app import find_pairs_with_sum

class TestFindPairsWithSumFromFile(unittest.TestCase):
    def test_pairs_from_file(self):
        """
        Test the find_pairs_with_sum function using input from a file.

        Reads input data and expected output pairs from a file and compares
        the function's output with the expected output.

        Test cases are provided in the format:
        input_numbers target_sum
        expected_output_pairs

        Each test case consists of a list of input numbers, a target sum,
        and a list of expected output pairs, all separated by spaces.

        If expected_output_pairs is "No pairs found", the function output
        is expected to be empty.

        Test passes if the function's output matches the expected output for
        each test case or prints appropriate error messages for invalid input.
        """
        try:
            filename = "test_input.txt"

            with open(filename, 'r') as file:
                input_str = file.readline().strip()
                nums_str, target_sum_str = input_str.split(' ')

                nums = list(map(int, nums_str.split(',')))
                target_sum = int(target_sum_str)

                pairs = find_pairs_with_sum(nums, target_sum)

                expected_output = file.readline().strip()
                if expected_output == "No pairs found":
                    expected_pairs = []
                else:
                    expected_pairs = [tuple(map(int, pair.split(','))) for pair in expected_output.split(';')]
                    expected_output_nums = [num for pair in expected_pairs for num in pair]

                output_nums = [num for pair in pairs for num in pair]

                self.assertEqual(output_nums, expected_output_nums)
                print("Test passed!")

        except FileNotFoundError:
            print("File not found. Please provide a valid filename.")
        except ValueError:
            print("Invalid input in the file. Please provide valid list of integers and a target sum.")

if __name__ == '__main__':
    unittest.main()


