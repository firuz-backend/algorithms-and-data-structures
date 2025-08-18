with open('data.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    file_headers = next(file_lines)
    line_values = (line.rstrip().split(',') for line in file_lines)
    only_a_series = (i for i in line_values if i[2] == 'a')
    summed = sum(int(i[1]) for i in only_a_series)

print(summed)
