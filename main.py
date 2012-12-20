from patterns import Patterns

def print_menu():
    print 'Welcome to Game of life'
    print '------------------------'
    print 'Please Enter the number of the pattern that you want'
    print '1. Blinker'
    print '2. Toad'
    print '3. Beacon'


def draw_selected_pattern_forever(choice):
        if (choice == 1):
            Patterns.blinker().draw_matrix_forever()
        elif (choice == 2):
            Patterns.toad().draw_matrix_forever()
        elif (choice == 3):
            Patterns.beacon().draw_matrix_forever()
        else:
            raise ValueError("there is no suitable pattern for the given number")


if __name__ == '__main__':
    try:
        print_menu()
        choice = int(raw_input())
        draw_selected_pattern_forever(choice)
        print('bye...')
        sys.exit()
    except KeyboardInterrupt:
        print('bye...')
        sys.exit()

