def cdf(arr, val, start):
    total = float(len(arr))
    i = start
    found = False
    count = start
    while i < total and not found:
        found = arr[i] > val
        if not found:
            count += 1
        i += 1
    result = [count / total, i - 1]
    return result


def generate_cdf(arr, values):
    res = []
    start = 0
    for val in values:
        cdf_val = cdf(arr, val, start)
        res.append(cdf_val[0])
        start = cdf_val[1]
    return res
