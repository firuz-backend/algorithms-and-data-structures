def get_min_max(data):
    if not data:
        return None

    min_idx = max_idx = 0
    min_val = max_val = data[0]

    for index, val in enumerate(data):
        if val < min_val:
            min_val = val
            min_idx = index
        elif val > max_val:
            max_val = val
            max_idx = index

    return min_idx, max_idx


data = [9]

print(get_min_max(data))
