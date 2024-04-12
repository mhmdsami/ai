import random

def monty_hall(strategy):
    doors = ['A', 'B', 'C']
    car = random.choice(doors)
    guess = random.choice(doors)
    
    if strategy == 'stay':
        new_guess = guess
    elif strategy == 'switch':
        revealed_door = random.choice([door for door in doors if door != car and door != guess])
        new_guess = [door for door in doors if door != guess and door != revealed_door][0]
    else:
        raise ValueError("Invalid strategy. Please choose 'stay' or 'switch'.")
    
    if new_guess == car:
        return True
    else:
        return False

num_simulations = 1000
num_wins_stay = sum([monty_hall('stay') for _ in range(num_simulations)])
num_wins_switch = sum([monty_hall('switch') for _ in range(num_simulations)])

print(f"Number of wins (stay strategy): {num_wins_stay}")
print(f"Win percentage (stay strategy): {num_wins_stay / num_simulations * 100}%")

print(f"Number of wins (switch strategy): {num_wins_switch}")
print(f"Win percentage (switch strategy): {num_wins_switch / num_simulations * 100}%")
