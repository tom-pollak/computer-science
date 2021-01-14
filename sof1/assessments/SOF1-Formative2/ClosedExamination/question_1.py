import csv


def text2dictionary(filename):
    countries = {}
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',', skipinitialspace=True)
        for row in reader:
            try:
                if row[1] not in countries.keys():
                    if len(row[2]) != 3:
                        raise IOError
                    countries[row[1]] = [(row[0], row[2])]
                else:
                    if (row[0], row[2]) not in countries[row[1]]:
                        countries[row[1]].append((row[0], row[2]))
            except IndexError:
                raise IOError
    return countries
