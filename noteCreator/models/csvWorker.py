import csv

class CsvWorker:
    def save_to_csv(self, notes):
        with open("data.csv", 'w') as f:
            for note in notes:
                f.write(str(note) + '\n')

    def read_csv(self):
        data = []
        with open("data.csv", 'r') as f:
            reader = csv.reader(f, delimiter='\n')
            for row in reader:
                data.append(row)
        return data