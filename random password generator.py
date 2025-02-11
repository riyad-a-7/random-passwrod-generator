import random
import string
        
# Simvolların dəstləri
lowercase_alphabet = string.ascii_lowercase
uppercase_alphabet = string.ascii_uppercase
numbers = "0123456789"
symbols = "!@$%&*#+-"

# İstifadəçidən məlumatlar alınır
n_strings = int(input("Xahiş olunur string uzunluğunu qeyd edin: "))
n_numbers = int(input("Xahiş olunur number uzunluğunu qeyd edin: "))
n_symbols = int(input("Xahiş olunur symbol uzunluğunu qeyd edin: "))

# Parol üçün siyahı
n_password = []

# Təsadüfi hərflər əlavə edilir
for _ in range(n_strings):
    random_string = random.choice(lowercase_alphabet + uppercase_alphabet)
    n_password.append(random_string)

# Təsadüfi rəqəmlər əlavə edilir
for _ in range(n_numbers):
    random_number = random.choice(numbers)
    n_password.append(random_number)

# Təsadüfi simvollar əlavə edilir
for _ in range(n_symbols):
    random_symbol = random.choice(symbols)
    n_password.append(random_symbol)

# Parolu qarışdır və birləşdir
random.shuffle(n_password)
password = ''.join(n_password)

print(f"Yaradılan parol: {password}")
