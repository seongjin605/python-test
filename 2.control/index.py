import pprint

c = 15 * 5
d = 15 + 15 + 15 + 15 + 15
print("c:", c)
print("d:", d)
if c > d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
elif c < d:
    print('c is less than d')
else:
    print('I don\'t know')

pprint.pprint(locals())

family = ['mother', 'father', 'gentleman', 'sexy lady']

for x in family:
    print('%s %d' % (x, len(x)))

result = list(range(2, 7))
print (result)