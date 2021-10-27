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

    match choice:
        case "1":
            print("////////////////////////////////////////")
            print("/                 CSV.                 /")
            print("////////////////////////////////////////")
            file_path = input("Choisiser le chemin d'accès du fichier: ")
            values = Loader.load_csv(file_path)
        case "2":
            print("////////////////////////////////////////")
            print("/              A la main.              /")
            print("////////////////////////////////////////")
            values = Loader.load_input()
        case _:
            print("Ce choix n'existe pas")
            return
    print()
    target = int(input("Choisissez un prix cible: "))
    best_choices, rest = the_price_is_right(values, target)

    print(
        f"La selection donnant le résultat le plus proche est {best_choices}.")
    print(f"Avec cette selection, il reste a la fin {rest}.")


if __name__ == "__main__":
    main()
