salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 1.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
delta = 0
i = 0
# TODO Оформить решение

while i < months:
    need_money = need_money + (spend - salary)
    spend *= increase
    i += 1

print(round(need_money))
