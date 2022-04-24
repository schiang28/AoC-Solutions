card_pk = 14082811
door_pk = 5249543
subject_number = 7
value = 1
card_ls = 0
door_ls = 0

while value != card_pk:
    value *= subject_number
    value = value % 20201227
    card_ls += 1

value = 1

while value != door_pk:
    value *= subject_number
    value = value % 20201227
    door_ls += 1

encryption_key = 1

for i in range(card_ls):
    encryption_key *= door_pk
    encryption_key = encryption_key % 20201227

print(card_ls, door_pk, encryption_key)
