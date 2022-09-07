from hashlib import md5

input = "ojvtpuvg"
hex = ''
code = ['', '', '', '', '', '', '', '']
num = 1
while not all(code):
    hex_input = input+str(num)
    hex = md5(hex_input.encode()).hexdigest()
    if hex[:5] == "00000":
        if (
            hex[5].isdigit()
            and int(hex[5]) < 8
            and code[int(hex[5])] == ""
        ):
            code[int(hex[5])] = hex[6]
        num += 1
        print(code)
    else:
        num += 1

print(''.join(code))