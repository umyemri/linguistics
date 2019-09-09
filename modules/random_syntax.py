import random

def stem():
    stems = ['isuu', 'oj', 'inn', 'sigo', 'jili', 'rao', 'fato', 'joast', \
        'wui', 'muoi', 'veo', 'och', 'oei', 'vj', 'peii', 'sme' ]
    return stems[random.randrange(0, len(stems)-1)]

def root():
    roots = ['bal', 'aop', 'ft', 'ano', 'hji', 'quf', 'cocix', 'jsk', 'jiv', \
        'voso', 'quoa']
    return roots[random.randrange(0, len(roots)-1)]

def particle():
    parti = ['ur', 'wa', 'to', 'na', 'ha', 'wano']
    return parti[random.randrange(0, len(parti)-1)]

def main():
    for i in range(400):
        rando = random.randrange(0,100)
        if rando < 75:
            print(stem() + root(), end=' ')
        else:
            print(particle(), end=' ')

if __name__ == '__main__':
    main()
