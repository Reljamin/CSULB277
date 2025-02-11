from sympy import symbols, log, simplify, oo, Limit, Lambda
#version 1
def asymptotic_analysis(left_function, right_function, asymptotic_symbol):
    # Define the variable n
    n = symbols('n', positive=True)
    lg = Lambda(n, log(n, 2))
    # Convert the string inputs into Sympy expressions
    left_expr = simplify(eval(left_function))
    right_expr = simplify(eval(right_function))
    
    if asymptotic_symbol == "O":  # Big-O analysis
        # Check if the limit of left_expr / right_expr tends to a finite constant or 0
        limit = Limit(left_expr / right_expr, n, oo).doit()
        return limit.is_finite or limit == 0
    elif asymptotic_symbol == "Θ":  # Theta analysis
        # Both left_expr / right_expr and right_expr / left_expr must tend to a non-zero constant
        limit1 = Limit(left_expr / right_expr, n, oo).doit()
        limit2 = Limit(right_expr / left_expr, n, oo).doit()
        return limit1.is_finite and limit2.is_finite and limit1 != 0 and limit2 != 0
    elif asymptotic_symbol == "Ω":  # Omega analysis
        # Check if right_expr / left_expr tends to a finite constant or 0
        limit = Limit(right_expr / left_expr, n, oo).doit()
        return limit.is_finite or limit == 0
    else:
        raise ValueError("Invalid asymptotic symbol. Use O, Θ, or Ω.")