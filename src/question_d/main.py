#add import

import question_d

def main():
    quit_program = False
    while not quit_program:
        get_day_ =input ('enter a number 1 through 7, or type "exit" to exit:')
        if get_day_.lower()== 'exit':
            print ("exiting program...")
            quit_program= True

        elif get_day_.isdigit():
            user_number= int(get_day_)
            result= question_d.get_day_of_the_week (user_number)

            print (result)

main()