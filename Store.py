import random
from typing import List


class Product:
    def __init__(self, id, name, price, rating):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__rating = rating

    @property
    def id(self): return self.__id

    @property
    def name(self): return self.__name

    @property
    def price(self): return self.__price

    @property
    def rating(self): return self.__rating


class Category:
    def __init__(self, id, name, products: List[Product] = []):
        self.__id = id
        self.__name = name
        self.__products = products

    @property
    def id(self): return self.__id

    @property
    def name(self): return self.__name

    @property
    def products(self): return self.__products


class Basket:
    def __init__(self, goods: List[Product] = []):
        self.__goods = goods

    @property
    def goods(self): return self.__goods


class User:
    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password
        self.__basket = Basket()

    @property
    def name(self): return self.__name

    @property
    def basket(self): return self.__basket

    def check_credentials(self, login, password):
        if self.__login == login and self.__password == password:
            return True
        else:
            return False


def init_products_categories():
    products_equipments = [Product(0, "Дрель", random.randint(100, 10000), random.randint(0, 10)),
                           Product(1, "Шуруповерт", random.randint(100, 10000), random.randint(0, 10)),
                           Product(2, "Сверло", random.randint(100, 10000), random.randint(0, 10)),
                           Product(3, "Отвертка", random.randint(100, 10000), random.randint(0, 10)),
                           Product(4, "Генератор", random.randint(100, 10000), random.randint(0, 10)),
                           Product(5, "Верстак", random.randint(100, 10000), random.randint(0, 10)),
                           Product(6, "Рулетка", random.randint(100, 10000), random.randint(0, 10)),
                           Product(7, "Тиски", random.randint(100, 10000), random.randint(0, 10)),
                           Product(8, "Шпатель", random.randint(100, 10000), random.randint(0, 10)),
                           Product(9, "Сварочный аппарат", random.randint(100, 10000), random.randint(0, 10))]

    product_hardware = [Product(0, "Саморез", random.randint(100, 10000), random.randint(0, 10)),
                        Product(1, "Дюбель", random.randint(100, 10000), random.randint(0, 10)),
                        Product(2, "Уголок", random.randint(100, 10000), random.randint(0, 10)),
                        Product(3, "Хомут", random.randint(100, 10000), random.randint(0, 10)),
                        Product(4, "Стропа", random.randint(100, 10000), random.randint(0, 10)),
                        Product(5, "Металлический профиль", random.randint(100, 10000), random.randint(0, 10)),
                        Product(6, "Крючок", random.randint(100, 10000), random.randint(0, 10)),
                        Product(7, "Петля дверная", random.randint(100, 10000), random.randint(0, 10)),
                        Product(8, "Замок почтовый", random.randint(100, 10000), random.randint(0, 10)),
                        Product(9, "Стропа", random.randint(100, 10000), random.randint(0, 10))]

    product_floor_coverings = [Product(0, "Ламинат", random.randint(100, 10000), random.randint(0, 10)),
                               Product(1, "Линолеум", random.randint(100, 10000), random.randint(0, 10)),
                               Product(2, "ПВХ-плитка", random.randint(100, 10000), random.randint(0, 10)),
                               Product(3, "Плинтус", random.randint(100, 10000), random.randint(0, 10)),
                               Product(4, "Порожек", random.randint(100, 10000), random.randint(0, 10)),
                               Product(5, "обвод для труб", random.randint(100, 10000), random.randint(0, 10)),
                               Product(6, "Подложка", random.randint(100, 10000), random.randint(0, 10)),
                               Product(7, "Клей", random.randint(100, 10000), random.randint(0, 10)),
                               Product(8, "Ковролин", random.randint(100, 10000), random.randint(0, 10)),
                               Product(9, "Доска", random.randint(100, 10000), random.randint(0, 10))]

    product_electrical_goods = [Product(0, "Обогреватель", random.randint(100, 10000), random.randint(0, 10)),
                                Product(1, "Тепловая пушка", random.randint(100, 10000), random.randint(0, 10)),
                                Product(2, "Розетка", random.randint(100, 10000), random.randint(0, 10)),
                                Product(3, "Выключатель", random.randint(100, 10000), random.randint(0, 10)),
                                Product(4, "Силовой кабель", random.randint(100, 10000), random.randint(0, 10)),
                                Product(5, "Мультиметр", random.randint(100, 10000), random.randint(0, 10)),
                                Product(6, "УЗО", random.randint(100, 10000), random.randint(0, 10)),
                                Product(7, "Вентилятор", random.randint(100, 10000), random.randint(0, 10)),
                                Product(8, "Удлинитель", random.randint(100, 10000), random.randint(0, 10)),
                                Product(9, "Сетевой фильтр", random.randint(100, 10000), random.randint(0, 10))]

    product_paints = [Product(0, "Краска для стен", random.randint(100, 10000), random.randint(0, 10)),
                      Product(1, "Краска для потолка", random.randint(100, 10000), random.randint(0, 10)),
                      Product(2, "Лак", random.randint(100, 10000), random.randint(0, 10)),
                      Product(3, "Эмаль", random.randint(100, 10000), random.randint(0, 10)),
                      Product(4, "Аэрозольная краска", random.randint(100, 10000), random.randint(0, 10)),
                      Product(5, "Штукатурка", random.randint(100, 10000), random.randint(0, 10)),
                      Product(6, "Антисептик для дерева", random.randint(100, 10000), random.randint(0, 10)),
                      Product(7, "Грунтовка", random.randint(100, 10000), random.randint(0, 10)),
                      Product(8, "Кисть", random.randint(100, 10000), random.randint(0, 10)),
                      Product(9, "Валик", random.randint(100, 10000), random.randint(0, 10))]

    return [Category(0, "Инструменты", products_equipments),
            Category(1, "Скобяные изделия", product_hardware),
            Category(2, "Напольные покрытия", product_floor_coverings),
            Category(3, "Электротовары", product_electrical_goods),
            Category(4, "Краски", product_paints)]


def init_users():
    return [User("Bob", "user", "pass"),
            User("Dylan", "user2", "pass2")]


if __name__ == '__main__':
    def check_credentials(login, password):
        for user in users:
            if user.check_credentials(login, password):
                return user

    def validate_selected_item(input_value: str, expected_list_size: int):
        try:
            int_value = int(input_value)
            if int_value >= 0 and int_value < expected_list_size:
                return int_value
            else:
                print("\nWrong value entered\n")
        except:
            print("\nInvalid value entered\n")

    def show_categories():
        print("List of categories:")
        for category in categories:
            print(f"[{category.id}] - {category.name}")

    def show_products(category: Category):
        print("List of products:")
        for product in category.products:
            print(f"[{product.id}] - {product.name}, \tprice: {product.price}, \trating: {product.rating}")

    def show_basket(user: User):
        print("\nYour purchases:")
        for product in user.basket.goods:
            print(f"[{product.id}] - {product.name}, \tprice: {product.price}, \trating: {product.rating}")

    users = init_users()
    categories = init_products_categories()
    exit_flag = False

    login = input("Enter login: ")
    password = input("Enter password: ")
    user = check_credentials(login, password)
    if user is None:
        print("Wrong login or password")
        exit(1)
    else:
        user_name = user.name
        print(f"Welcome, {user_name}!")

    while not exit_flag:
        show_categories()

        category_id = validate_selected_item(input("Select a category: "), len(categories))
        if category_id is None:
            continue

        show_products(categories[category_id])

        product_id = validate_selected_item(input("Select a product: "), len(categories[category_id].products))
        if product_id is None:
            continue

        user.basket.goods.append(categories[category_id].products[product_id])

        user_answer = input("\nContinue shopping(y/n): ")
        if user_answer != "y":
            exit_flag = True

    show_basket(user)
