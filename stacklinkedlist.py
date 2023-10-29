from SLLNC import SingleLinkedList

class StackLinkedList:

    #constructor inisialisasi single linked list non circular
    def __init__(self):
        self.stack_data = SingleLinkedList()

    def push(self, new_data):
        #untuk push cukup gunakan insert head
        self.stack_data.insertHead(new_data)

    def top(self):
        if self.stack_data.size == 0 :
            return None
        else:
            #ambil data di bagian head
            top_data = self.stack_data.head.data
            return top_data
        
    def pop(self):
        # cek apakah masih kosong?
        if self.stack_data.size == 0 :
            return None
        else:
            #ambil data di bagian head
            pop_data = self.top()

            #hapus head
            self.stack_data.delete_head()
            #return data di yg di pop
            return pop_data
        
    def clear(self):
        #hapus isi satu persatu
        while self.stack_data.size > 0 :
            self.pop()
        
    def print(self):
        # gunakan method print dari Single Linked list
        print(self.stack_data.print())

    # fungsi khusus supaya bisa dipakai dalam fungsi len()
    def __len__(self):
        return self.stack_data.size



if __name__ == '__main__':
    stack = StackLinkedList()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.print()
    print('Jumlah data dalam stack: ', len(stack))
            