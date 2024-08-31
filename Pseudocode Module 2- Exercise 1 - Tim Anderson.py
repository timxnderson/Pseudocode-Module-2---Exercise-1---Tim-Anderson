'''
Author: Tim Anderson
Date: 8/30/2024
Version: 1.0
Program: helloUser.py 
'''
Start program
//input
Promp user to enter refrigerator model name
store use input in refrigeratorModelName

prompt user to enter interior height in inches
store user input in heightInches

prompt user to enter interior width in inches
store user input in widthInches

prompt user to enter interior depth in inches
store user input in depthInches

//process
set cubicInches = heightInches * widthInches * depthInches
set cubicFeet = cubicInches / 1728

//output
print "refrigerator model: " + refrigeratorModelName
print "capacity in cubic feet: " + cubicFeet

End program