from datetime import date
from tabulate import tabulate
import pandas


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


# functions go here
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
    area_answer = ""
    perimeter_answer = ""

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
        print()
        # find out what shape the user wants to calculate
        shape_option = string_check("Choose a Shape: ", shape_list, 1)
        if shape_option == "xxx":
            # end = "yes"
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
            user_chose = f"You chose to calculate the {function_option} of a {shape_option}" \
                         f"in {unit_of_measurement_option}"
        print(user_chose)

        # asking user measurements if they picked a square
        if shape_option == "square":
            length = int_check("Length: ")
            measurements = f"Length : {length}{unit_of_measurement_option}"
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
            measurements = f"Length : {length}{unit_of_measurement_option} | " \
                           f"Width : {width}{unit_of_measurement_option}" \
                # finding area
            if function_option != "perimeter":
                area_answer = length * width
            # finding perimeter
            if function_option != "area":
                perimeter_answer = (length * 2) + (width * 2)

        # asking user measurements if they picked a triangle
        elif shape_option == "triangle":
            # finding area
            if function_option != "perimeter":
                base = int_check("Base: ")
                height = int_check("Height: ")
                measurements = f"Base : {base}{unit_of_measurement_option} | " \
                               f"Height : {height}{unit_of_measurement_option}"
                area_answer = base * height / 2
            # finding perimeter
            if function_option != "area":
                s1 = int_check("Side 1: ")
                s2 = int_check("Side 2: ")
                s3 = int_check("Side 3: ")
                # checking to make sure this is a triangle
                if s1 + s2 < s3 or s2 + s3 < s1 or s3 + s1 < s2:
                    perimeter_answer = "invalid"
                else:
                    perimeter_answer = s1 + s2 + s3
                    measurements = f"S1 : {s1}{unit_of_measurement_option} | " \
                                   f"S2 : {s2}{unit_of_measurement_option} | " \
                                   f"S3 : {s3}{unit_of_measurement_option}"
        # asking user for measurements if they picked a circle
        else:
            radius = int_check("Radius: ")
            measurements = f"Radius : {radius}{unit_of_measurement_option}"
            # finding area
            if function_option != "perimeter":
                area_answer = (radius ** 2) * 3.14
            # finding perimeter
            if function_option != "area":
                perimeter_answer = radius * 6.28

        # letting user know that this is an invalid triangle
        if perimeter_answer == "invalid":
            print(f"This is not a triangle")
            continue

        # print perimeter answer for user
        if function_option == "perimeter":
            results = f"The perimeter = {perimeter_answer}{unit_of_measurement_option}"

        # print area answer for user
        elif function_option == "area":
            results = f"The area = {area_answer}{unit_of_measurement_option}^2"
        else:
            results = f"The perimeter = {perimeter_answer}{unit_of_measurement_option}" \
                      f" | The area = {area_answer}{unit_of_measurement_option}^2"

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

get_calculations = calculations("Start")
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
