print("Create Random Usernames for OSINT Accounts.")
print("PRESS 1 TO MAKE A RANDOM USERNAME")
interaction = input("Write your answer here: ")
if interaction == "1":
    import random
import string

# Function to generate a random username
def generate_username():
    adjectives = ['happy', 'sunny', 'daring', 'brave', 'curious', 'clever', 'vivid', 'cool', 'silly', 'witty']
    nouns = ['unicorn', 'wizard', 'adventure', 'hero', 'dreamer', 'jester', 'artist', 'rebel', 'champion', 'voyager']
    numbers = random.randint(10, 99)
    username = random.choice(adjectives) + random.choice(nouns) + str(numbers)
    return username

# Example usage
username = generate_username()
print('Generated Username:', username)