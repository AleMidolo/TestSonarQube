import csv


class CSVProcessor:

    def __init__(self):
        pass

    def read_csv(self, file_name):
        data = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            title = next(reader)
            for row in reader:
                data.append(row)
        return title, data

    def write_csv(self, data, file_name):
        try:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return 1
        except Exception as e:
            print(f"Error writing to file: {e}")
            return 0

    def process_csv_data(self, column_index, save_file_name):
        title, data = self.read_csv(save_file_name)
        processed_data = self.get_processed_column_data(data, column_index, title)
        return self.write_csv(processed_data, self.get_processed_file_name(save_file_name))

    def get_processed_column_data(self, data, column_index, title):
        column_data = [row[column_index].upper() for row in data]
        return [title, column_data]

    def get_processed_file_name(self, original_file_name):
        return f"{original_file_name.split('.')[0]}_process.csv"