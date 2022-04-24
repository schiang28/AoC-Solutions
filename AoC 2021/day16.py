from math import prod

with open("day16input.txt") as f:
    # python automatically removes 0s at start so have to add them if first digit of hex is less than 8
    file = [
        "0" * (4 - len(bin(int(f, 16))[2:])) + bin(int(f, 16))[2:] for f in f.read()
    ]
versiontotal, code = [], "".join(file)


def parsecode(code):
    version, typeid, code = int(code[0:3], 2), int(code[3:6], 2), code[6:]
    versiontotal.append(version)
    if typeid == 4:
        val, code = literalpacket(code)
    elif code[0] == "0":
        val, code = lengthid0(typeid, code[1:])
    else:
        val, code = lengthid1(typeid, code[1:])
    return val, code


def literalpacket(code):
    finalbin = ""
    while True:
        subpacket = code[:5]
        finalbin += subpacket[1:]
        code = code[5:]
        if subpacket[0] == "0":
            break
    return int(finalbin, 2), code  # value of literal packet and remaining bits at end


def lengthid0(typeid, code):
    lengthofsubpackets = int(code[:15], 2)
    code, v = code[15:], []
    while lengthofsubpackets > 0:
        length = len(code)
        val, code = parsecode(code)
        lengthofsubpackets -= length - len(code)
        v.append(val)
    return calculatetype(typeid, v), code


def lengthid1(typeid, code):
    nosubpackets = int(code[:11], 2)
    code, v = code[11:], []
    for _ in range(nosubpackets):
        val, code = parsecode(code)
        v.append(val)
    return calculatetype(typeid, v), code


def calculatetype(typeid, v):
    cases = {
        0: sum(v),
        1: prod(v),
        2: min(v),
        3: max(v),
    }
    if typeid > 4:
        cases[5] = 1 if v[0] > v[1] else 0
        cases[6] = 1 if v[0] < v[1] else 0
        cases[7] = 1 if v[0] == v[1] else 0
    return cases[typeid]


val, code = parsecode(code)
print(sum(versiontotal))
print(val)
