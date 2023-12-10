def lis_dp(arr):
    """Get the length of the longest icreasing subsequence using DP."""

    lis_values = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[j] <= arr[i] and lis_values[i] < lis_values[j] + 1:
                lis_values[i] = lis_values[j] + 1

    return max(lis_values)


arr = [50, 3, 10, 7, 40, 80, 2, 3, 4, 5, 6, 7, 8, 40, 50, 70]
arr = [50, 3, 10, 7, 40, 80]

print("LIS: ", lis_dp(arr))
