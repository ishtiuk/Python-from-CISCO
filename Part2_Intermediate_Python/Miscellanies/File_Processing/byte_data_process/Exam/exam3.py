from os import strerror
import os


class StudentsDataException(Exception):
    e_dict = {0 : 'text', 1 : 'text', 2 : 'number'}
    
    def __init__(self, n, n2 = ''):
        self.n = n
    def __str__(self): 
        return f"Error: the serial {self.n+1}'s data must be [{self.e_dict[self.n]}]"
 

class BadLine(StudentsDataException):
    def __init__(self):
        pass
    def __str__(self):
        return "Error: The line must contain: [1st name] [2nd name] [points]"


class FileEmpty(StudentsDataException):
    def __init__(self):
        pass
    def __str__(self):
        return "Error: [This file is empty]"
    
def data_checker(data):
    try:
        if len(data) != 3:
            raise BadLine

        data[2] = float(data[2])

        for i in range(2):
            if not data[i].isalpha():
                raise StudentsDataException(i) 

    except StudentsDataException as s:
        exit(s)
    except BadLine as b:
        exit(b)
    except ValueError as e:
        print("Error: ", end='')   
        exit( e)

    return data

def main():
    cnt_dict = {}
    filenm = input("Enter source filename: ")


    try:
        s = open(filenm, 'rt')
        lines = s.readlines()
        print(lines)
        s.close()
        src = open(filenm, 'rt')
          
        if any(i.isspace() for i in lines):
            raise FileEmpty
    except IOError as er:
        print("Unable to open file: ", strerror(er.errno))
        exit(er.errno)
    except FileEmpty as fe:
        exit(fe)

    data = src.readline().strip().split()

    while len(data) != 0:
        data = data_checker(data)
        if f"{data[0]} {data[1]}" not in cnt_dict.keys():
            cnt_dict[f"{data[0]} {data[1]}"] = 0
  
        cnt_dict[f"{data[0]} {data[1]}"] += float(data[2])

        data = src.readline().strip().split()

    return cnt_dict, filenm

counters = main()
output = open(counters[1]+'.hist', 'wt')

for key in sorted(counters[0].keys()):
    d = f"{key}\t{counters[0][key]}\n"
    output.write(d)

output.close()

print("\nSuccessfully written histogram file, Location: [", os.path.abspath(counters[1]+".hist ]"))

