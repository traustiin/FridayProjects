def madlib():
    adjective = input("Enter an adjective: ")
    large_objects_plural = input("Enter a plural noun for large objects: ")
    body_part = input("Enter a body part: ")
    restaurant = input("Enter a restaurant name: ")
    first_food = input("Enter a type of food: ")
    second_food = input("Enter another type of food: ")
    large_object_singular = input("Enter a singular noun for a large object: ")

    story = f"I've had a very {adjective} day. This morning, I dropped a box of {large_objects_plural} on my {body_part}. " \
            f"Then, at lunch, I went to {restaurant} for their delicious {first_food}. But the waiter brought me " \
            f"{second_food}, which I was not hungry for. Finally, on my way home, I was cut off by a van with a large " \
            f"{large_object_singular} strapped to the roof."

    print("\nHere's your MadLib story:")
    print(story)


if __name__ == "__main__":
    madlib()
