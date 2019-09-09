import random

def stem():
    stems = ['isuu', 'oj\'', 'inn', 'sigo', 'jili', 'rao', 'fato', 'joast', \
        'wui', 'muoi', 'veo', 'och\'', 'oei', 'vj', 'peii', 'sme']
    return stems[random.randrange(0, len(stems)-1)]

def root():
    roots = ['bal', 'aop', 'ft', 'ano', 'hji', 'quf', 'cocix', 'jsk', 'jiv', \
        'voso', 'quoa', 'iees', ]
    return roots[random.randrange(0, len(roots)-1)]

def particle():
    parti = ['ur', 'wa', 'to', 'na', 'ha', 'wano', 'keis', 'sho']
    return parti[random.randrange(0, len(parti)-1)]

def punctuation():
    punct = ['.', '?', '...', '!', ',']
    return punct[random.randrange(0, len(punct)-1)]

def main():
    for i in range(1000):
        rando = random.randrange(0,100)
        if rando <= 75 and rando >= 25:
            print(stem() + root(), end=' ')
        elif rando < 25:
            print(particle(), end=' ')
            print(stem() + root(), end='')
            if rando < 10:
                print(punctuation()+' '+stem().capitalize() + root(), end=' ')
            else:
                print(' ', end='')

if __name__ == '__main__':
    main()
