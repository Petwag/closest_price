from closest_price.loader import Loader
from closest_price.closest_price import the_price_is_right


def main():
    print("////////////////////////////////////////")
    print("/            Choisi un mode            /")
    print("////////////////////////////////////////")
    print("1) Fichier CSV")
    print("2) A la main")
    print()
    choice = input("Ton choix: ")
    print()

    loader = Loader()

    match choice:
        case "1":
            print("////////////////////////////////////////")
            print("/                 CSV.                 /")
            print("////////////////////////////////////////")
            file_path = input("Choisiser le chemin d'accès du fichier: ")
            loader.load_csv(file_path)
        case "2":
            print("////////////////////////////////////////")
            print("/              A la main.              /")
            print("////////////////////////////////////////")

            # Ask for inputs untils an empty input is sent
            while True:
                print(f"valeurs actuelles {loader.values}")
                value = input(
                    "Ajoutez une valeur (valeur vide pour quitter): ")
                if not value:
                    break
                loader.load_input(float(value))
        case _:
            print("Ce choix n'existe pas")
            return
    print()
    target = int(input("Choisissez un prix cible: "))
    best_choices, rest = the_price_is_right(loader.values, target)

    print(
        f"La selection donnant le résultat le plus proche est {best_choices}.")
    print(f"Avec cette selection, il reste a la fin {rest}.")


if __name__ == "__main__":
    main()
