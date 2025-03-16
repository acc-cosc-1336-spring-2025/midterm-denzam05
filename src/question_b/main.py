#add import

from question_b import get_random_number

def main ():
    keep_going= 'y'
    while keep_going =='y' or keep_going =='Y':
        number= get_random_number()
        guess= int(input ('guess a number between 1 and 5'))

        if number == guess:
            print ('congratulations, that is the correct number')

        else:
            print (f'try again. the correct number was {number}')

        keep_going= input('would you like to keep going? y/n')

def  keep_guessing():
    keep_going='y'
    while keep_going =='y' or keep_going=="Y":
        number= get_random_number()
        guess= int(input ('guess a number between 1 and 5'))

        if number == guess:
            print ('congratulations, that is the correct number')

        else:
            print (f'try again. the correct number was {number}')
main()

        


        