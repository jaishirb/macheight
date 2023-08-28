# Find Pairs with Sum

This project includes a Python script that finds pairs of integers from a list that sum to a given value with O(n). It also includes unit tests to ensure the correctness of the implemented function.

## Usage

1. **find_pairs_with_sum Function**

   The `find_pairs_with_sum` function takes a list of integers and a target sum as inputs and returns a list of pairs that sum to the target. The function guarantees a time complexity of O(n) by using a hash set to efficiently track seen numbers. The output pairs are formatted as individual numbers on separate lines.

   To use the function, simply copy the `find_pairs_with_sum` function from the `app.py` file to your project. Ensure you have Python 3 installed.

2. **Running the Tests**

   The tests for the `find_pairs_with_sum` function are defined in the `test_app.py` file. These tests ensure that the function produces correct outputs for various input scenarios.

   To run the tests:
   
   1. Check the `app.py` and `test_app.py` files to be in the same directory.
   2. Create a file named `test_input.txt` in the same directory and add test cases in the format:
   
      ```
      input_numbers target_sum expected_output_pairs
      ```
   
      For example:
   
      ```
      1,9,5,0,20,-4,12,16,7 12 1,9;5,7
      4,2,8,6,5,9,1,3,7 12 1,11;2,10;3,9;4,8;5,7
      ```
    3. If you want to run the script directly without the tests, you need to create a file named `data.txt` or whatever you want, in the same directory, with the following format:

         ```
        input_numbers target_sum
        ```
    
        For example:
    
        ```
        1,2,3,4,5,6 7
        8,9,10,11,12 13
        ```
   4. Open a terminal/command prompt and navigate to the directory.

   5. Run the script with the command:
   
      ```
      python app.py <filename>
      ```
      Where filename is the name of the file you just created with the input data.
      
      Example: 
      ```bash
      python3 app.py data.txt
    
   6. Run the tests with the command:
   
      ```
      python -m unittest test_app.py
      ```

   The program will run, and you'll see the results displayed in the terminal.
