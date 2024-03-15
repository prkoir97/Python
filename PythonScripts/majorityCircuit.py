# A23
# Majority Circuit: computes the output of a logical expression based on three input variables

in1 = True
in2 = False
in3 = True

out = ((in1 and in2) or (in1 and in3)) or (in2 and in3)

print(out)