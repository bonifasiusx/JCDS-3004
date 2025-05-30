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
    elif menu_options == '3':
        pass
        # Update Items
    elif menu_options == '4':
        pass
        # Remove Items
    else:
        print('\nInvalid option, please try again.')
    input('Press Enter to continue...')
    os.system(clear_command)
# End of CRUD Practice Session

    