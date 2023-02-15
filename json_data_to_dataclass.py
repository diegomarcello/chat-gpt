import json
from dataclasses import dataclass

# Define the dataclass structure
@dataclass
class Person:
    name: str
    age: int
    email: str

# Load the JSON object from a file
with open('person.json', 'r') as file:
    json_str = file.read()

# Parse the JSON into a dictionary
data = json.loads(json_str)

# Create a Person dataclass object from the dictionary
person = Person(**data)

# Access the dataclass attributes
print(person.name)
print(person.age)
print(person.email)
