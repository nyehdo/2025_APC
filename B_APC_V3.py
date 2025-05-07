from datetime import date
from tabulate import tabulate
import pandas
import math


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1, exit_code="xxx"):
    """checks that users enter the full word or the
    'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:
            if response == exit_code:
                return response
            # check if the response is the entire word
            elif response == item:
                return item

            # check if it's the 'n' letter
            elif response == item[:num_letters]:
                return item

        # makes the code look more neat and fixes grammar
        error = ' or '.join(', '.join(valid_answers).rsplit(', ', 1))
        print("Please choose either", error)


def int_check(question):
    """checks user enter an integer"""

    error = "Oops - please enter an integer"

    while True:
        response = input(question).lower()

        try:
            # change the response to an integer and check that it's more than zero
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''

Choose a shape (e.g. square / rectangle / triangle / circle)
Then choose whether you would like to calculate the area, perimeter or both.
After pick which unit of measurement you would like to use (e.g. mm / cm / m / km).

Based on your options, the system will ask for the dimensions required.
The system will loop until you enter the exit code ('xxx') and then output calculator history.
''')


def calculations(question):
    shape_list = ["square", "rectangle", "triangle", "circle"]
    function = ["area", "perimeter", "both"]
    unit_of_measurement = ["mm", "cm", "m", "km"]

    all_shapes = []
    all_dimensions = []
    all_results = []

    # expenses dictionary
    data = {
        "Shape": all_shapes,
        "Dimensions": all_dimensions,
        "Results": all_results
    }

    while True:
        measurements = ""
        area_answer = "valid"
        perimeter_answer = "valid"
        results = ""

        print()
        # find out what shape the user wants to calculate
        shape_option = string_check("Choose a Shape: ", shape_list, 1)
        if shape_option == "xxx":
            break

        # find out what the user wants to calculate (area or perimeter or both)
        function_option = string_check("What function would you like to use? ", function, 1)

        # find out what unit of measurement the user wants to use
        unit_of_measurement_option = string_check("What unit of measurement would you like to use: ",
                                                  unit_of_measurement,
                                                  2)
        # tells user what options they have picked
        if function_option == "both":
            user_chose = f"You chose to calculate the area and perimeter of a " \
                         f"{shape_option} in {unit_of_measurement_option}"
        else:
            user_chose = f"You chose to calculate the {function_option} of a {shape_option} " \
                         f"in {unit_of_measurement_option}"
        print(user_chose)
        print()

        # asking user measurements if they picked a square
        if shape_option == "square":
            length = int_check("Length: ")
            measurements = f"Length : {length}"
            # finding area
            if function_option != "perimeter":
                area_answer = length * length
            # finding perimeter
            if function_option != "area":
                perimeter_answer = length * 4

        # asking user measurements if they picked a rectangle
        elif shape_option == "rectangle":
            length = int_check("Length: ")
            width = int_check("Width: ")
            measurements = f"Length : {length} | Width : {width}"
            # finding area
            if function_option != "perimeter":
                area_answer = length * width
            # finding perimeter
            if function_option != "area":
                perimeter_answer = (length * 2) + (width * 2)

        # asking user measurements if they picked a triangle
        elif shape_option == "triangle":
            side_check = string_check("Do you have all sides of the triangle? ")
            if side_check == "yes":
                s1 = int_check("Side 1: ")
                s2 = int_check("Side 2: ")
                s3 = int_check("Side 3: ")
                if s1 + s2 < s3 or s2 + s3 < s1 or s3 + s1 < s2:
                    perimeter_answer = "invalid"
                    area_answer = "invalid"
                else:
                    # finding area
                    if function_option != "perimeter":
                        s = (s1 + s2 + s3) / 2
                        area_answer = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
                    # finding perimeter
                    if function_option != "area":
                        perimeter_answer = s1 + s2 + s3
                    measurements = f"S1 : {s1} | S2 : {s2} | S3 : {s3}"
            elif function_option == "perimeter":
                perimeter_answer = "invalid"
            else:
                base_height_check = string_check("Do you have the base and the height of the triangle? ")
                if base_height_check == "yes":
                    if shape_option != "perimeter":
                        base = int_check("Base: ")
                        height = int_check("Height: ")
                        measurements = f"Base : {base} | Height : {height}"
                        area_answer = base * height / 2
                    if shape_option != "area":
                        perimeter_answer = "invalid"
                else:
                    area_answer = "invalid"
                    perimeter_answer = "invalid"
        # asking user for measurements if they picked a circle
        else:
            radius = int_check("Radius: ")
            measurements = f"Radius : {radius}"
            # finding area
            if function_option != "perimeter":
                area_answer = (radius ** 2) * math.pi
            # finding perimeter
            if function_option != "area":
                perimeter_answer = radius * math.pi * 2

        # results if the user chose to calculate both
        if function_option == "both":
            # results when both answer cannot be found
            if area_answer == "invalid" and perimeter_answer == "invalid":
                results = f"The area cannot be found | " \
                          f"The perimeter cannot be found"
            # results if only perimeter can be found
            elif area_answer == "invalid":
                results = f"The area cannot be found | " \
                          f"The perimeter = {perimeter_answer:.2f}{unit_of_measurement_option}"
            # results if only area can be found
            elif perimeter_answer == "invalid":
                results = f"The area = {area_answer:.2f}{unit_of_measurement_option} | " \
                          f"The perimeter cannot be found"
            # results if both are found
            else:
                results = f"The area = {area_answer:.2f}{unit_of_measurement_option}^2 | " \
                          f"The perimeter = {perimeter_answer:.2f}{unit_of_measurement_option}"
        # results if user chose area
        if function_option == "area":
            if area_answer == "invalid":
                results = f"The area cannot be found"
            else:
                results = f" The area = {area_answer:.2f}{unit_of_measurement_option}^2"
        # results if user chose perimeter
        if function_option == "perimeter":
            if perimeter_answer == "invalid":
                results = f"The perimeter cannot be found"
            else:
                results = f" The perimeter = {perimeter_answer:.2f}{unit_of_measurement_option}"

        # appending shape and measurements to data
        all_shapes.append(shape_option)
        all_dimensions.append(measurements)
        all_results.append(results)
        print(results)

    # make panda
    frame = pandas.DataFrame(data)

    variable = tabulate(frame, headers=["Shape", "Dimensions", "Results"], tablefmt="psql", showindex=False)
    return variable


make_statement("Area Perimeter Calculator", "🔢")

# main routine goes here
print()
want_instructions = string_check("Do you want to see instructions? ")

if want_instructions == "yes":
    instructions()

get_calculations = calculations("")
print(get_calculations)

# *** get current date for heading and filename***
today = date.today()

# get day month and year
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

# heading for file
main_heading_string = f"Area Perimeter Calculator"

# write to file
to_write = [main_heading_string, "\n",
            get_calculations]

# create file to hold data (add .txt extension)
file_name = f"{main_heading_string}_{year}_{month}_{day}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
 