# Practice Session --> Membuat CRUD Rungkad's Store
import os

match os.name:
    case 'nt':
        clear_command = 'cls'
    case 'posix':
        clear_command = 'clear'

title = "WELCOME TO RUNGKAD'S STORE"
symbol = '*' * len(title)

print(symbol)
print(title)
print(symbol)
print()

menu = '''
[1] Add Items
[2] Show Items
[3] Update Items
[4] Remove Items
    
[0] Exit              
'''

while True:
    print(menu)
    menu_options = input('\nPlease select menu: ')
    if not menu_options.isdigit() or int(menu_options) < 0 or int(menu_options) > 4:
        print('Invalid input, please try again.')
        continue
    os.system(clear_command)
    if menu_options == '0':
        print('Exiting the program. Goodbye!')
        break
    if menu_options == '1':
        try:
            with open('rungkad.txt', encoding='utf-8', mode='a') as file:
                print()
                name = input('Enter item: ').title()
                category = input('Category: ').title()
                price = int(input('Enter price: '))
                stock = int(input('Enter stock: '))
                
                file.write(f'{name},{category},{price},{stock}\n')
                print(f'\nItem {name} added successfully.')
        except FileNotFoundError:
            print('Error: rungkad.txt file not found. Creating new file...')
            with open('rungkad.txt', encoding='utf-8', mode='w') as file:
                file.write(f'{name},{category},{price},{stock}\n')
                print(f'Item {name} added successfully.')
    elif menu_options == '2':
        try:
            with open('rungkad.txt', encoding='utf-8', mode='r') as file:
                items = file.readlines()
                if items:
                    print()
                    print('Items in Rungkad\'s Store:')
                    for item in items:
                        name, category, price, stock = item.strip().split(',')
                        print(f'Name: {name}, Category: {category}, Price: {price}, Stock: {stock}')
                else:
                    print('No items found.')
        except FileNotFoundError:
            print('Error: rungkad.txt file not found. Please add items first.')
    # Index masih start dari 0, perbaiki dan juga untuk estetika new lines
    elif menu_options == '3':
        # Update Items
        try:
            with open('rungkad.txt', encoding='utf-8', mode='r') as file:
                items = file.readlines()
                if not items:
                    print('No items to update.')
                    continue
                print()
                print('Items in Rungkad\'s Store:')
                for index, item in enumerate(items):
                    name, category, price, stock = item.strip().split(',')
                    print(f'[{index}] Name: {name}, Category: {category}, Price: {price}, Stock: {stock}')
                
                item_index = int(input('Enter the index of the item to update: '))
                if 0 <= item_index < len(items):
                    name = input('Enter new item name (leave blank to keep current): ').title() or items[item_index].split(',')[0]
                    category = input('Enter new category (leave blank to keep current): ').title() or items[item_index].split(',')[1]
                    price = input('Enter new price (leave blank to keep current): ')
                    stock = input('Enter new stock (leave blank to keep current): ')
                    
                    if price == '':
                        price = items[item_index].split(',')[2]
                    if stock == '':
                        stock = items[item_index].split(',')[3]
                    
                    items[item_index] = f'{name},{category},{price},{stock}\n'
                    
                    with open('rungkad.txt', encoding='utf-8', mode='w') as file:
                        file.writelines(items)
                    
                    print(f'Item at index {item_index} updated successfully.')
                else:
                    print('Invalid index.')
        except FileNotFoundError:
            print('Error: rungkad.txt file not found. Please add items first.')
    elif menu_options == '4':
        try:
            with open('rungkad.txt', encoding='utf-8', mode='r') as file:
                items = file.readlines()
                if not items:
                    print('No items to remove.')
                    continue
                print()
                print('Items in Rungkad\'s Store:')
                for index, item in enumerate(items):
                    name, category, price, stock = item.strip().split(',')
                    print(f'[{index}] Name: {name}, Category: {category}, Price: {price}, Stock: {stock}')

                item_index = int(input('Enter the index of the item to remove: '))
                if 0 <= item_index < len(items):
                    removed_item = items[item_index]
                    del items[item_index]

                    with open('rungkad.txt', encoding='utf-8', mode='w') as file:
                        file.writelines(items)

                    print(f'Item removed successfully: {removed_item.strip()}')
                else:
                    print('Invalid index.')
        except FileNotFoundError:
            print('Error: rungkad.txt file not found. Please add items first.')
    else:
        print('\nInvalid option, please try again.')
    input('Press Enter to continue...')
    os.system(clear_command)
# End of CRUD Practice Session

    