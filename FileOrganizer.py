import os

print (dir(os))

basedir="/home/k1ll3r/"

print (os.walk(basedir))

for obj in os.walk(basedir):
    print (obj)
