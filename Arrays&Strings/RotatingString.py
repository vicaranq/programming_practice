

def rotationalCipher(input, rotation_factor):
    # Write your code here
    s = []
    for x in input:

        if x.isdigit():
            # rotate number
            t = (int(x)+rotation_factor) % 10
            s.append(str(t))
        elif x.isalpha():
            # rotate letter
            if x.isupper():
                t_val = (ord(x) - ord('A')  + rotation_factor) % (ord('Z') - ord('A')  +1) + ord('A')
            else:
                t_val = (ord(x) - ord('a')  + rotation_factor) % (ord('z') - ord('a')  +1) + ord('a')

            t = chr(t_val)
            s.append(t)
        else:
            s.append(x)

    return "".join(s)

x = "AlL-convoYs-9-be:Alert1."
rotation_factor = 4
print(rotationalCipher(x, rotation_factor))