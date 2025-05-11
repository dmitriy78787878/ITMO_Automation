##EX1
# class Button:
#
#     type: #str = 'Кнопка'
#
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
# # Создаем экземпляры класса
# home = Button('Домой', 'home')
# catalog_msk = Button('Каталог', '/msk/catalog')
#
# # Получаем доступ к атрибутам
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)
# print('\n')
# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

#EX2
class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return 'Клик по локатору - {}'.format(self.loc)


# Создаем экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button2home')

# Вызываем метод
print(home_two.click())


#EX3
# class Input:
#
#     def __init__(self, loc, text):
#         self.loc = loc
#         self.text = text
#
# class Button:
#
#     def __init__(self, loc, text):
#         self.loc = loc
#         self.text = text
#
# class Title:
#
#     def __init__(self, loc, text):
#         self.loc = loc
#         self.text = text
#
# class Link:
#
#     def __init__(self, loc, text):
#         self.loc = loc
#         self.text = text
#
# search = Input('inputsearch', 'req')
# home = Button('Домой', ' home')
# abcd = Link('12345', ' 77777')
#
# print(search.loc)
# print(search.loc + search.text)
# print(home.loc + home.text)
# print(abcd.loc + abcd.text)


#EX4
# class Page:
#
#     def __init__(self, url):
#         self.url = url
#
#     def get(self):
#         print(self.url)
#
# home = Page('https://demoga.com/')
# home.get()


# #EX5
# class Soda:
#
#     def __init__(self, ing = None):
#         self.ing = ing
#
#     def show_my_drink(self):
#         if self.ing:
#             print(f'Газировка и {self.ing}')
#
#         else:
#             print('Обычная газировка')
#
# drink1 = Soda()
# drink2 = Soda('Малина')
# drink1.show_my_drink()
# drink2.show_my_drink()

# #EX7
# class Mammal:
#     className = 'mlekopitay'
#
# class Dog(Mammal):
#     species = 'Canis'
#
# dog = Dog()
# print(dog.className)



