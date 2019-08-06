print("Mad libs where libs get Mad")
print("Start Below:")

time = input("Insert a time of day: ")
items = input("Insert items (plural): ")
name = input("Insert a name: ")
scream = input("Scream something: ")
action = input("Insert an action: ")

print("It was " + str(time) + " o'clock when I heard a knock at the door.")
print("I opened the door and there was a box full of " + items + " with a note saying \"From Mr." + name.title() + '.\"')
print('Just as I closed the door I heard a scream "' + scream.upper() +'!"')
print("I froze in place and all I could do was " + action + '.')