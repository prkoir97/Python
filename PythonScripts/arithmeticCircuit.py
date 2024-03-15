# A34
# Arithmetic Circuit

in1 = True  # or False, depending on the desired input
in2 = False  # or True, depending on the desired input

out1 = (in1 and in2)
out2 = not(in1 and in2) and (in1 or in2)
out3 = not(in2)

print(out1, out2, out3)
