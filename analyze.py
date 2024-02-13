import csv

def average_temperature_anomaly(decade_data):
    total_anomaly = 0
    count = 0
    for row in decade_data:
        for value in row[1:13]:
            if value != '***' and value != '****' and value != '*****':
                total_anomaly += float(value)
                count += 1
    if count != 0:
        return total_anomaly / count
    else:
        return 0

def main():
    with open('data/clean_data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        data = list(reader)

    start_year = 1880
    end_year = 2024
    decade_start = start_year
    while decade_start < end_year:
        decade_end = decade_start + 9
        decade_data = [row[1:-1] for row in data if decade_start <= int(row[-1]) <= decade_end]
        avg_anomaly = average_temperature_anomaly(decade_data)
        print(f"Average temperature anomaly for {decade_start} to {decade_end}: {avg_anomaly:.2f} °F")
        decade_start += 10

if __name__ == "__main__":
    main()


