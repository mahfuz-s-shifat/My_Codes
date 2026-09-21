class Example:
    # Public: Meant to be accessed from anywhere
    public_var = "I am Public"
    # Protected: Meant to be accessed within class and subclasses
    _protected_var = "I am Protected"
    # Private: Name mangled, intended for internal class use only
    __private_var = "I am Private"



class Example:
    a = 5 # Public
    _b = 7 # Protected
    __c = 10 # Private

