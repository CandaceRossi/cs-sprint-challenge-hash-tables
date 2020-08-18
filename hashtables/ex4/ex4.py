def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = {}
    for num in a:
        if num >= 0:
            if num not in result:
                result[num] = 1
        if num < 0:
            num = abs(num)
            result[num] += 1
    if result[num] == 2:
        return result

# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


a = [-1, 2, 1, -2, 3, -4]

has_negatives(a)
