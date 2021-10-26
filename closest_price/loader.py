class Loader:
    @staticmethod
    def load_csv(file_path):
        # Load csv file and fetch data
        pass

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
