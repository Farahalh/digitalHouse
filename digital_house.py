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
        return f"I am using the {self.name} to {self.action}."


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

elif choice == "2":
    for room in my_house.rooms:
        print(room.name_and_description())

        for furniture in room.furniture:
            print(f"  {furniture.name_and_description()}")\

elif choice == "3":
    print("1. Kitchen")
    print("2. Bedroom")
    print("3. Living Room")

    room_choice = input("Choose a room: ")

    if room_choice == "1":
        selected_room = kitchen
    elif room_choice == "2":
        selected_room = bedroom
    elif room_choice == "3":
        selected_room = living_room
    else:
        print("Invalid choice.")
        selected_room = None

    if selected_room:
        print(selected_room.name_and_description())

        for furniture in selected_room.furniture:
            print(f"  {furniture.name_and_description()}")

elif choice == "4":
    print("1. Kitchen")
    print("2. Bedroom")
    print("3. Living Room")

    room_choice = input("Choose a room: ")

    if room_choice == "1":
        selected_room = kitchen
    elif room_choice == "2":
        selected_room = bedroom
    else:
        selected_room = living_room

    for number, furniture in enumerate(selected_room.furniture, 1):
        print(f"{number}. {furniture.name}")

    furniture_choice = int(input("Choose furniture: "))

    selected_furniture = selected_room.furniture[furniture_choice - 1]

    print(selected_furniture.use())

elif choice == "5":
    print("Goodbye!")


# ## Tornado

# Import the `random` module.
# Create a tornado function that:

# * Collects all furniture
# * Randomly distributes the furniture between all rooms in all houses

# The menu should include an option to use the tornado function.
