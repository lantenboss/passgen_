def passgen_(l):
    import string
    import random
    characs = (string.ascii_letters)
    nums = (string.digits)
    spec_chr = (string.punctuation)
    total = characs + nums + spec_chr

    x = random.choices(total , k=l)
    return string(x) 

k = passgen_(6)
print(k)