class House:
    def __init__(self,
                 adress: str,
                 adress_number: int, 
                 description: str,
                 rooms: list
                 ):
        self.adress = adress
        self.adress_number = adress_number
        self.description = description
        self.rooms = rooms

    def number_and_description(self):
        return f"{self.adress_number} - {self.description}."


class Room:
    def __init__(self,
                 name: str,
                 description: str,
                 furniture: list
                 ):
        self.name = name
        self.description = description
        self.furniture = furniture

    def name_and_description(self):
        return f"{self.name} - {self.description}."


class Furniture:
    def __init__(self,
                 name:str,
                 description: str,
                 action: str
                 ):
        self.name = name
        self.description = description
        self.action = action

    def name_and_description(self):
        return f"{self.name} - {self.description}."

    def use(self):
        return f"I am using the {self.name} for {self.action}."


class InteractiveFurniture:
    def __init__(self,
                 name: str,
                 description: str,
                 alternate_state: str,
                 action: str
                 ):
        self.name = name
        self.description = description
        self.alternate_state = alternate_state
        self.action = action

    def name_and_description(self):
        return f"{self.name} - {self.description}."

    def use(self):
        self.description, self.alternate_state = (
            self.alternate_state,
            self.description
        )
        return f"I am using the {self.name} to {self.action}."


# Create 3 room objects
kitchen = Room(
    "Kitchen",
    "Where I cook and eat",
    []
)

bedroom = Room(
    "Bedroom",
    "Where I sleep",
    []
)

living_room = Room(
    "Living Room",
    "Where I relax",
    []
)


# Create 1 house object
# and assign the 3 rooms to it
my_house = House(
    "Canary Drive", 
    45,
    "a nice house", 
    [kitchen, bedroom, living_room]
)


# Create 6 furniture objects
table = Furniture(
    "Table",
    "A place to eat",
    "eat a meal"
)

chair = Furniture(
    "Chair",
    "A seat for sitting",
    "sit down"
)

bed = Furniture(
    "Bed",
    "A place to sleep",
    "sleep"
)

wardrobe = Furniture(
    "Wardrobe",
    "A place to store clothes",
    "store clothes"
)

sofa = Furniture(
    "Sofa",
    "A comfortable place to sit",
    "relax"
)

bookshelf = Furniture(
    "Bookshelf",
    "A place to store books",
    "read a book"
)


# Assign the 6 furniture objects to rooms
kitchen.furniture = [
    table,
    chair
]

bedroom.furniture = [
    bed,
    wardrobe
]

living_room.furniture = [
    sofa,
    bookshelf
]


# Create 3 interactive furniture objects
blender = InteractiveFurniture(
    "Blender",
    "Blends food and liquids",
    "Hard to clean after use",
    "make a smoothie"
)

fridge = InteractiveFurniture(
    "Fridge",
    "Keeps food cold",
    "The door is open",
    "get some food"
)

lamp = InteractiveFurniture(
    "Lamp",
    "Provides light",
    "The light is on",
    "turn on the light"
)

# Assign the 3 interactive furniture objects to rooms
kitchen.furniture.append(blender)
bedroom.furniture.append(fridge)
living_room.furniture.append(lamp)


print("\n=== DIGITAL HOUSE ===")
print("1. Get house and room descriptions")
print("2. Get rooms and furniture")
print("3. Get furniture in a room")
print("4. Use furniture")
print("5. Exit")

choice = input("Choose an option: ")

if choice == "1":
    print(my_house.number_and_description())

    for room in my_house.rooms:
        print(room.name_and_description())

elif choice == "5":
    print("Goodbye!")

# ## Menu
# The menu should allow the user to:

# * Get the description of a house object and its rooms
# * Get the description of a house object's room objects and their furniture
# * Get the description of a room object's furniture objects
# * Use a furniture object

# Use the menu to explore the house created above.


# ## Tornado

# Import the `random` module.
# Create a tornado function that:

# * Collects all furniture
# * Randomly distributes the furniture between all rooms in all houses

# The menu should include an option to use the tornado function.
