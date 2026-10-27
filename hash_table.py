
class Contact:
    """Store a contact's name and phone number."""

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    """A node in a linked list used for collision handling."""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """A hash table that stores contacts using separate chaining."""

    def __init__(self, size):
        if size <= 0:
            raise ValueError("Hash table size must be positive.")

        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        """Convert a string key into an array index."""
        return sum(ord(character) for character in key) % self.size

    def insert(self, key, value):
        """Insert a contact or update an existing contact's number."""
        if not isinstance(key, str):
            raise TypeError("Contact name must be a string.")

        if isinstance(value, Contact):
            contact = Contact(key, value.number)
        else:
            contact = Contact(key, str(value))

        index = self.hash_function(key)
        current = self.data[index]

        # Update an existing contact if its name already exists.
        while current is not None:
            if current.key == key:
                current.value = contact
                return
            current = current.next

        # Add a new node to the front of the linked list.
        new_node = Node(key, contact)
        new_node.next = self.data[index]
        self.data[index] = new_node

    def search(self, key):
        """Return the matching Contact or None if it is not found."""
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        """Print every index and its stored contacts."""
        for index in range(self.size):
            current = self.data[index]

            if current is None:
                print(f"Index {index}: Empty")
                continue

            print(f"Index {index}:", end=" ")
            while current is not None:
                print(f"- {current.value}", end=" ")
                current = current.next
            print()


if __name__ == "__main__":
    table = HashTable(10)

    print("Initial table:")
    table.print_table()

    print("\nInserting contacts...")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")

    print("\nUpdated table:")
    table.print_table()

    print("\nSearch result:", table.search("John"))

    # Test duplicate names: Rebecca's number should be updated.
    table.insert("Rebecca", "999-444-9999")
    print("Updated Rebecca:", table.search("Rebecca"))

    # Test a contact that does not exist.
    print("Missing contact:", table.search("Chris"))

    # Confirm that two contacts can share the same index.
    print(
        "Amy and May share an index:",
        table.hash_function("Amy") == table.hash_function("May")
    )
