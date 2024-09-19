#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Opdracht PROG: NS-Functies
(c) 2024 Hogeschool Utrecht,
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
"""


def standaardprijs(distance):
    # If the number given is less than 0 than default to 0
    if distance < 0:
        distance = 0
    
    # Check if the distance is greater than 50km and calculate accordingly
    if distance > 50:
        price = 15 + (distance * 0.60)
    else:
        price = distance * 0.80

    # Return the calculated price of the travel
    return price


def ritprijs(age, weekend, distance):
    # Calculate standard price before performing any of the other calculations
    standardPrice = standaardprijs(distance)

    # Check if the travelers age is between 11 and 65 years in and calculate their price accordingly
    if age >= 12 and age < 65:
        # Check if it's weekend and return the correct price
        if weekend:
            return standardPrice * 0.6

        return standardPrice
    # If the travelers age is below 12 or 65 perform these calculations
    else:
        # Check if it's weekend and return the correct price
        if weekend:
            return standardPrice * 0.65
        
        return standardPrice * 0.7


def development_code():
    # Plaats hieronder code om je functies tussentijds te testen. Bijv:
    print("development printout:", standaardprijs(30))


def module_runner():
    development_code()      # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()           # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_assert_args(function, args, expected_output, check_type=False):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    if str(expected_output) == str(output):
        msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
              f"in plaats van {expected_output} (type {type(expected_output).__name__})"
    else:
        msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"

    if type(expected_output) is float and isinstance(output, (int, float, complex)):
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_standaardprijs():
    case = collections.namedtuple('case', 'distance expected_output')

    testcases = [ case(-51, 0), case(-10, 0), case(0, 0), case(10,8),
                  case(49, 39.2), case(50, 40), case(51, 45.6), case(80, 63) ]

    for test in testcases:
        __my_assert_args(standaardprijs, (test.distance,), test.expected_output)


def test_ritprijs():
    case = collections.namedtuple('case', 'age weekend distance expected_output')

    testcases = [ case(11, True,  50, 26.0),  case(11, False,  50, 28.0), case(11, True,  51, 29.64),
                  case(11, False, 51, 31.92), case(11, True, -51,  0.0),  case(11, False, -51,  0.0),
                  case(12, True,  50, 24.0),  case(12, False, 50, 40.0),  case(12, True,  51, 27.36),
                  case(12, False, 51, 45.6),  case(12, True, -51,  0.0),  case(12, False, -51, 0.0),
                  case(64, True,  50, 24.0),  case(64, False,  50, 40.0), case(64, True,  51, 27.36),
                  case(64, False, 51, 45.6),  case(64, True, -51,  0.0),  case(64, False, -51,  0.0),
                  case(65, True,  50, 26.0),  case(65, False, 50, 28.0),  case(65, True,  51, 29.64),
                  case(65, False, 51, 31.92) ]

    for test in testcases:
        __my_assert_args(ritprijs, (test.age, test.weekend, test.distance), test.expected_output)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_standaardprijs, test_ritprijs ]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()