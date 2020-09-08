import sys
sys.path.append("/Users/samwiseaaron/PycharmProjects/samwise")
import numpy
import samwise as sw
import input_name as inn
from samwise import pb

# a trick to get the path, is to drag the folder that's holding the module into the terminal.


# I Created "pb" in module samwise_tools (as sw): Print Break --> for clearer & quicker printing.
# No Parm, just a Print line break,
# 1 parm, print that object with a preceding visual break
# 2 parm, added info to preceding line
# if the object is a list or tuple, each element will print each onb a separate line
# if the object is a libr, each element will print with an " = " followed by it's value
#

x = numpy.zeros((5, 3))

sw.pb(dir(x), "dir(x)")

sw.pb("", "Loop code to get items in Directory, 1 per line")
for i in dir(x):  # Dir gets you all the methods in an object
    print(f"{i}")

sw.pb(x, "2 Dim Array")

y = 0
rn = 0
cn = 0
for r in x:
    cn = 0
    for c in r:
        y += 1
        x[rn][cn] += float(y)
        cn += 1
    rn += 1


sw.pb(x, "2 Dim Array")

y = 0
rn = 0
cn = 0
for r in x:
    cn = 0
    for c in r:
        y += 1
        x[rn][cn] += float(y)
        cn += 1
    rn += 1


sw.pb(x, "2 Dim Array")


y = 0
rn = 0
cn = 0
for r in x:
    cn = 0
    for c in r:
        y += 1
        x[rn][cn] += float(y)
        cn += 1
    rn += 1


sw.pb(x, "2 Dim Array")


sw.pb(numpy.sum(x), "sum(x)")

sw.pb("Sam was Here!".upper(), "Sam was Here!.upper()")
sw.pb()
sw.pb(type(sw.pb))
sw.pb(type(sw.pb), "type(sw.pb)")

sw.pb(sw.__name__, "sw.__name__")
sw.pb(dir(sw), "sw.dir()")

file_name = "TOOM099.gamble"
sw.pb(sw.get_inc_file_ext(file_name), f"Next File {file_name}")

sw.pb(sw.__builtins__, "sw.__builtins__")

xyz = ["Sam", "Jack", "Chris", "John", "Wink", "Ted", "Mary", "Terry"]


xyzu = []
for item in xyz:
    xyzu.append(item.upper())

xyzl = []
for item in xyz:
    xyzl.append(item.lower())

xyzc = []
for item in xyzu:
    l1 = item[0].upper()
    l2 = item[1:].lower()
    xyzc.append(l1 + l2)


sw.pb(xyz, "Original")
sw.pb(xyzu, "Upper Case")
sw.pb(xyzl, "Lower Case")
sw.pb(xyzc, "Capitalize First Letter")

sw.pb(sys.path, "System Path")

sw.pb(dir(sw), "Items in sw: samwise_tools (Imported Module)")

sw.pb("", "Run Function [p_name] from Added Sys Path")

# sw.pb(inn.p_name())  # Called function from module that I added the path to the sys.path

sw.pb(sw.__file__, f"Loc of {sw.__name__}")

pb("", "pb() Imported From Samwise_tools")

pb(__name__, "A")
pb(sw.__name__, "B")
