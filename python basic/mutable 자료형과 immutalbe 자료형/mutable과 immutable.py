immutable = "String is immutable!!"
mutable = ["list is mutable!!"]
 
string = immutable
list_ = mutable

string += " immutable string!!"
list_.append("mutable list!!")

print(immutable)
print(mutable)
print(string)
print(list_)

# result print
"""
String is immutable!!
['list is mutable!!', 'mutable list!!']
String is immutable!! immutable string!!
['list is mutable!!', 'mutable list!!']
"""