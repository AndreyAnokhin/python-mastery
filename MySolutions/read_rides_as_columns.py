import csv


def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


def to_mb(bytes_):
    return round(bytes_ / 1024 / 1024, 1)


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_columns('../Data/ctabus.csv')
    current, peak = tracemalloc.get_traced_memory()
    # print('Memory Use: Current %d, Peak %d' % (current, peak))
    print(f'Memory Use in MB: Current {to_mb(current)} Mb, Peak {to_mb(peak)} Mb')
