import urllib.request, urllib.parse, urllib.error

host = input('Enter URL host and file:')
try:
    req = urllib.request.urlopen(host)
except:
    print('Invalid host, quitting')
    quit()

char_count = 0
for line in req:
    char_count = char_count + len(line)
    if(char_count <=3000):
        print(line.decode().strip())
    else:
        break

print('Number of characters:', char_count)
