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


make_statement("Area Perimeter Calculator", "🔢")

print()
want_instructions = string_check("Do you want to see instructions? ")

if want_instructions == "yes":
    instructions()

print()

shape_list = ["square", "rectangle", "triangle", "circle"]
function = ["area", "perimeter", "both"]
unit_of_measurement = ["mm", "cm", "m", "km"]
answer = ""
area_answer = ""
perimeter_answer = ""

while True:

    shape_option = string_check("Choose a Shape: ", shape_list, 1)
    function_option = string_check("What function would you like to use? ", function, 1)
    unit_of_measurement_option = string_check("What unit of measurement would you like to use: ", unit_of_measurement,
                                              2)
    if function_option == "both":
        print(f"You chose to calculate the area and perimeter of a {shape_option} in {unit_of_measurement_option}")
    else:
        print(f"You chose to calculate the {function_option} of a {shape_option} in {unit_of_measurement_option}")
    print()

    if shape_option == "square":
        length = int_check("Length: ")
        if function_option == "area":
            answer = length * length
        elif function_option == "perimeter":
            answer = length * 4
        else:
            area_answer = length * length
            perimeter_answer = length * 4

    elif shape_option == "rectangle":
        length = int_check("Length: ")
        width = int_check("Width: ")
        if function_option == "area":
            answer = length * width
        elif function_option == "perimeter":
            answer = (length * 2) + (width * 2)
        else:
            area_answer = length * width
            perimeter_answer = length + length + width + width

    elif shape_option == "triangle":
        if function_option == "perimeter":
            s1 = int_check("Side 1: ")
            s2 = int_check("Side 2: ")
            s3 = int_check("Side 3: ")
            answer = s1 + s2 + s3
        elif function_option == "area":
            base = int_check("Base: ")
            height = int_check("Height: ")
            answer = base * height / 2
        else:
            base = int_check("Base: ")
            height = int_check("Height: ")
            s1 = int_check("Side 1: ")
            s2 = int_check("Side 2: ")
            s3 = int_check("Side 3: ")
            perimeter_answer = s1 + s2 + s3
            area_answer = base * height / 2

    else:
        radius = int_check("Radius: ")
        if function_option == "area":
            answer = radius * radius * 3.14
        elif function_option == "perimeter":
            answer = radius * 6.28
        else:
            area_answer = (radius ** 2) * 3.14
            perimeter_answer = radius * 6.28

    if function_option == "area":
        print(f"The area = {answer}{unit_of_measurement_option}^2")
    elif function_option == "perimeter":
        print(f"The perimeter = {answer}{unit_of_measurement_option}")
    else:
        print(f"The area = {area_answer}{unit_of_measurement_option}^2")
        print(f"The perimeter = {perimeter_answer}{unit_of_measurement_option}")

    print()
