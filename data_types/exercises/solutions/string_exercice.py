
python_string = "hello world"

# Capitalize the python_string variable but not using capitalize function. Find the index of "h" and "w" and change it
# to "H" and "W"

indexH = python_string.find("h")
python_string[indexH] = "H"

indexW = python_string.find("w")
python_string[indexW] = "W"

print(python_string)

python_string = "hello world"

python_string[python_string.find("h")] = "H"
python_string[python_string.find("w")] = "W"

print(python_string)
