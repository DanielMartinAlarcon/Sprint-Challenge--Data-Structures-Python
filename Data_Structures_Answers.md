Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

        O(1).  I don't have to read through any of the array in order to know where to put things, and the array itself always has the same length because I'm just replacing old items with new ones.

2. What is the space complexity of your ring buffer's `append` function?

        O(0), because I'm just updating the values of existing variables.

3. What is the runtime complexity of your ring buffer's `get` method?

        O(n), because I go through each item in the array and test it so that I'm not returning any Nones.

4. What is the space complexity of your ring buffer's `get` method?

        O(n), because I'm creating a new array for the results before returning them.


5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
