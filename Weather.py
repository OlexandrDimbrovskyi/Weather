import pyowm
from colorama import init, Fore, Back, Style

init()
i = 3

while i > 1:
    owm = pyowm.OWM('968583ed9f68bd1a435184a2b6bc01b7', language="ua")

    print(Fore.BLUE)

    place = input("В якому Місті/Країні: ")

    observation = owm.weather_at_place(place)
    w = observation.get_weather()

    temp = w.get_temperature('celsius')["temp"]

    print(Fore.CYAN)

    print("В місті " + place + " зараз " + w.get_detailed_status())

    print("Температура зараз в районі " + str(temp) + " градусів за цельсієм!")

    print(Fore.RED)

    if temp < 10:
        print("На вулиці холодно!")
    if temp < 20:
        print("Зараз холодно вдінься тепліше!")
    else:
        print("Температура норм,вдягайся як хочеш!")

    print(Fore.GREEN)
    exita = input("Ви бажаєте закінчити роботу Так/Ні: ")
    if exita == "Так":
        break
    elif exita == "Ні":
        print(Fore.WHITE)
        print("Продовжуємо роботу")
    else:
        print(Fore.LIGHTWHITE_EX)
        print("Капец ти хацкер,мені страшно!")
        break
