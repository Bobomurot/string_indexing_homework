def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a = len(s)
    
    if abs(n) > a:
        return False
    else:
        return s[n]
