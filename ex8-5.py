count = 0
filename = input('Enter a file name:')
try:
  file = open(filename)
except:
  print('Could not open file: ', filename)
  quit()
for line in file:
  if line.startswith('From:'):
    words = line.split()
    print(words[1].rstrip())
    count = count + 1
print('There were', count, 'lines in the file with From: as the first word')