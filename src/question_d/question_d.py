#write functions here, don't add input('') statements here!

def get_day_of_the_week (day):
    if 1<= day <=7:

        if (day == 1):
            result= ' monday'
            return result
        
        elif (day ==2):
            result= ' tuesday'
            return result
        
        elif (day ==3):
            result= ' wednesday'
            return result
         
        elif (day ==4):
            result= ' thursday'
            return result
        
        elif (day ==5):
            result= ' friday'
            return result
         
        elif (day ==6):
            result= ' saturday'
            return result
        
        elif (day ==7):
            result= ' sunday'
            return result
        
    else:
        return 'invalid number'