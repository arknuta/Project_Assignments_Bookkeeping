equation = input("Hi! Enter your quadratic equation folowing this patern: ax^2 + bx + c = 0: ")


try:
    a, b, c = eval(equation.replace('x^2', '').replace('x', ''))

    print("This are the coefficientsof your equation:", a, b, c)

    x1 = (-(b) + (b ** 2 - 4 * a * c )** (0.5)) /(2 * a )
    x2 = (-(b) - (b ** 2 - 4 * a * c )** (0.5)) /(2 * a )

    print("This are the roots of your equation:", int(x1),",", int(x2))

except (SyntaxError, TypeError) as e:
    print(f"Error processing the equation: {e}")
