filename = input("Enter a file name:")
try:
  file = open(filename)
except:
  print("Could not open file, quitting.")
  quit()
for line in file:
  print(line.upper().rstrip())