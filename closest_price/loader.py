import csv


class Loader:
    @staticmethod
    def load_csv(file_path, delimiter=" "):
        # Load csv file and fetch data
        with open(file_path, newline="") as csv_file:
            spamreader = csv.reader(csv_file, delimiter=delimiter)
            return [int(row[0]) for row in spamreader]

    @staticmethod
    def load_input():
        # Ask for inputs untils an empty input is sent
        data = []

        while True:
            print(f"valeurs actuelles {data}")
            value = input("Ajoutez une valeur (valeur vide pour quitter): ")
            if not value:
                break
            data.append(int(value))

        return data
