def count_evens(lst):
    ans = 0
    for num in lst:
        if num%2 == 0:
            ans += 1
    return ans