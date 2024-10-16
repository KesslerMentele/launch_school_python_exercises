'''
Full Description:
Write a function that takes a floating point number representing an angle
between 0 and 360 degrees and returns a string representing that angle in
degrees, minutes, and seconds. You should use a degree symbol (°) to represent
degrees, a single quote (') to represent minutes, and a double quote (") to
represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.




What about values >= 360 or < 0?

Can I assume all inputs are floats?

What about sub-second precision?

Input: floating point number
Output: string
Rules:
    Explicit Requirements:
    - Use the degree symbol to represent degrees
    - Use ' to represent minutes
    - Use " to represent seconds
    Implicit Requirements:
    - input of 360 can return "360°00'00\"" or  "0°00'00\""

Algorithm:
    - Create an int that is the whole number of the input called degrees
    - Create a float that is equal to 60 * the remainder from degrees called minutes
    - Create a float that is equal to 60 * the remainder from minutes called seconds
    - return a string with the values concatenated and the appropriate symbols between

use int() coercion to get the whole number

subtract the degrees from the input, multiply by 60 then coerce to int for minutes

repeat that process for seconds


Further Exploration:

Just mod degrees by 360 before printing

'''
DEGREE = "\u00B0"

def dms(input_degrees:float)->str:
    degrees = int(input_degrees)
    input_degrees -= degrees
    input_degrees = 60 * input_degrees
    minutes = int(input_degrees)
    input_degrees -= minutes
    input_degrees = 60 * input_degrees
    seconds = int(input_degrees)
    return f'{degrees % 360}{DEGREE}{str(minutes).zfill(2)}\'{str(seconds).zfill(2)}\"'




# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1) == "359°00'00\"")
print(dms(400) == "40°00'00\"")
print(dms(-40) == "320°00'00\"")
print(dms(-420) == "300°00'00\"")