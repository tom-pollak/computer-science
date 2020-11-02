import math

STONES_TO_POUNDS = 14
POUNDS_TO_KG = 0.453592


def convert_to_metric():
    stones = int(input('Enter number of stones: '))
    pounds = int(input('Enter number of pounds: '))

    weight_pounds = (STONES_TO_POUNDS * stones) + pounds
    weight_kg = POUNDS_TO_KG * weight_pounds

    print('Your weight is: %skg' % weight_kg)


def convert_to_imperial():
    kg = float(input('Enter number of kilograms: '))
    weight_pounds = (1 / POUNDS_TO_KG) * kg
    stones = math.floor((1 / STONES_TO_POUNDS) * weight_pounds)
    pounds = math.floor(weight_pounds % (stones * STONES_TO_POUNDS))
    print('Your approximate weight is %s stone and %s pounds' %
          (stones, pounds))


def calc_order_cost():
    kg_bananas = float(input('Enter number of kilos of bananas: '))
    cost = 3 * kg_bananas + 4.99
    if cost > 50:
        cost -= 1.5
    print('Cost of order: £%s' % (math.floor(cost * 100) / 100))


def calc_training():
    age = int(input('Enter age: '))
    rate = int(input('Enter training heart rate: '))
    m = 208 - 0.7 * age
    if rate >= 0.9 * m:
        zone = 'Interval training'
    elif 0.7 * m <= rate < 0.9 * m:
        zone = 'Threshold training'
    elif 0.5 * m <= rate < 0.7 * m:
        zone = 'Aerobic training'
    else:
        zone = 'Couch potato'
    print('Your zone is: %s' % zone)


def herons_formula():
    a = int(input('Enter first side of the triangle\'s length: '))
    b = int(input('Enter second side of the triangle\'s length: '))
    c = int(input('Enter third side of the triangle\'s length: '))
    s = (a + b + c) / 2
    A = math.sqrt(s * ((s - a) * (s - b) * (s - c)))
    print('The area of the triangle is: %s' % A)


convert_to_metric()
convert_to_imperial()
calc_order_cost()
calc_training()
herons_formula()
