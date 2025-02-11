from cecs328pa1 import asymptotic_analysis
from sympy import symbols
# Testing the function
print(asymptotic_analysis("2**n", "3**n", "O"))  # Expected: True
print(asymptotic_analysis("lg(n)", "n", "O"))  # Expected: True (lg is log base 2)
print("hi")
