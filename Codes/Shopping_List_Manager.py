shopping_list = []

while True:
    item = input("Enter an item (type 'done' to finish): ").strip()
    
    if item.lower() == 'done':
        break
    elif item == '':
        print("Please enter a valid item.")
    else:
        shopping_list.append(item)

print("\nShopping List:")
for item in shopping_list:
    print(f"- {item}")

print(f"\nTotal number of items: {len(shopping_list)}")
