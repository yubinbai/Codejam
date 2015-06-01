function kadane(array)
    # kadane's dynamic programming algorithm
    maxL, maxR, maxSum = -1, -1, 0.0
    currL, currR, currSum = 0, 0, 0.0
    for (i, a) in enumerate(array)
        if currSum < 0
            currL, currR, currSum = i, i + 1, a
        else
            currR, currSum = i + 1, currSum + a
        end
        if maxSum < currSum
            maxL, maxR, maxSum = currL, currR, currSum
        end
    end
    return maxL, maxR, maxSum
end

function kadane2(array)
    # kadane's dynamic programming algorithm
    maxSum = 0.0
    currSum = 0.0
    for a in array
        currSum = max(a, a + currSum)
        maxSum = max(maxSum, currSum)
    end
    return maxSum
end

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
println(kadane(array))
