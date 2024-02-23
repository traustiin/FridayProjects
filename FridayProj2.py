import random

def generate_powerball_numbers():
    # Initialize an empty list to store the Powerball numbers
    powerball_numbers = []

    # Generate 5 random numbers (white balls) in the range of 1 to 69 (inclusive)
    for _ in range(5):
        white_ball = random.randint(1, 69)
        powerball_numbers.append(white_ball)

    # Generate 1 random number (red ball, or Powerball) in the range of 1 to 26 (inclusive)
    powerball = random.randint(1, 26)
    powerball_numbers.append(powerball)

    return powerball_numbers

if __name__ == "__main__":
    # Call the function to generate Powerball numbers
    powerball_numbers = generate_powerball_numbers()

    # Print the generated Powerball numbers
    print("Generated Powerball numbers:")
    print(powerball_numbers)
