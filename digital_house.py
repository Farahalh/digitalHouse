# Create a `House` class.
# The House class should have:

# * A variable for street address
# * A variable for address number
# * A variable for description
# * A variable containing a sequence of rooms
# * A function that returns the address number and description

class House:
    def __init__(self,
                 adress: str,
                 adress_number: int, 
                 description: str,
                 rooms: list[str]
                 ):
        self.adress = adress
        self.adress_number = adress_number
        self.description = description
        self.rooms = rooms

    def number_and_description(self):
        return f"{self.adress_number} - {self.description}."

my_house = House("Canary Drive", 45, "a nice house", ["Kitchen", "Bedroom", "Bathroom"])
print(my_house.number_and_description())

# Create a `Room` class.
# Room objects should have:

# * A variable for name
# * A variable for description
# * A variable containing a sequence of furniture
# * A function that returns the name and description

class Room:
    def __init__(self,
                 name: str,
                 description: str,
                 furniture: list[str]
                 ):
        self.name = name
        self.description = description
        self.furniture = furniture

    def name_and_description(self):
        return f"{self.name} - {self.description}."

my_room = Room("Kitchen", "Where I cook and eat", ["Table", "Four chairs", "Stove", "Sink"])
print(my_room.name_and_description())



# Create a `Furniture` class.
# Furniture objects should have:

# * A variable for name
# * A variable for description
# * A function that returns the name and description
# * A function that "uses" the furniture object


# Create an `InteractiveFurniture` class.
# Interactive furniture objects should have:

# * A variable for name
# * A variable for description
# * A variable for the description of the alternative state
# * A function that returns the name and description
# * A function that "uses" the furniture object

# When the function is used, the description variable and
# the alternative state description variable should switch.

# ## Furnishing a House
# Create:

# * At least 1 house object
# * At least 3 room objects and assign them to the house object's sequence of rooms
# * At least 6 furniture objects and assign them to the room object's sequence of furniture
# * At least 3 interactive furniture objects and assign
# them to the room object's sequence of furniture

# ## Menu
# The menu should allow the user to:

# * Get the description of a house object and its rooms
# * Get the description of a house object's room objects and their furniture
# * Get the description of a room object's furniture objects
# * Use a furniture object

# Use the menu to explore the house created above.

# ## Neighbour
# Use Git to share the project with group members.

# * Create a Git branch for each group member.
# * Each group member should complete the house furnishing task.
# * Where and how the code should be changed may only be communicated through self-documenting code.

# ## Tornado

# Import the `random` module.
# Create a tornado function that:

# * Collects all furniture
# * Randomly distributes the furniture between all rooms in all houses

# The menu should include an option to use the tornado function.
