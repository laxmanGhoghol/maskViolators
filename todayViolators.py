from dbconn import getViolatorsList

vlist = getViolatorsList()
print('\n-------------')
print('No. ID  Username')
print('--------------')
count = 0
for violator in vlist:
    print(count , violator)
    count += 1

print('\n-------------')

