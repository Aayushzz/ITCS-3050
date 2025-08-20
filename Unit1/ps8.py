def above_threshold(lst, threshold):
    result = []
    for number in lst:
        if number > threshold:
            result.append(number)
    print(result)
      
    