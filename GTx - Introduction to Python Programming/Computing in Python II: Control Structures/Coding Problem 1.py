days_since_release = 14
original_price = 60
greatest_hits = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Write a conditional that determines the price of a
# newly-released game, movie, or album based on the time since
# it was released.
#
# Assume that a new release loses $2 off its price for every
# full week since it was released. So, two full weeks (14 days)
# after a $60 game is released, it will cost $56.
#
# However, if the release is considered a "greatest hit", it
# loses value half as fast: after two weeks, it will be $58
# instead of $56.
#
# No release will ever fall to below $20, however, no matter
# how fast it loses value or whether it's a greatest hit.
#
# Add some code below to print the current price of the release.
# For example, with the values above, it would pring $58.


# Add your code here! Make sure to print the dollar sign, too.

real_price = original_price
weak_since_release = days_since_release/7
weak_since_release = int(weak_since_release)
for i in range(0, weak_since_release):
    # print(i)
    if greatest_hits:
        real_price = real_price-1
    else:
        real_price = real_price-2
if real_price < 20:
    real_price = 20
    print("$", real_price, sep="")
else:
    print("$", real_price, sep="")
