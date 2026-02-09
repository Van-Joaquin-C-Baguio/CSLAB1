import matplotlib.pyplot as plt
from decimal import Decimal, getcontext, ROUND_HALF_UP



getcontext().prec = 150 

PI_STRING = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647"



def get_pi_truncated(n_decimals):
    """Cut off Pi after n decimals without rounding."""
    dot_index = PI_STRING.find('.')
    truncated_str = PI_STRING[:dot_index + 1 + n_decimals]
    return Decimal(truncated_str)

def get_pi_rounded(n_decimals):
    """Round Pi to n decimals."""
    full_pi = Decimal(PI_STRING)
    return full_pi.quantize(Decimal(f"1e-{n_decimals}"), rounding=ROUND_HALF_UP)

# Formula chosen: Circumference
# C = 2 * pi * r
def calculate_circumference(radius, pi_val):
    return Decimal(2) * pi_val * Decimal(radius)



radius = 5000
decimals_to_test = [20, 40, 60, 100]

true_pi = Decimal(PI_STRING)
true_circumference = calculate_circumference(radius, true_pi)

errors_truncated = []
errors_rounded = []



print("\n========== ACTIVITY INFORMATION ==========")
print("Goal:")
print("Get the difference between the 2 baselines\n")

print("Formula Used:")
print("C = 2 * pi * r\n")

print(f"Radius used: {radius}")
print(f"Decimal precision of calculations: {getcontext().prec}")

print("\nBaselines Concept:")
print("Truncation example (4 decimals): 3.1415")
print("Rounding example   (4 decimals): 3.1416")

print("\nTrue reference pi (first digits):")
print(str(true_pi)[:60] + "...")

print("\n============================================")
print(f"{'Decimals':<10} | {'Type':<10} | {'Difference from True Circumference':<30}")
print("-" * 70)



for d in decimals_to_test:

    # Truncation
    pi_t = get_pi_truncated(d)
    circ_t = calculate_circumference(radius, pi_t)
    diff_t = abs(true_circumference - circ_t)
    errors_truncated.append(diff_t)

    # Rounding
    pi_r = get_pi_rounded(d)
    circ_r = calculate_circumference(radius, pi_r)
    diff_r = abs(true_circumference - circ_r)
    errors_rounded.append(diff_r)

    print(f"{d:<10} | {'Trunc':<10} | {diff_t:.101f}...")
    print(f"{d:<10} | {'Round':<10} | {diff_r:.101f}...")



plt.figure(figsize=(10, 6))
plt.plot(decimals_to_test, errors_truncated, marker='o', label='Truncation Error', linestyle='--')
plt.plot(decimals_to_test, errors_rounded, marker='s', label='Rounding Error', linestyle='-')

plt.title(f'Error in Circle Circumference (Radius={radius}) by Pi Precision')
plt.xlabel('Decimal Places of Pi')
plt.ylabel('Absolute Error (Difference from True Circumference)')
plt.yscale('log')

plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()
plt.show()
