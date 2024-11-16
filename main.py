# Task 10.3
'''def is_even(digit):
    return digit % 2 == 0
user_input = int(input("Введіть ціле число: "))
if is_even(user_input):
    print(f"Число {user_input} є парним.")
else:
    print(f"Число {user_input} є непарним.")'''
#task 10.2
'''def first_word(text):
    text = text.strip("., ")
    words = text.split()
    for word in words:
        word = word.strip("., ")
        return word

user_input = input("Введіть текст: ")
print("Перше слово:", first_word(user_input))'''
#task 10.1
'''def sequence_generator(rule_func, first_value, n):
    current_value = first_value
    for _ in range(n):
        yield current_value
        current_value = rule_func(current_value)
def next_term(x):
    return x + 2
gen = sequence_generator(next_term, first_value=1, n=5)
for num in gen:
    print(num)'''
#task 11.3
'''def is_even(number):
    return (number & 1) == 0'''
# task 11.2
'''def generate_cube_numbers(end):
    number = 2
    while True:
        cube = number ** 3
        if cube > end:
            return  
        yield cube 
        number += 1
end_limit = int(input("Введіть верхню межу: "))
print(f"Куби чисел до {end_limit}:")
for cube in generate_cube_numbers(end_limit):
    print(cube)'''
#task 11.1
def prime_generator(limit):
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            yield num





