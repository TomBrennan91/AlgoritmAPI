def is_valid(isbn: str):
    """
    Determines whether the provided ISBN-10 string is valid. An ISBN-10 is valid
    if it consists of exactly 10 characters where each character except the last
    one must be a digit, and the last one can be a digit or 'X' (representing
    the value 10). Hyphens in the input are ignored for validation purposes.
    The validity of the ISBN is calculated using the modulus 11 algorithm.

    :param isbn: The ISBN-10 string to validate (with or without hyphens).
    :type isbn: str
    :return: True if the ISBN-10 is valid; otherwise, False.
    :rtype: bool
    """
    isbn = isbn.replace('-', '')

    if not len(isbn) == 10:
        return False

    total = 0
    for i in range(len(isbn)):
        multiplier = 10 - i
        c = isbn[i]

        # it's valid to use X to mean "10" as the last digit in the ISBN
        if c == 'X' and multiplier == 1:
            total += 10
            continue

        if not c.isdigit():
            return False

        total += int(c) * multiplier

    return total % 11 == 0
