def count_less_than(numbers, threshold):
    ans = 0; 
    for num in numbers:
        if num < threshold: 
            ans += 1
    return ans