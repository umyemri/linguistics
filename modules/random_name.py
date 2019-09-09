import random

def vow():
    vowels = ['a', 'i', 'u', 'e', 'o', 'y']
    return vowels[random.randrange(0, len(vowels)-1)]

def con():
    consonants = ['b', 'c', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', \
    'r', 's', 't', 'v', 'w', 'x', 'z']
    return consonants[random.randrange(0, len(consonants)-1)]

def nam(name_len):
    name = ''
    for i in range(int(name_len)):
        rando = random.randrange(0, 100)
        #print(str(rando) + ' ', end='') #debugging rando number
        if rando > 40:
            name = name + con()
        else:
            name = name + vow()
    print(name.capitalize(), end=' ')

def main():
    name_len = input('length of name: ')
    iterations = input('how many iterations: ')
    if name_len == 'rando':
        for j in range(int(iterations)):
            nam(random.randrange(5,10))
    else:
        for j in range(int(iterations)):
            print(str(j+1) + '. ', end='')
            nam(name_len)
            print()

if __name__ == '__main__':
    main()
