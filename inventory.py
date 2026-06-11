def add_inventory():

    item = input(
        "Item Name: "
    )

    quantity = int(
        input("Quantity: ")
    )

    file = open(
        "inventory.txt",
        "a"
    )

    file.write(
        item + "," +
        str(quantity) + "\n"
    )

    file.close()

    print(
        "Inventory Added"
    )

def view_inventory():

    file = open(
        "inventory.txt",
        "r"
    )

    print()

    print("INVENTORY")

    for line in file:

        print(
            line.strip()
        )

    file.close()