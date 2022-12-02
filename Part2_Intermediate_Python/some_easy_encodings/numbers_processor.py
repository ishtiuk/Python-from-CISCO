
# Numbers Processor.

def numbers_processor(line):
    strings = line.split()
    total = 0
    try:
        if line.isspace():
            return "Empty string!"
        for substr in strings:
            total += float(substr)
        return "The total is: " + str(total)
    except:
        return str(substr) + " is not a number."


line = numbers_processor(input("Enter a line of numbers - separate them with spaces: "))
print(line)