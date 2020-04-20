import math

#
#
# Need to add retaining wall calculation.
# Instructions: The brick retaining wall is one brick deep and 3 bricks tall. 
# It covers half of the circumference of the sand trap. Each brick is 12 inches long. 
#
#


# Find course area in yards
def get_course_area(course_length, course_width):
    length = int(course_length)
    width = int(course_width)
    area = length * width
    return area

# Use formula pi*r^2 to find circular area then multiply by two for putting green and teebox
def get_area_of_smooth_sod(course_width, pi):
    width = int(course_width)
    pi = float(pi)
    radius = width / 4
    area = pi * radius ** 2 * 2
    return area

# Use formula pi*r^2 to find circular area of sand trap
def get_area_of_sand_trap(course_width, pi):
    width = int(course_width)
    pi = float(pi)
    radius = width / 6
    area = pi * radius ** 2
    return area

#def get_number_of_retaining_wall_bricks(course_width, pi):
#perimeter_in_yards = get_perimeter_of_sand_trap / 2
                                               
# Calculate the course perimeter, 2L + 2W = P
def get_course_perimeter(course_length, course_width):
    length = int(course_length)
    width = int(course_width)
    perimeter = length * 2 + width * 2
    return perimeter

#smooth mowing time is 1 sec per square yard, find smooth sod area
def get_smooth_mowing_time(area_of_smooth_sod):
    mowing_time = int(area_of_smooth_sod)
    return mowing_time 
    
#rough mowing time is 0.5 secs per square yard, find rough sod area and multiply by 0.5, leave as float
def get_rough_mowing_time(course_area, area_of_smooth_sod):
    total_area = int(course_area)
    green_and_teebox = float(area_of_smooth_sod)
    rough_sod_mowing_area = total_area - green_and_teebox
    mowing_time = rough_sod_mowing_area * 0.5
    return mowing_time

# Convert seconds to minutes
def convert_secs_to_minutes(total_mowing_time_in_secs):
    seconds = float(total_mowing_time_in_secs)
    exact_mins = seconds / 60
    return exact_mins

# List inputs:

course_length = input("Course length: ")
course_width = input("Course width: ")
pi = 3.14159

# Area of golf course in square yards
course_area = int(get_course_area(course_length, course_width))

# Area of smooth sod in square yards
area_of_smooth_sod = float(get_area_of_smooth_sod(course_width, pi))

# Area of sand trap in square yards
area_of_sand_trap = float(get_area_of_sand_trap(course_width, pi))

# Number of bricks required for retaining wall
#BRICKS    
    
# Course perimeter in yards
course_perimeter = get_course_perimeter

# Rounded rough sod area string statement
rough_sod_area_calculation = str(round(course_area - area_of_smooth_sod - area_of_sand_trap))

                                                # Smooth_sod string statement
smooth_sod_area_calculation = str(math.ceil(area_of_smooth_sod))

                                                # sand trap area * 9 to convert to feet and multiply by height in feet, then divide by 2000 to find tons, then round up to whole number
sand_required_calculation = str(math.ceil((area_of_sand_trap * 9 * 100 / 2000)))

                                                # Bricks statement again????
#retaining_wall_bricks_required = str(get_number_of_retaining_wall_bricks * 4)

#Find course perimeter then subtract 2 for the entry and exit points, 1 bush for every 1 yard
number_of_bushes_calculation = (get_course_perimeter(course_length, course_width) - 2)

#Find smooth and rough mowing times in secs, divide by 60 and round up to find time in mins
smooth_mowing_calculation = float(get_smooth_mowing_time(area_of_smooth_sod))
rough_mowing_calculation = float(get_rough_mowing_time(course_area, area_of_smooth_sod))
mowing_time_calculation = smooth_mowing_calculation + rough_mowing_calculation
total_mowing_time_in_mins = math.ceil((mowing_time_calculation) / 60)
            
print("Total square yards of rough sod: " + str(rough_sod_area_calculation))           # Total square yards of rough sod: 152
print("Total square yards of smooth sod: " + str(smooth_sod_area_calculation))         # Total square yards of smooth sod: 40
print("Tons of sand: " + str(sand_required_calculation))                               # Tons of sand: 4
#print("Number of retaining wall bricks: " + str(retaining_wall_bricks_required))      # Number of retaining wall bricks: 48
print("Number of bushes: " + str(number_of_bushes_calculation))      # Number of bushes: 58
print("Total Mowing Time (mins): " + str(total_mowing_time_in_mins))                   # Total Mowing Time (mins): 2
