#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def N_i_p(knots,i,p,xk):
        
    if p==0:
        if xk > knots[i] and xk <= knots[i+1]:
            N12 = 1
        else:
            N12 = 0        
        return N12    
    numerator1 = xk - knots[i]
    dominator1 = knots[i + p] - knots[i]
    if dominator1 == 0:
        N1 = 0
    else:
        N1 = numerator1 / dominator1 * N_i_p(knots,i,p-1,xk)    
    numerator2 = knots[i + p + 1] - xk
    dominator2 = knots[i + p + 1] - knots[i + 1]
    if dominator2 == 0:
        N2 = 0
    else:
        N2 = numerator2 / dominator2 * N_i_p(knots,i+1,p-1,xk)    
    return N1 + N2
 