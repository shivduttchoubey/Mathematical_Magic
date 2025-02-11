import sympy as sp

def name_to_integral_exact(name):
    # Convert the name to alphabetical coding
    alphabetical_code = [ord(char.lower()) - 96 for char in name if char.isalpha()]

    # Construct the integral expression
    x = sp.symbols('x')
    integral_expr = sum(code * sp.sin(code * x) for code in alphabetical_code)

    # Define the integral with adjusted limits to get an integer result
    integral = sp.integrate(integral_expr, (x, 0, sp.pi / 4))

    return integral, alphabetical_code

# Example usage
name = input("Enter the name: ")
integral_result, alphabetical_code = name_to_integral_exact(name)
print(f"Alphabetical coding for {name}: {alphabetical_code}")
print(f"Integral result: {integral_result}")

# Output the integral expression
integral_expr = sum(code * sp.sin(code * sp.symbols('x')) for code in alphabetical_code)
print(f"Integral expression: ∫(0 to π/4) [{integral_expr}] dx")
