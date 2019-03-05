print("Adelaide".strip('A'))  # use the '.strip' function to remove characters from only
                              # the beginning or end of a string

print("Adelaide".strip('del'))
 # here's the result set for this above syntax: delaide, Adelai; important to notice here that
 # the .strip function removed the leading 'A' in Adelaide in the first print function, but in
 # the second however, it does not remove the leading 'del' in Adelaide but the last 'de' b/c
 # there is a partial match at the end of the string.
