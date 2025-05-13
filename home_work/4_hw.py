# ##Ex1
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         print (self.width * self.height)
#
#     def perimeter(self):
#         print (self.width*2 + 2*self.height)
#
# obj1 = Rectangle(7,8)
# obj1.area()
# obj1.perimeter()
#
# obj2 = Rectangle(2,5)
# obj2.area()
# obj2.perimeter()
#
# obj3 = Rectangle(1,3)
# obj3.area()
# obj3.perimeter()

##Ex2
# class Math:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         print (self.a + self.b)
#
#     def multiplication(self):
#         print (self.a * self.b)
#
#     def division(self):
#         print(self.a / self.b)
#
#     def subtraction(self):
#         print(self.a - self.b)
#
# abcd = Math(7, 17)
# abcd.addition()
# abcd.multiplication()
# abcd.division()
# abcd.subtraction()

##Ex3
# class Elements:
#
#     def __init__(self, text, type, loc):
#         self.text = text
#         self.type = type
#         self.loc = loc
#
#    def click(self):
#         return 'Клик по кнопке - {}'.format(self.text)
#
# Text_Box = Elements('Text Box','Кнопка','____')
# print('Текст кнопки ' + Text_Box.text + ', Тип ' + Text_Box.type + ', Локатор ' + Text_Box.loc)
# print(Text_Box.click())
#
# Check_Box = Elements('Check Box','Кнопка','____')
# print('Текст кнопки ' + Check_Box.text + ', Тип ' + Check_Box.type + ', Локатор ' + Check_Box.loc)
# print(Check_Box.click())
#
# Radio_Button = Elements('Radio Button','Кнопка','____')
# print('Текст кнопки ' + Radio_Button.text + ', Тип ' + Radio_Button.type + ', Локатор ' + Radio_Button.loc)
# print(Radio_Button.click())
#
# Web_Tables = Elements('Web Tables','Кнопка','____')
# print('Текст кнопки ' + Web_Tables.text + ', Тип ' + Web_Tables.type + ', Локатор ' + Web_Tables.loc)
# print(Web_Tables.click())
#
# Buttons = Elements('Buttons','Кнопка','____')
# print('Текст кнопки ' + Buttons.text + ', Тип ' + Buttons.type + ', Локатор ' + Buttons.loc)
# print(Buttons.click())
#
# Links = Elements('Links','Кнопка','____')
# print('Текст кнопки ' + Links.text + ', Тип ' + Links.type + ', Локатор ' + Links.loc)
# print(Links.click())
#
# Broken_Links = Elements('Broken Links','Кнопка','____')
# print('Текст кнопки ' + Broken_Links.text + ', Тип ' + Broken_Links.type + ', Локатор ' + Broken_Links.loc)
# print(Broken_Links.click())


## ex4
# class Car:
#
#     def __init__(self, color: str, type: str, year: int) -> str:
#         self.color = color
#         self.type = type
#         self.year = year
#
#     def caron(self):
#         print('Автомобиль заведен')
#
#     def caroff(self):
#         print('Автомобиль заглушен')
#
#     def caryear(self):
#         print(self.year)
#
#     def cartype(self):
#         print(self.type)
#
#     def carcolor(self):
#         print(self.color)
#
# car1 = Car("red", "sedan", 2015)
# car1.caron()
# car1.caroff()
# car1.caryear()
# car1.cartype()
# car1.carcolor()


