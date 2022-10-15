salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for current_money in range(months):
        current_money = spend - salary
        spend *= increase + 1
        need_money += current_money


# TODO Оформить решение

print(round(need_money))