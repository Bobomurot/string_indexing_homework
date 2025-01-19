def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    return s.count('0') + s.count('1') + s.count('2') + s.count('3') + s.count('4') + s.count('5') + s.count('6') + s.count('7') + s.count('8') + s.count('9')