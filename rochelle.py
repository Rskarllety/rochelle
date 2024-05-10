class ProductNode:
    def __init__(self, id, price, description):
        self.id = id
        self.price = price
        self.description = description
        self.next = None

class ProductList:
    def __init__(self):
        self.head = None

    def insert(self, id, price, description):
        new_node = ProductNode(id, price, description)
        if self.head is None or self.head.description > description:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.description < description:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def search(self, description):
        current = self.head
        while current is not None:
            if current.description == description:
                return current
            current = current.next
        return None

    def remove(self, description):
        current = self.head
        previous = None
        while current is not None:
            if current.description == description:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(f"ID: {current.id}, Price: {current.price}, Description: {current.description}")
            current = current.next

product_list = ProductList()

product_list.insert(1, 12.0, "Biscoito")
product_list.insert(2, 20.0, "Arroz")
product_list.insert(3, 4.0, "Macarrão")
product_list.insert(4, 3.0, "Leite")

print("Exibição original:")
product_list.display()

product_list.remove("Arroz")

print("\n\nNova exibição após a remoção:")
product_list.display()
''