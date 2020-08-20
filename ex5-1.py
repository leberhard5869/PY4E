sum = 0
count = 0
while True:
  num = input("Enter a number: ")
  if num == 'done':
    break
  try:
    fl_num = float(num)
  except:
    print("Invalid Input")
    continue
  sum = sum + fl_num
  count = count + 1
print(sum, count, sum / count)