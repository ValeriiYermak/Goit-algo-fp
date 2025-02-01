"""
Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного
програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви,
а значення — це словник з вартістю та калорійністю.
Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до
вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір
страв для максимізації калорійності при заданому бюджеті.
"""

# information about food
foods = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

#Greedy algorithm
def greedy_algorithm(foods, budget):
    # Sort the foods by cost
    sorted_foods = sorted(foods.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_foods = []

    for food_name, food_info in sorted_foods:
        if total_cost + food_info["cost"] <= budget:
            selected_foods.append(food_name)
            total_cost += food_info["cost"]
            total_calories += food_info["calories"]
    return selected_foods, total_calories


def dynamic_algorithm(foods, budget):
    # Create an array to store the maximum calories for each budget
    dp = [0] * (budget + 1)
    selected = [[] for _ in range(budget +1)]

    for current_budget in range(budget + 1):
        for food_name, food_info in foods.items():
            if food_info["cost"] <= current_budget:
                if dp[current_budget - food_info["cost"]] + food_info["calories"] > dp[current_budget]:
                    dp[current_budget] = dp[current_budget - food_info["cost"]] + food_info["calories"]
                    selected[current_budget] = selected[current_budget - food_info["cost"]] + [food_name]
    return selected[budget], dp[budget]


# The main function
def main():
    budget = 100 # Total budget

    # Greedy algorithm
    greedy_selected_foods, greedy_calories = greedy_algorithm(foods, budget)
    print("Greedy Algorithm Result:")
    print(f"Selected Foods: {greedy_selected_foods}")
    print(f"Total Calories: {greedy_calories}\n")

    # Dynamic algorithm
    dp_selected, dp_calories = dynamic_algorithm(foods, budget)
    print("\nDynamic Algorithm Result:")
    print(f"Selected foods: {dp_selected}")
    print(f"Total Calories: {dp_calories}")

if __name__ == "__main__":
    main()