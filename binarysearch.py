#English version of it

# List of numbers to search
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def search(value: int) -> str:
    low = 0  # lowest index of the list
    high = len(numbers) - 1  # highest index of the list

    while low <= high:  # start the search
        middle = (low + high) // 2  # calculate the middle index
        guess = numbers[middle]  # make a guess by picking the middle element

        if guess == value:  # check if the guess is correct
            return "Value found"
        
        if guess < value:  # check if the guess is too low
            low = middle + 1  # if so, continue searching in the higher half (from 5 onwards)
        
        else:  # if the guess is too high
            high = middle - 1  # continue searching in the lower half (up to 4)
    
    return "Value not found"  # if the value is not found, return a message

print(search(6))  # test the function with value 6


"""
The algorithm works like an "intelligent guess." Instead of checking each item in the list one by one to see if it matches the value, 
it divides the list in half and checks if the value we are looking for is in the middle. If it is, it eliminates a large part of 
the search process and finds the value in one step.

If the value we are looking for is smaller than the middle element, the algorithm eliminates any numbers larger than the middle 
value. For example, if the middle is 5, any numbers greater than 5 are eliminated.

How does it do this?

For example, if we are searching for the value 2 in the list, here's what happens: it starts by considering the total number of 
elements in the list (9 in this case). It divides it by 2, which gives 4.5, but it rounds this down to 4, which corresponds to 
the index of element 5. The algorithm checks if the value is equal to 5, but since we're looking for 2, this condition is false. 
Thus, the program understands that 5 is too high, and it discards any numbers greater than 5.

Now the algorithm needs to find the new middle. Since it divided by 2 earlier, it subtracts 1 from the middle index (4), resulting 
in index 3. It then checks if the value at index 3 is equal to 2. If it's not, the process repeats by dividing the index (3) by 2 
to get index 1, which is the value 2.

This only takes 2 comparisons to complete.
"""