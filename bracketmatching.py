from stacklinkedlist import StackLinkedList

#definisikan tag opening dan closing
opening  = ['{', '[', '(', '<']
closing = ['}', ']', ')', '>']

bracket_dictionary = {'{':1,'}':1,'[':2,']':2,'(':3,')':3,'<':4,'>':4}

#input
input_string = input('Masukkan code berisi bracket: ')

# buat stack
stack = StackLinkedList()

matched = True

#cek satu-persatu karakter
for karakter in input_string:
    #jika opening bracket, push ke stack
    if karakter in opening:
        stack.push(karakter)
    #jika closing bracket, cek apakah berpasangan dengan yang ada
    elif karakter in closing:
        #jika memang sepasang bracket yang sesuai, pop dari stack
        if bracket_dictionary[karakter] == bracket_dictionary[stack.top()]:
            stack.pop()
        #jika tidak sama, maka bracket tidak valid
        else:
            matched = False
            break

# jika stack tidak kosong di akhir, maka tidak valid
if len(stack) > 0 :
    matched = False

if matched:
    print('Penggunaan bracket sudah sesuai')
else:
    print('Penggunaan bracket salah!!')