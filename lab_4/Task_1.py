inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}

print("\n Original Inventory",inventory)


inventory.update({
    "smartphone":inventory["Smartphone"]+10,
    "Headphone":inventory["Headphones"]+5
})

print("\nUpdated Inventory",inventory)

sold_item=inventory.popitem()
print("sold item : ",sold_item)

camera_stock=inventory.get("camera","Out Of stock")
print("Camera",camera_stock)