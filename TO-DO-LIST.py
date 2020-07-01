user_input = 'random'
data=[]

def show_menu():
    print('Menu')
    print('1:Add item')
    print('2:Mark as done')
    print('3:View the to-do list')
    print('4:Exit')

while user_input != '4':

    show_menu()
    user_input = input('Enter your choice: ')

    if user_input == '1':
        item = input('Add your choice: ')
        data.append(item)
        print('Added item:',item)
    elif user_input == '2':
        item = input('What is to be marked as done..')
        if item in data:
            data.remove(item)
            print('Remove item:',item)
        else:
            print('The choice is not exist')
    elif user_input == '3':
        print('List of to-do items are:')
        for item in data:
            print(item)
    elif user_input == '4':
        print('Goodbye')
    else:
        print('Enter your choice from 1,2,3 or 4')
