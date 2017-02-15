#!/usr/bin/env python

"""

Amaterasu'Kai

Kyoto University
Graduate School of Medicine
Erik Walinda

Last change: 2017-2-15

* added APK

********************* For Screening *********************  

./amaterasu.py --reference=examples/2001 --data=examples/2001 -r -s

--reference=1001  [reference data] directory. __has to be specified, but is not used__!!! 
--data=1001       [screening data] directory. 
-m                manual phasing
--p0=0            manual phase p0 = 0
-r                run
-s                perform screening

************** For full dataset processing **************  

./amaterasuX.py --reference=1000 --data=1001 -m --p0=0 -r

--reference=1000  [reference data] directory 
--data=1001       [spin-lock data] directory
-m                manual phasing
--p0=0            manual phase p0 = 0
-r                run

*********************************************************
"""

from amaterasux import *
#import amaterasux

amaterasux.main()
