import os
import platform

# NOTE: the "os.uname()" is only available on a subset of Unix distributions/versions:-
# So, it'll work on Linux based Systems ;), but won't work on Windows........ 🥴

# Hence, we can use the "platform.uname()" module instead. It'll provide the same infos of the "os.uname()", and also a extra info which is the name of "processor" 😁
# so I think it's a better solution...  

print(os.path.pathsep.join(['C://devil', "D://python.exe"]))

print(platform.uname().processor)


# The os module allows you to quickly distinguish the operating system using the name attribute, which supports one of the following names:

# posix — you'll get this name if you use Unix;
# nt — you'll get this name if you use Windows;
# java — you'll get this name if your code is written in Jython.

# For Ubuntu 16.04.6 LTS, the name attribute returns the name posix:

import os
print(os.name)


# NOTE: On Unix systems, there's a command called uname that returns the same information (if you run it with the -a option) as the uname function.