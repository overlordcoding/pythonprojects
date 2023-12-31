print("Create Random User Profile Descriptions for OSINT Accounts")
print("PRESS 1 TO MAKE A RANDOM USER PROFILE")
interaction = input("Write your answer here: ")
if interaction == "1":
    import random

# Lists of possible profile details
interests = ['Travel', 'Photography', 'Food', 'Music', 'Fitness', 'Art', 'Fashion', 'Sports']
locations = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Berlin', 'Los Angeles', 'Dubai']
occupations = ['Software Engineer', 'Designer', 'Writer', 'Teacher', 'Marketing Specialist', 'Chef', 'Athlete']
quotes = [
    "Carpe Diem! Seize the day.",
    "Life is what happens when you're busy making other plans.",
    "In a world where you can be anything, be kind.",
    "Adventure awaits just outside your comfort zone.",
    "Follow your dreams and never look back.",
    "Believe you can and you're halfway there."
]

# Random name generator
def generate_random_name():
    first_names = ['John', 'Emily', 'Michael', 'Sophia', 'Daniel', 'Olivia', 'David', 'Emma']
    last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Lee', 'Walker', 'Clark', 'Anderson']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate a random user profile description
def generate_profile_description():
    name = generate_random_name()
    age = random.randint(20, 50)
    interest = random.choice(interests)
    location = random.choice(locations)
    occupation = random.choice(occupations)
    quote = random.choice(quotes)
    
    profile_description = f"Hi, I'm {name}! {age} years old. I'm passionate about {interest}. Based in {location}. {occupation} by profession. {quote}"
    
    return profile_description

# Example usage
profile_description = generate_profile_description()
print('Generated Profile Description:')
print(profile_description)