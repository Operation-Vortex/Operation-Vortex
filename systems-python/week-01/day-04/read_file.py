with open("/Users/mackook/Development/Operation-Vortex/systems-python/week-01/day-04/test_file.txt", "r") as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()