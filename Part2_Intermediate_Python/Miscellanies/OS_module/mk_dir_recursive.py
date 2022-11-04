
import os

try:
    os.makedirs("my_first_directory/my_second_directory")
    os.chdir("my_first_directory")
except FileExistsError as e:
    print("Error: ", e.__str__())
finally:
    os.chdir("my_first_directory")
    print(os.listdir())
    os.chdir('..')


try:
    os.makedirs("hello/nc/h/j/k/m/j")
except FileExistsError as e:
    print("Error: ", e.__str__())
finally:
    os.chdir('hello')
    print(os.listdir())
 
# NOTE: "os.mkdirs()" function isn't available on Linux-family Systems, it's only available for Windows.....