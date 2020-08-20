most_add = None
most_count = None
results = dict()
lst = list()

filename = input('Enter a file name:')
try:
  file = open(filename)
except:
  print('Could not open file: ', filename)
  quit()

for line in file:
  if line.startswith('From:'):
    words = line.split()
    results[words[1]] = results.get(words[1] , 0) + 1

for k,v in results.items():
  newtup = v,k
  lst.append(newtup)

lst = sorted(lst, reverse=True)
for v,k in lst[:1]:
  print(k, v)