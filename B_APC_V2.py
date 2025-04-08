# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


# functions go here
def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """checks that users enter the full word or the
    'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


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


def calculation():
    shape_list = ["square", "rectangle", "triangle", "circle"]
    function = ["area", "perimeter", "both"]
    unit_of_measurement = ["mm", "cm", "m", "km"]
    area_answer = ""
    perimeter_answer = ""
    while True:
        print()
        # find out what shape the user wants to calculate
        shape_option = string_check("Choose a Shape: ", shape_list, 1)

        # find out what the user wants to calculate (area or perimeter or both)
        function_option = string_check("What function would you like to use? ", function, 1)

        # find out what unit of measurement the user wants to use
        unit_of_measurement_option = string_check("What unit of measurement would you like to use: ",
                                                  unit_of_measurement,
                                                  2)
        # tells user what options they have picked
        if function_option == "both":
            print(f"You chose to calculate the area and perimeter of a {shape_option} in {unit_of_measurement_option}")
        else:
            print(f"You chose to calculate the {function_option} of a {shape_option} in {unit_of_measurement_option}")
        print()

        # asking user measurements if they picked a square
        if shape_option == "square":
            length = int_check("Length: ")
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
        # asking user for measurements if they picked a circle
        else:
            radius = int_check("Radius: ")
            # finding area
            if function_option != "perimeter":
                area_answer = radius * radius * 3.14
            # finding perimeter
            if function_option != "area":
                perimeter_answer = radius * 6.28

        # letting user know that this is an invalid triangle
        if perimeter_answer == "invalid":
            print(f"This is not a triangle")
            continue

        # print perimeter answer for user
        if function_option != "area":
            print(f"The perimeter = {perimeter_answer}{unit_of_measurement_option}")

        # print area answer for user
        if function_option != "perimeter":
            print(f"The area = {area_answer}{unit_of_measurement_option}^2")


make_statement("Area Perimeter Calculator", "🔢")

# main routine goes here
print()
want_instructions = string_check("Do you want to see instructions? ")

if want_instructions == "yes":
    instructions()

calculation()
