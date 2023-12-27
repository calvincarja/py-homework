def web_password(password):
    str_password = str(password)
    if not (8 <= len(str_password) <= 12):
        return "incorrect length of password"
    upper_count = 0
    lower_count = 0
    digit_count = 0
    for x in password:
        if x.isupper(): 
            upper_count += 1 # adds a 1 to each instance of upper == true
        if x.islower():
            lower_count += 1
        if x.isdigit():
            digit_count += 1
        if upper_count >= 2 and lower_count >= 3 and digit_count >= 1:  # change this number to require more uppercase letters
            break # goes directly to final return 
    if upper_count < 2 or lower_count < 3 or digit_count < 1:
        return "Does not include at least one capital letter"
    return "password saved"

# test calvin 
