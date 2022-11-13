import random as rd
import string

def get_random_password(n= 8) -> str:
    base = string.ascii_lowercase + string.ascii_uppercase + string.digits
    pass_lst = rd.sample(base, 8)
    pass_ = ''
    for x in pass_lst:
        pass_ += x
    return (pass_)

print(get_random_password(8))
