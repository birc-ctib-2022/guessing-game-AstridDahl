# The following code is just to setup the exercise. You do not need to
# understand but can jump to the game below.


def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


print("Please think of a number from 1 to 20, both included.")
print("Let me know how good my guess is.\n")

# Here, we implement the computer's strategy for guessing
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.

for guess in range(1, 21):                                   # 5n+2
    result = input_selection(                                # 2n
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":                                      # 2
        print("Wuhuu!")                                      # 1
        break                                                # ?

    print("I must have been too low, right?", result)        # n-1

# best case: 12 operations. O(1)
# worst case: 128 operations. O(n)


for guess in range(21, 1, -1):
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break

    print("I must have been too high, right?", result)


# result = ""                 # 1
# lower_bound = 1             # 1
# upper_bound = 20            # 1

# while result!="hit":                                           # 2n
#     guess = (lower_bound + upper_bound) // 2                   # 3n
#     result = input_selection(                                  # 2n
#         "I'm guessing {}\nHow is my guess?".format(guess),
#         ["low", "hit", "high"]
#     )
#     if result == "hit":                                         # 2n
#         print("Wuhuu!")                                         # 1
#         break                                                   # 1

#     if result == "low":                                         # 2n-2
#         lower_bound = guess + 1                                 # 2n-2

#     if result == "high":                                        # 2n-2
#         upper_bound = guess - 1                                 # accounted for in if statement above

# best case: right on first guess, 13 operations
# worst case: right on 5th guess, 73. log_2(n) running time

