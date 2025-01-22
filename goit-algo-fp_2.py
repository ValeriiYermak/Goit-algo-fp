"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії:

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має
візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""

import turtle
import time


def pythagoras_tree(branch_lenght, level, angle):
    if level == 0 or branch_lenght < 5:
        return

    # Draw the trunk
    turtle.forward(branch_lenght)

    # Save the current position and heading
    position = turtle.pos()
    heading = turtle.heading()

    # Draw the right branch

    turtle.left(angle)
    pythagoras_tree(branch_lenght * 0.7, level - 1, angle)

    # Return to trunk's end position

    turtle.setpos(position)
    turtle.setheading(heading)

    # Draw the left branch
    turtle.right(angle)
    pythagoras_tree(branch_lenght * 0.7, level - 1, angle)

    # Return to the base of the trunk
    turtle.setpos(position)
    turtle.setheading(heading)


def main():
    # Ask user for the recursion depth
    level = int(input("Enter the recursion depth (e.g., 8): "))

    # Setup turtle environment
    turtle.speed("fastest")
    turtle.left(90)  # Start pointing upwards
    turtle.up()
    turtle.goto(0, -200)  # Start near the bottom of the screen
    turtle.down()

    # Measure the time for drawing
    start_time = time.time()

    # Draw the Pythagoras tree
    pythagoras_tree(100, level, 45)

    # Calculate and display time
    finished_time = time.time() - start_time
    print(f"Tame taken to draw the tree: {finished_time:.6f} seconds")

    # Wait for the user to close the window

    turtle.done()


if __name__ == "__main__":
    main()
