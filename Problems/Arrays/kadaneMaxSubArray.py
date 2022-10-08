def maxSubArray(array):
    currSum = array[0]
    maxSum = currSum

    for num in array[1:]:

        currSum = max(num, currSum + num)
        maxSum = max(currSum, maxSum)
    return maxSum


print(maxSubArray([0, -2, -13, 4, 5, -9, 5, 6]))
 