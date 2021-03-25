#!/usr/bin/env python
#xrange only in python2 
#xrange not available in python3 

import xrange

for a in range(1,100):
    print(a,end="")

print("\n\n")

for x in xrange(100):
    print(x,end="")

