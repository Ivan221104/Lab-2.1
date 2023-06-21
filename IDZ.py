candy_price = float(input("Введите стоимость 1 кг конфет: "))
cookie_price = float(input("Введите стоимость 1 кг печенья: "))
apple_price = float(input("Введите стоимость 1 кг яблок: "))

candy_weight = float(input("Введите количество кг конфет: "))
cookie_weight = float(input("Введите количество кг печенья: "))
apple_weight = float(input("Введите количество кг яблок: "))

total_cost = candy_price*candy_weight + cookie_price*cookie_weight + apple_price*apple_weight

print("Стоимость всей покупки составляет:", total_cost)