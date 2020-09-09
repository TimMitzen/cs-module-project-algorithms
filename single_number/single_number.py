'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    duplicates = [] # creates an empty list
    for duplicate in arr: #loops over the arr
        if duplicate in duplicates:# if the duplicate is there remove it
            duplicates.remove(duplicate)
        else:
            duplicates.append(duplicate)#if not add it
    return duplicates[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")