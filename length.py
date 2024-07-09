#only the most basic conversions are added here, with further conversions daisy
#chained as needed from the main program

#we will start with the easiest/most elementary conversions. in metric, this
#means converting everything to/from meters, while for imperial this will be 
#inches. because converting between most metric lengths is just an adjustment
#to orders of magnitude, one function call aims to resolve this by simply
#adding or slicing off 0s until we have everything in our base unit, meters

def magnitude(orders, total):
    positive = True #this flag will tell us if the loop should increment or
    #decrement towards 0
    answer = total
    iterator = orders 
    if (orders < 0):
        positive = False
    while (iterator != 0):
        if (positive == True):
            iterator-= 1
            answer *= 10
        else:
            iterator += 1
            answer /= 10
    return answer


