
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for character in key:
            total += ord(character)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                current.value.number = value
                return
            current = current.next

        contact = Contact(key, value)
        new_node = Node(key, contact)
        new_node.next = self.data[index]
        self.data[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            print(f"Index {index}:", end="")
            current = self.data[index]

            if current is None:
                print(" Empty")
            else:
                while current is not None:
                    print(f" - {current.value}", end="")
                    current = current.next
                print()


if __name__ == "__main__":
    table = HashTable(10)

    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")

    # Test updating an existing contact
    table.insert("Rebecca", "999-444-9999")

    # Print the table
    table.print_table()

    # Test searching
    print("\nSearch result:", table.search("John"))
    print("Updated contact:", table.search("Rebecca"))
    print("Missing contact:", table.search("Chris"))
