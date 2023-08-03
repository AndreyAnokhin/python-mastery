file_path = '../Data/portfolio.dat'

total_sum = 0
with open(file_path, 'r') as file:
    for line in file.readlines():
        line_list = line.split()
        num_shares = float(line_list[1])
        price_shares = float(line_list[2])
        total_sum += num_shares * price_shares

print(total_sum)
