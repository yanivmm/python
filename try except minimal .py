# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:56:03 2020

@author: 97250
"""


def send_invitation(name, age):
    try:    
        if int(age) < 18:
            raise underAge(age)
    except underAge as A:
        print("bro, you're young you can come in %s years from now"  %(18-A.get_age()))
    else:
         print("The party will be at the 3/3/21, tou're welcome.")   
            
class underAge(Exception):
    pass
