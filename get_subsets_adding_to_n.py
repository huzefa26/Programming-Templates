def get_subsets_adding_to_n(array, n):
    dp = [1] + [0]*n
    curr = 0
    for i in range(0, len(array)):
        curr += array[i]
        for  j in range(min(n, curr), array[i]-1, -1):
            dp[j] += dp[j - array[i]]
    return dp[-1]
