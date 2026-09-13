user_name = input("Enter your name: ")

with open("name.txt", " w") as file:
    	 file.write (user_name)

print("Name saved successfully.")
