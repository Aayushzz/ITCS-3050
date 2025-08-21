def get_evens(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result        
    