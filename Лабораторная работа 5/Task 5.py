from random import sample
import string
def get_random_password() -> str:
    all_symb = string.ascii_letters + string.digits
    return ''.join(sample(all_symb, 8))

print(get_random_password())
