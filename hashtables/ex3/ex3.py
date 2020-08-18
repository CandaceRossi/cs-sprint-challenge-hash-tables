def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    corr = {}
    result = []
    for nums in arrays:
        for num in nums:
            if num in corr:
                corr[num] += 1
            else:
                corr[num] = 1

            if num not in result and corr[num] > 1:
                result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
