import os

# Path of the directory
path = "."

# Print contents of the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)
