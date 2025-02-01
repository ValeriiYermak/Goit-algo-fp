"""
Завдання 7. Використання методу Монте-Карло
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на
кубиках, і визначає ймовірність кожної можливої суми.
Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на
обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи
ці дані, обчисліть імовірність кожної суми.
На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за
допомогою методу Монте-Карло.
Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці.
Висновки оформлено у вигляді файлу readme.md фінального завдання.
"""
import random
import matplotlib.pyplot as plt

# Function for simulating dice rolls
def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2,13)} # Dictionary to store the count of each sum

    for _ in range(num_rolls):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = dice1 + dice2
        sums_count[total] += 1
    return sums_count

# Function for calculate probability of each sum
def calculate_probabilities(sums_count, num_rolls):
    probabilities = {i: count / num_rolls for i, count in sums_count.items()}
    return probabilities

# Function for display results
def print_probabilities(probabilities):
    print("| The Sum  |  Probabilities (%)|")
    print("| -------- | ----------------- |")
    for total, prob in probabilities.items():
        sum_str = str(total).center(7)
        prob_str = f"{prob*100:.2f}%".center(12)
        print(f"|  {sum_str} |    {prob_str}   |")

# the function for display graph

def display_graph(probabilities):
    plt.bar(probabilities.keys(), probabilities.values(), color="skyblue")
    plt.xlabel("Sum")
    plt.ylabel("Probabilities (%)")
    plt.title("The probabilities of each sum for dice rolls (The Monte Carlo method)")
    plt.xticks(range(2,13))
    plt.show()

# Main program

if __name__ == "__main__":
    num_rolls = int(input("Enter the number of dice rolls: "))
    sums_count = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(sums_count, num_rolls)

    print_probabilities(probabilities)
    display_graph(probabilities)