import string
def isUUID4(id):
    for char in id:
        if char not in string.digits or char not in string.ascii_letters:
            return False
    return True