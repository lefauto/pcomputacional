def fibonacci(x):
    result = [0, 1]
    for x in range(2, x):
        result.append(result[x - 2] + result[x - 1])
    return result


print(fibonacci(20))
