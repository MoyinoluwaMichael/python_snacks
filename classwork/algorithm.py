acre_to_inch = 6272640
gallon_in_inch = 0.004329
gallon_in_acre = acre_to_inch*gallon_in_inch

inch = float(input("Enter the volume of rain on an acre in inch(es): "))
result_in_gallons = inch * gallon_in_acre

print("The total number of gallons found in an acre is:",result_in_gallons)