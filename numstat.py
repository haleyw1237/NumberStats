
def calculate(filename):

    file = open(filename)
    numbers = []
    for line in file:
        n = float(line)
        numbers.append(n)

    file.close()

    number_sum = sum(numbers)
    number_count = len(numbers)
    number_average = number_sum / number_count
    number_maximum = max(numbers)
    number_minimum = min(numbers)
    number_range = number_maximum - number_minimum


    print("Filename:", filename)
    print("Sum:", number_sum)
    print("Count:",number_count)
    print("Average:", number_average)
    print("Maximum:", number_maximum)
    print("Minimum:", number_minimum)
    print("Range", number_range)

def main():
    while(True):
     requested = input("Filename:")
     calculate(requested)
     requested = input(" Would you like to continue? y/n")
     if (requested != "y"):
        break

main()