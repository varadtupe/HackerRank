contacts = []
def find(search):
    matching = [s for s in contacts if search in s]
    print(len(matching))

def add(inp):
    contacts.append(inp)

n = int(input().strip())

for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add(contact)
    elif op == 'find':
        find(contact)




