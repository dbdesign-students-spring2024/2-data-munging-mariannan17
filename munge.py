# Function to convert temperature change from Celsius to Fahrenheit
def celsius_change_to_fahrenheit(change_celsius):
    return format(change_celsius / 100 * 1.8, '.1f')  

# Clean data function
def clean_data(raw_data):
    cleaned_data = []
    data_started = False
    for line in raw_data:
        if line.startswith("Year"):
            data_started = True
            if not cleaned_data:
                cleaned_data.append(line.strip().split(','))
        elif data_started and line.strip():
            values = line.strip().split()
            try:
                year = int(values[0])
            except ValueError:
                continue
            if year > 2024:
                break
            converted_values = [value if i in (0, len(values) - 1) or value in ('****', '***', '*****') else celsius_change_to_fahrenheit(int(value))
                                for i, value in enumerate(values)]
            cleaned_data.append(converted_values)
    return cleaned_data

# Main method
def main():
    with open("data/readme.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

    cleaned_data = clean_data(raw_data)

    with open("data/clean_data.csv", "w", encoding="utf-8") as file:
        for row in cleaned_data:
            file.write(','.join(map(str, row)) + '\n')

if __name__ == "__main__":
    main()
