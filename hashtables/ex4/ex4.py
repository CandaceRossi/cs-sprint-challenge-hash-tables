def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    posneg = {}
    result = []
    for nums in a:
        if nums >= 0:
            posneg[nums] = True

    for nums in a:
        if nums < 0 and abs(nums) in posneg:
            result.append(-nums)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


# a = [-1, 2, 1, -2, 3, -4]

# has_negatives(a)
