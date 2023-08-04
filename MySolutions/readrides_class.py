import csv


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
    
    def __repr__(self) -> str:
        return f"Row(route={self.route}, date={self.date}, daytype={self.daytype}, rides={self.rides})"


def read_rides(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            r = Row(
                route = row[0],
                date = row[1],
                daytype = row[2],
                rides = int(row[3])
            )
            records.append(r)
    return records


def to_mb(bytes_):
    return round(bytes_ / 1024 / 1024, 1)


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides('../Data/ctabus.csv')
    current, peak = tracemalloc.get_traced_memory()
    # print('Memory Use: Current %d, Peak %d' % (current, peak))
    print(f'Memory Use in MB: Current {to_mb(current)} Mb, Peak {to_mb(peak)} Mb')
