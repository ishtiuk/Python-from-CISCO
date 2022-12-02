
import platform

print(platform.platform(aliased=False, terse=True))

print(platform.machine())
print(platform.win32_ver())

print(platform.uname())
print(platform.uname_result(platform.system(), platform.node(), platform.release(), platform.version(), platform.machine(), platform.processor()))      # tedious, exhausting 😵‍💫

print(platform.processor())
print(platform.system())
print(platform.version())


from platform import python_branch, python_implementation, python_version_tuple

print('.'.join(python_version_tuple()))

for atr in python_version_tuple():
    print(atr)
