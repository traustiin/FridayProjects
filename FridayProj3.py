def quiz_bowl():
    score = 0  # Initialize score to keep track of correct answers

    # Question 1
    answer_1 = input("1. What's that thing that orbits the Earth? ")
    if answer_1.lower() == "moon":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 2
    print("2. TikTok is:")
    print("A) Waste of time")
    print("B) Stealing my data")
    print("C) Both")
    answer_2 = input("Enter your choice (A, B, or C): ")
    if answer_2.upper() == "B":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 3
    answer_3 = input("3. What kind of data type is 'hello world'? ")
    if answer_3.lower() == "string":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 4
    answer_4 = input("4. What has four wheels and moves? ")
    if answer_4.lower() == "car":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 5
    answer_5 = input("5. True or False: Coding is cool? ")
    if answer_5.lower() == "true":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Display final score
    print("\nYour final score is:", score)

if __name__ == "__main__":
    quiz_bowl()
