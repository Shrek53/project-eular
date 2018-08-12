#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n_squre_sum=((n*(n+1)*((2*n)+1))/6)
    n_sum_squre=math.pow((n*(n+1)/2), 2)
    print( int(math.fabs(n_squre_sum-n_sum_squre)) )
