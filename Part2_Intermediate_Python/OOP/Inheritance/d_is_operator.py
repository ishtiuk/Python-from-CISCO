
class SampleClass:
    def __init__(self, val):
        self.val = val

class Clss:
    def __init__(self, val):
        self.val = val


clss_obj = Clss(0)
clss_obj.val += 1
object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_3 is clss_obj)
print(object_3.val is clss_obj.val)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
print(id(object_1), id(object_3))                    # both's memory locations are same, because they both refers the same Object ;)