Instructions for MadLib Project.

def madlib(): - Defines a function named madlib which will contain the code for the MadLib game.
adjective = input("Enter an adjective: ") - Prompts the user to enter an adjective and stores the input in the variable adjective.
large_objects_plural = input("Enter a plural noun for large objects: ") - Prompts the user to enter a plural noun for large objects and stores the input in the variable large_objects_plural.
Similar lines of code collect input for other parts of speech required for the MadLib story.
Story construction using f-strings: Combines the user inputs with the fixed parts of the story to create the complete MadLib story stored in the variable story.
print("\nHere's your MadLib story:") - Prints a message indicating that the MadLib story is about to be displayed.
print(story) - Prints out the completed MadLib story.
if __name__ == "__main__": - Checks if the script is being run directly (not imported as a module).
madlib() - Calls the madlib function to start the MadLib game when the script is run.


Instructions for Powerball Project. 
import random: This imports the random module, which provides functions for generating random numbers.
def generate_powerball_numbers():: Defines a function named generate_powerball_numbers() to generate the list of Powerball numbers.
powerball_numbers = []: Initializes an empty list powerball_numbers to store the Powerball numbers.
Generating 5 white ball numbers:
for _ in range(5):: Initiates a loop to generate 5 random numbers (white balls).
white_ball = random.randint(1, 69): Generates a random integer between 1 and 69 (inclusive) and stores it in white_ball.
powerball_numbers.append(white_ball): Appends the generated white ball number to the powerball_numbers list.
Generating 1 red ball (Powerball):
powerball = random.randint(1, 26): Generates a random integer between 1 and 26 (inclusive) for the red ball (Powerball).
powerball_numbers.append(powerball): Appends the generated Powerball number to the powerball_numbers list.
return powerball_numbers: Returns the list of generated Powerball numbers.
if __name__ == "__main__":: Checks if the script is being run directly.
powerball_numbers = generate_powerball_numbers(): Calls the generate_powerball_numbers() function to generate the Powerball numbers and stores the result in the variable powerball_numbers.
print("Generated Powerball numbers:"): Prints a message indicating the list of generated Powerball numbers is about to be displayed.
print(powerball_numbers): Prints out the generated Powerball numbers.

Instructions for QuizBowl
