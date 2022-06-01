def tasc(a):
    if not isinstance(a, str):
        raise TypeError("a must be a str")
    r = []
    for i in list(a):
        r = r + [ord(i)]
    return r
def fasc(a):
    if not isinstance(a, list):
        raise TypeError("a must be a list")
    r = ""
    for i in a:
        r = r + chr(i)
    return r
if __name__ == "__main__":
    print("This is a package! Do not run this!")
