# strings and integers CANNOT be directly written to a binary file; they need to be converted
# to bytes first; you can achieve this by using the 'bytes' built-in function

# ************************************************************************************************
# with open("binary", 'bw') as bin_file:
#     # bin_file.write(bytes(range(17)))  .... this is the same code below, just more efficient
#     for i in range(17):
#         bin_file.write(bytes([i]))
#         # what we're doing here is converting the number 'i' to bytes format and then writing
#         # that to a binary file
#         # by enclosing 'i' in [] we are passing a list through a single item, 'i' which the
#         # bytes function then correctly converts to a single byte
#
# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)

# *************************************************************************************************

a = 65534    # FF FE
b = 65535    # FF FF
c = 65536    # 00 01 00 00
x = 2998302  # 02 2D C0 1E

with open("binary2", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big')) #  the '.to_bytes' function converts the integer to bytes (length, byteorder)
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))

with open("binary2", 'br') as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    print(e)
    f = int.from_bytes(binFile.read(2), 'big')
    print(f)
    g = int.from_bytes(binFile.read(4), 'big')
    print(g)
    h = int.from_bytes(binFile.read(4), 'big')
    print(h)
    i = int.from_bytes(binFile.read(4), 'big')
    print(i)



