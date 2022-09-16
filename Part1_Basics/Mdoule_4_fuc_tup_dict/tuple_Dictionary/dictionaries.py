
# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

# Example 2:
phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }

for key in dictionary:
    print(key, "->", dictionary[key])




# one new thing I've learnt today ;D.....

# To remove the last item in a dictionary, you can use the popitem() method:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}

# or our conventional way from programming hero learning 
del dictionary['cat']
print(dictionary)