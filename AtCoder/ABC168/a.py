n = input()
a = ["2","4","5","7","9"]
b = ["0", "1", "6", "8"]
if n[-1] in a:
    print("hon")
    exit()
elif n[-1] in b:
    print("pon")
    exit()
else:
    print("bon")
    exit()
