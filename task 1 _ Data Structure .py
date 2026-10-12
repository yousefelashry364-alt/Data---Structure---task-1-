


def seconds_to_hms(seconds):
    """Convert a non-negative number of seconds to HH:MM:SS."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{remaining_seconds:02}"


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit, rounded to 2 decimal places."""
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


def split_evenly(total, people):
    """Return (amount_each, leftover) when total is shared among people."""
    return total // people, total % people


def initials(full_name):
    """Return the uppercase initials from a space-separated full name."""
    parts = full_name.split()
    result = ""
    index = 0
    while index < len(parts):
        result = result + parts[index][0].upper()
        index = index + 1
    return result


def is_palindrome_word(word):
    """Return whether word reads the same in reverse, ignoring case/spaces."""
    cleaned = word.strip().lower()
    return cleaned == cleaned[::-1]


def mask_email(email):
    """Hide the email username except for its first character."""
    at_index = email.index("@")
    username = email[:at_index]
    domain = email[at_index:]
    if len(username) <= 1:
        return username + domain
    return username[0] + ("*" * (len(username) - 1)) + domain


def middle(values):
    """Return the middle item, or the two middle items, as a list."""
    length = len(values)
    if length == 0:
        return []
    middle_index = length // 2
    if length % 2 == 1:
        return [values[middle_index]]
    return values[middle_index - 1:middle_index + 1]


def rotate_left(values, k):
    """Return a new list rotated left by k positions; leave values unchanged."""
    length = len(values)
    if length == 0:
        return []
    k = k % length
    return values[k:] + values[:k]


def fib_list(n):
    """Return the first n Fibonacci numbers, starting with 0 and 1."""
    result = []
    a = 0
    b = 1
    count = 0
    while count < n:
        result.append(a)
        a, b = b, a + b
        count = count + 1
    return result


def collatz_steps(n):
    """Return the number of Collatz steps needed for positive n to reach 1."""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps = steps + 1
    return steps


print("1. seconds_to_hms:", seconds_to_hms(3661))
print("2. celsius_to_fahrenheit:", celsius_to_fahrenheit(25))
print("3. split_evenly:", split_evenly(10, 3))
print("4. initials:", initials("Mona Ali Hassan"))
print("5. is_palindrome_word:", is_palindrome_word("Level"))
print("6. mask_email:", mask_email("student@example.com"))
print("7. middle:", middle([10, 20, 30, 40]))
print("8. rotate_left:", rotate_left([1, 2, 3, 4], 1))
print("9. fib_list:", fib_list(7))
print("10. collatz_steps:", collatz_steps(6))



