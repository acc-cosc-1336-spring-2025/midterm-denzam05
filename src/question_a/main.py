#add import

from question_a import get_miles_per_hour

def main ():
    
    kilometers= int (input ("enter the number of kilometers"))
    minutes= int (input ("enter the number of minutes"))

    result= get_miles_per_hour (kilometers, minutes)

    if result== 'invalid argument':
        print(result)
    else:
        print( "the speed is {result:.6} miles per hour")

main()     