import math


def is_prime(number: int) -> bool:
    """
    Determines whether an integer is prime.
    
    Convention: By standard mathematical definition, primes are integers
    strictly greater than 1 (only divisible by 1 and themselves).
    Non-positive numbers (<= 0) and 1 are not prime.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check divisors up to sqrt(number) using 6k +/- 1 step optimization
    limit = int(math.isqrt(number))
    for i in range(5, limit + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def get_divisors(number: int) -> list[int]:
    """
    Returns all positive divisors of an integer in ascending order.
    
    Convention: Divisors are based on the magnitude abs(number).
    Zero has infinitely many non-zero divisors (0 % d == 0 for all d != 0),
    so we return an empty list [] to represent no finite divisor set.
    """
    n = abs(number)
    if n == 0:
        return []

    divisors = []
    limit = math.isqrt(n)
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


def sum_of_digits(number: int) -> int:
    """
    Returns the sum of the digits of the number.
    
    Convention: Uses the absolute value of the number because the sign
    is an operator, not an inherent value of the constituent digits.
    """
    return sum(int(digit) for digit in str(abs(number)))


def reverse_number(number: int) -> int:
    """
    Reverses the integer's digits.
    
    Convention: Preserves the negative sign (e.g., -120 -> -21).
    Trailing zeroes in the original number naturally drop when parsed back to int.
    """
    sign = -1 if number < 0 else 1
    reversed_digits = str(abs(number))[::-1]
    return sign * int(reversed_digits)


def analyze_number(number: int) -> dict:
    """
    Aggregates a complete numerical breakdown into a structured dictionary.
    """
    parity = "even" if number % 2 == 0 else "odd"

    report = {
        "number": number,
        "parity": parity,
        "is_prime": is_prime(number),
        "digit_sum": sum_of_digits(number),
        "reversed": reverse_number(number),
        "divisors": get_divisors(number),
    }

    return report


def print_analysis(report: dict):
    """Utility function to print a clean report."""
    print("=" * 40)
    print(f"ANALYSIS REPORT FOR: {report['number']}")
    print("=" * 40)
    print(f"• Parity       : {report['parity'].capitalize()}")
    print(f"• Prime        : {'Yes' if report['is_prime'] else 'No'}")
    print(f"• Sum of Digits: {report['digit_sum']}")
    print(f"• Reversed     : {report['reversed']}")
    divisors_str = ", ".join(map(str, report['divisors'])) if report['divisors'] else "Undefined / Infinite"
    print(f"• Divisors     : [{divisors_str}]")
    print("=" * 40 + "\n")


# --- Demonstrations ---
if __name__ == "__main__":
    # Test 1: Standard input (123)
    print_analysis(analyze_number(123))

    # Test 2: Negative number (-120)
    print_analysis(analyze_number(-120))

    # Test 3: Zero (0)
    print_analysis(analyze_number(0))