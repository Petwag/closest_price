from closest_price.loader import Loader
from closest_price.closest_price import the_price_is_right
def main():
    values = Loader.load_input()

    target = int(input("Choisissez un prix cible: "))

    print(the_price_is_right(values, target))

if __name__ == "__main__":
    main()
