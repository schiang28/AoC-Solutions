with open("day1input.txt") as f:
    file = f.read().splitlines()

digits = {'one':1,
          'two':2,
          'three':3,
          'four':4,
          'five':5,
          'six':6,
          'seven':7,
          'eight':8,
          'nine':9,}

ls = []
for word in range(len(file)):
    digit = ''
    for char in range(len(file[word])):
        if file[word][char].isdigit():
            digit += file[word][char]
        for end in range(char, len(file[word])+1):
            if file[word][char:end] in digits.keys():
                 digit += str(digits[file[word][char:end]])
    ls.append(''.join(digit))

ans = sum([int(i[0]+i[-1]) for i in ls])
print(ans)