from patterns import Patterns
def print_menu():
    print('Welcome to Game of life')
    print('------------------------')
    print("Please Enter the number of the pattern that you want")
    print("1. Blinker")
    print("2. Toad")
    print("3. Beacon")


if __name__ == '__main__':
    print_menu()
    choice = raw_input()
    if (choice == '1'):
        Patterns.blinker().draw_matrix_forever()
    elif (choice == '2'):
        Patterns.toad().draw_matrix_forever()
    elif (choice == '3'):
        Patterns.beacon().draw_matrix_forever()
    else:
        print('bye...')
