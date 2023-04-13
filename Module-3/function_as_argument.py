def bonus():
    bonus=2000
    return bonus


def salary (b):
    basic_salary=30000
    Total_salary=b()+basic_salary
    print(Total_salary)

salary(bonus)