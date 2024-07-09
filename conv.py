#!/usr/bin/python3

import sys
import temperature
import length
import invalid
from decimal import *

#the following is to handle help
try:
    sys.argv[1]
except:
    invalid.print_command_help()
    sys.exit(0)

try:
    argument = float(sys.argv[3])
except:
    if (sys.argv[1].lower() == "help"):        
        if (sys.argv[2].lower() == "temp"):    
            invalid.print_temp_help()          
        elif (sys.argv[2].lower() == "length"):
            invalid.print_length_help()        
        elif (sys.argv[2].lower() == "units"):
            invalid.print_units_help()
        elif (sys.argv[2].lower() == "metric"):
            invalid.print_metric_help()
        elif (sys.argv[2].lower() == "lengths"):
            invalid.print_lengths_help()
        else:                                  
            invalid.print_command_help()       
    else:                                      
        invalid.print_command_help()           

##the following function calls do temperature conversion
if (sys.argv[1].lower() == "temp"):
    if (sys.argv[2].lower() == "c2f"):
        print(temperature.c2f(argument))
    elif(sys.argv[2].lower() == "f2c"):
        print(temperature.f2c(argument))
    elif(sys.argv[2].lower() == "r2f"):
        print(temperature.r2f(argument))
    elif(sys.argv[2].lower() == "f2r"):
        print(temperature.f2r(argument))
    elif(sys.argv[2].lower() == "c2k"):
        print(temperature.c2k(argument))
    elif(sys.argv[2].lower() == "k2c"):
        print(temperature.k2c(argument))
    elif(sys.argv[2].lower() == "r2c"):
        print(temperature.f2c(temperature.r2f(argument)))
    elif(sys.argv[2].lower() == "c2r"):
        print(temperature.f2r(temperature.c2f(argument)))
    elif(sys.argv[2].lower() == "k2f"):
        print(temperature.c2f(temperature.k2c(argument)))
    elif(sys.argv[2].lower() == "f2k"):
        print(temperature.c2k(temperature.f2c(argument)))
    elif(sys.argv[2].lower() == "r2k"):
        print(temperature.c2k(temperature.f2c(temperature.r2f(argument))))
    elif(sys.argv[2].lower() == "k2r"):
        print(temperature.f2r(temperature.c2f(temperature.k2c(argument))))
    else:
        invalid.print_temperature_help() 
#the following function calls do length conversion
if (sys.argv[1].lower() == "length"):        
    #this portion will convert any metric length to meters by moving the
    #decimal point an appropriate number of digits to the left or right
    #of 0 via the  magnitude function. see the table at the bottom of
    #this file for conversions. some of the conversions require capitals
    #as such we will not be calling the lower() method
    if(sys.argv[2] == "ym"):
        print(length.magnitude(-24, argument))
    elif(sys.argv[2] == "zm"):
        print(length.magnitude(-21, argument))
    elif(sys.argv[2] == "am"):
        print(length.magnitude(-18, argument))
    elif(sys.argv[2] == "fm"):
        print(length.magnitude(-15, argument))
    elif(sys.argv[2] == "pm"):
        print(length.magnitude(-12, argument))
    elif(sys.argv[2] == "nm"):
        print(length.magnitude(-9, argument))
    elif(sys.argv[2] == "μm"):
        print(length.magnitude(-6, argument))
    elif(sys.argv[2] == "mm"):
        print(length.magnitude(-3, argument))
    elif(sys.argv[2] == "cm"):
        print(length.magnitude(-2, argument))
    elif(sys.argv[2] == "dm"):
        print(length.magnitude(-1, argument))
    elif(sys.argv[2] == "dam"):
        print(length.magnitude(1, argument))
    elif(sys.argv[2] == "hm"):
        print(length.magnitude(2, argument))
    elif(sys.argv[2] == "km"):
        print(length.magnitude(3, argument))
    elif(sys.argv[2] == "Mm"):
        print(length.magnitude(6, argument))
    elif(sys.argv[2] == "Gm"):
        print(length.magnitude(9, argument))
    elif(sys.argv[2] == "Tm"):
        print(length.magnitude(12, argument))
    elif(sys.argv[2] == "Pm"):
        print(length.magnitude(15, argument))
    elif(sys.argv[2] == "Em"):
        print(length.magnitude(18, argument))
    elif(sys.argv[2] == "Zm"):
        print(length.magnitude(21, argument))
    elif(sys.argv[2] == "Ym"):
        print(length.magnitude(24, argument))
    elif(sys.argv[2] == "Rm"):
        print(length.magnitude(27, argument))
    else:
        invalid.print_length_help()

#metric converstions in orders of magnitude, numbers below will convert
#to meters by multiplying the input by n, where n is the number of
#orders of magnitude away from meters that given measurement is

#yoctometer -24
#zeptometer -21
#attometer -18
#femtometer -15
#picometer -12
#nanometer -9
#micrometer -6
#millimeter -3
#centimeter -2
#decimeter -1
#meter 0
#decameter 1
#hecometer 2
#kilometer 3
#megameter 6
#gigameter 9
#terameter 12
#petameter 15
#exameter 18
#zettameter 21
#yottameter 24
#ronnameter 27
