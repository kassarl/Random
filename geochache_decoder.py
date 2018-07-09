import string

dict = {' ' : ' '}

completed_values = []

for i in range(97, 123):
    if i not in completed_values:
        val = input("%c:" % chr(i))
        dict[chr(i)] = val
        dict[val] = chr(i)
        completed_values.append(i)
        completed_values.append(ord(val))
    

list_output = []
string = input("Write string here:")
string = string.lower()
for letter in string :
    list_output.append(dict[letter])

output_string = ''.join(list_output)
print(output_string)
