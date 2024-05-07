import re

def generator_numbers(text):
    pattern = r'\d+(\.\d+)?'
    for value in re.finditer(pattern, text):
        yield value.group()

def sum_profit(text, generator_numbers):
    numbers = [float(num) for num in generator_numbers(text)]
    total = sum(numbers)
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(total_income)