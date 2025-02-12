text = 'banana'
char = 'b'

index = text.find(char)
list_index = [index]

while index != -1:
    index = text.find(char, index+1)
    list_index.append(index)
list_index.pop()

print(list_index)