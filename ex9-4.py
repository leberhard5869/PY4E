most_add = None
most_count = None
results = dict()

filename = input('Enter a file name:')
try:
  file = open(filename)
except:
  print('Could not open file: ', filename)
  quit()

for line in file:
  if line.startswith('From:'):
    words = line.split()
    print(words)
    results[words[1]] = results.get(words[1] , 0) + 1

for add,count in results():
  if most_count == None or count > most_count:
    most_add = add
    most_count = count
print(most_add, most_count)
