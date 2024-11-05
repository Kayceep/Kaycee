# def sell(self):
#     return f"Selling Price: {self.__max_price}"

#     def set_max_price(self, price):
#       if price > self.__max_price:
#          self.__max_price = price

# # Object
# desktopObj = Desktop()
# print(desktopObj.sell()) 

# # modifying the price directly
# desktopObj.__max_price = 35000
# print(desktopObj.sell()) 

# # modifying the price using setter function
# desktopObj.set_max_price(35000)
# print(desktopObj.sell())        

class Cars:
    def __init__(self,  name, color, speed):
        self.name = name
        self.__color = color
        self.__speed = speed 

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color
    

ford = Cars("ford", "blue", "100kmph")
toyota = Cars("Toyota", "yellow", "50kmph")
kia = Cars("kia", "green","70kmph")


# print(ford.get_color())
# print(ford.speed)
print(kia.get_speed())
# toyota.color = "cyan"
# print(toyota.color)