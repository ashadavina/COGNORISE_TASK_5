#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def roll_dice(num_sides, num_rolls):
    results = [random.randint(1, num_sides) for _ in range(num_rolls)]
    return results

def main():
    print("Welcome to the Dice Roller Simulator!")

    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice: "))
            num_rolls = int(input("Enter the number of rolls: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if num_sides <= 0 or num_rolls <= 0:
            print("Please enter positive values for the number of sides and rolls.")
            continue

        results = roll_dice(num_sides, num_rolls)

        print(f"\nResults of rolling a {num_sides}-sided dice {num_rolls} times:")
        for index, result in enumerate(results, start=1):
            print(f"Roll {index}: {result}")

        play_again = input("\nDo you want to roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for rolling! Goodbye!")
            break

if __name__ == "__main__":
    main()


# In[ ]:




