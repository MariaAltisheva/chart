
list_of_id = []

with open('facebook.txt', 'r') as file:
    for line in file:
        list_of_id.append(line[32:].strip())

list_of_id_2 = []
for i in list_of_id:
    list_of_id_2.append(i.strip('/'))

# print(list_of_id_2)

with open('new.txt', 'w', encoding='utf-8') as file:
    for i in list_of_id_2:
        file.write(i + '\n')
