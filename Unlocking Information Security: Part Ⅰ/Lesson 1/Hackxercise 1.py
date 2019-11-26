#The function check_password(password) is used by a safe with 4-digits passwords, and is susceptible to timing attacks.
#More specifically, it takes it around 0.1 seconds to check one digit – so brute-forcing all the possible combinations
#will take around 1,500 hours. Can you implement a way to crack its password in less than a minute?

import time
import sys  # ignore

sys.path.insert(0, '.')  # ignore
from Root.pswd import real_password


def check_password(password):  # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True


def crack_password():
    password_zero = ["0", "0", "0", "0"]
    for i in range(0, 4):
        for j in range(0, 10):
            password_zero[i] = str(j)
            password = ''.join(map(str, password_zero))

            time1 = time.time()
            ret = check_password(password)
            time2 = time.time()

            if (ret == True):
                return (password)

            time_difference = time2 - time1
            if time_difference > 0.1 * (i + 2):
                password_zero[i] = str(j)
                break


print("checking...")
t0 = time.time()
pwd = crack_password()
t1 = time.time()
print(pwd)
print(str(t1 - t0))