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


def calculations():
    # list for users to pick from
    shape_list = ["square", "rectangle", "triangle", "circle"]
    unit_of_measurement = ["mm", "cm", "m", "km"]

    # list to hold measurements and answers
    all_shapes = []
    all_dimensions = []
    all_area = []
    all_perimeter = []

    # expenses dictionary
    data = {
        "Shape": all_shapes,
        "Dimensions": all_dimensions,
        "Area": all_area,
        "Perimeter": all_perimeter
    }

    while True:
        measurements = ""

        print()
        # find out what shape the user wants to calculate
        shape_option = string_check("Choose a Shape: ", shape_list, 1)
        if shape_option == "xxx":
            break

        # find out what unit of measurement the user wants to use
        unit_of_measurement_option = string_check("What unit of measurement would you like to use: ",
                                                  unit_of_measurement,
                                                  2)
        print(f"You chose to calculate the area and perimeter of a {shape_option} in {unit_of_measurement_option}")
        print()

        # asking user measurements if they picked a rectangle or circle
        if shape_option == "rectangle" or shape_option == "square":
            length = int_check("Length: ")
            if shape_option == "square":
                width = length
            else:
                width = int_check("Width: ")
            measurements = f"Length : {length} | Width : {width}"
            # finding area and perimeter
            area_answer = length * width
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
                    s = (s1 + s2 + s3) / 2
                    area_answer = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
                    perimeter_answer = s1 + s2 + s3
                    measurements = f"S1 : {s1} | S2 : {s2} | S3 : {s3}"
            else:
                base_height_check = string_check("Do you have the base and the height of the triangle? ")
                if base_height_check == "yes":
                    base = int_check("Base: ")
                    height = int_check("Height: ")
                    measurements = f"Base : {base} | Height : {height}"
                    # finding area
                    area_answer = base * height / 2
                    perimeter_answer = "invalid"
                else:
                    area_answer = "invalid"
                    perimeter_answer = "invalid"
        # asking user for measurements if they picked a circle
        else:
            radius = int_check("Radius: ")
            measurements = f"Radius : {radius}"
            # finding area and perimeter
            area_answer = (radius ** 2) * math.pi
            perimeter_answer = radius * math.pi * 2

        # results
        if area_answer == "invalid":
            area_results = f"Cannot be found"
        else:
            area_results = f"{area_answer:.2f}{unit_of_measurement_option}^2"

        if perimeter_answer == "invalid":
            perimeter_results = f"Cannot be found"
        else:
            perimeter_results = f"{perimeter_answer:.2f}{unit_of_measurement_option}"

        # printing the results
        print(f"The area = {area_results}")
        print(f"The perimeter = {perimeter_results}")

        # appending shape and measurements to data
        all_shapes.append(shape_option)
        all_dimensions.append(measurements)
        all_area.append(area_results)
        all_perimeter.append(perimeter_results)

    # make panda
    frame = pandas.DataFrame(data)

    variable = tabulate(frame, headers=["Shape", "Dimensions", "Area", "Perimeter"], tablefmt="psql", showindex=False)
    return variable


make_statement("Area Perimeter Calculator", "🔢")

# main routine goes here
print()
want_instructions = string_check("Do you want to see instructions? ")

if want_instructions == "yes":
    instructions()

# calculator
get_calculations = calculations()
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
