#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:07:25 2019

@author: jericajohnson
"""

# This Python program will have the user enter a parallax angle of a nearby
# star. The program will then calculate three different distances from Earth:
# 1. Parsecs (pc) 2. Lightyears (ly) 3. Astronomical Units (AU).

#note: the number may not be completely accurate after the hundredths place.

# Asks user to input the star's name.
starName = input("What is the name of the star we will be calculating? ")

# Asks user to input the parallax angle, then convert that to a float.
parallaxAngle = float(input("What is the star's parallax angle? "))

# Defines and calculates the parsecs distance from star to Earth.
parsecsDistance = 1 / parallaxAngle

# Prints a blank line to seperate user input from print statements.
print("")
# Program prints the star's distance from Earth in parsecs (pc).
print(starName, "has a distance of", parsecsDistance, "parsecs.")

# Defines and calculates the distance in lightyears from star to Earth.
lightyearsDistance = parsecsDistance * 3.2616

# Program prints the star's distance from Earth in lightyears (ly).
print(starName, "has a distance of", lightyearsDistance, "lightyears.")

# Defines and calculates the distance in Astronomical Units from star to Earth.
astronomicalUnit = parsecsDistance * 206264.806

# Program prints the star's distance from Earth in Astronomical Units (AU).
print(starName, "has a distance of", astronomicalUnit, "AU.")


