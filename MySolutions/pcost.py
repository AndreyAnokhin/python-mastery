file_path = '../Data/portfolio.dat'

def portfolio_cost(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line_list = line.split()
            try:
                num_shares = float(line_list[1])
            except ValueError as e:
                print(f"Couldn't parse: {line_list[1]}")
                print(f"Reason: {e}")
            try:
                price_shares = float(line_list[2])
            except ValueError as e:
                print(f"Couldn't parse: {line_list[2]}")
                print(f"Reason: {e}")
            total_sum += num_shares * price_shares
    return total_sum


# print(portfolio_cost(file_path))
file_path_bad_data = '../Data/portfolio3.dat'
print(portfolio_cost(file_path_bad_data))
