def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = {}
    for nums in arrays:
        for num in nums:
            if num not in result:
                result[num] = num
            else:
                return num
    for key, value in result.items():
        if value == 2:
            return key

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
