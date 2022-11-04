
def function():
    latins = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    count_dict = {}
    srcnm = input("Enter the file name: ")
    s = open(srcnm, 'rt')
    line = s.readline()
    
    while len(line) > 0:
        for c in line:
            if c in latins:
                c = c.lower()
                
                if c not in count_dict:
                    count_dict[c] = 0
                count_dict[c] += 1
            
        line = s.readline()
     
    lambda count_dict : sorted(count_dict.items())
    
    
data = function()

for key in data.keys():
    print(key, data[key], sep=" -> ")

print(data)