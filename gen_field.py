import random


def main():
    a=[[i for i in range (1,10)] for j in range (9)]
    print (a)
    for i in range (3):
        if i%3==1:
            for j in range (9):
                a[i][j]+=3
                if a[i][j]>9:
                    a[i][j]=a[i][j]%9
        if i%3==2:
            for j in range (9):
                a[i][j]+=6
                if a[i][j]>9:
                    a[i][j]=a[i][j]%9

    for i in range (3,6):
        if i%3==0:
            for j in range (9):
                a[i][j]+=8
                if a[i][j]%9!=0:
                    a[i][j]=a[i][j]%9
                else:
                    a[i][j]=9
        if i%3==1:
            for j in range (9):
                a[i][j]+=11
                if a[i][j]%9!=0:
                    a[i][j]=a[i][j]%9
                else:
                    a[i][j]=9
        if i%3==2:
            for j in range (9):
                a[i][j]+=14
                if a[i][j]%9!=0:
                    a[i][j]=a[i][j]%9
                else:
                    a[i][j]=9
    for i in range (6,9):
        if i%3==0:
            for j in range (9):
                a[i][j]+=16
                if a[i][j]%9!=0:
                    a[i][j]=a[i][j]%9
                else:
                    a[i][j]=9
        if i%3==1:
            for j in range (9):
                a[i][j]+=19
                if a[i][j]%9!=0:
                    a[i][j]=a[i][j]%9
                else:
                    a[i][j]=9
        if i%3==2:
            for j in range (9):
                a[i][j]+=22
                if a[i][j]%9!=0:
                    a[i][j]=a[i][j]%9
                else:
                    a[i][j]=9

    for k in range (1000):
        b=[]
        for i in range (3):
            b.append(a[i])
        random.shuffle(b)
        for j in range (3):
            a[j]=b[j]
        b=[]
        for i in range (3,6):
            b.append(a[i])
        random.shuffle(b)
        for j in range (3,6):
            a[j]=b[j%3]
        b=[]
        for i in range (6,9):
            b.append(a[i])
        random.shuffle(b)
        for j in range (6,9):
            a[j]=b[j%3]
        b=[]
        c=[]
        f=[]
        m=[]
        for i in range (9):
            f.append(a[i])
            if i%3==2 :
                m.append(f)
                f=[]
        random.shuffle(m)
        for i in range (9):
            a[i]=m[i//3][i%3]
        for i in range (9):
            for j in range (9):
                c.append (a[j][i])
            b.append(c)
            c=[]
        a=[]
        for i in range (3):
            a.append(b[i])
        random.shuffle(a)
        for j in range (3):
            b[j]=a[j]
        a=[]
        for i in range (3,6):
            a.append(b[i])
        random.shuffle(a)
        for j in range (3,6):
            b[j]=a[j%3]
        a=[]
        for i in range (6,9):
            a.append(b[i])
        random.shuffle(a)
        for j in range (6,9):
            b[j]=a[j%3]
        a=[]
        for i in range (9):
            a.append (b[i])
        f=[]
        m=[]
        for i in range (9):
            f.append(a[i])
            if i%3==2 :
                m.append(f)
                f=[]
        random.shuffle(m)
        for i in range (9):
            a[i]=m[i//3][i%3]
        b=[]
        for i in range (9):
            for j in range (9):
                c.append (a[j][i])
            b.append(c)
            c=[]
        a=[]
        for i in range (9):
            a.append (b[i])
        b=[]
    f=[]
    m=[]
    for i in range(9):
        print (a[i])
    for i in range (9):
        f.append(a[i])
        if i%3==2 :
            m.append(f)
            f=[]
    random.shuffle(m)
    for i in range (9):
        a[i]=m[i//3][i%3]
    print ('------------------')
    text=''
    text1=''
    luch=0
    for i in range(9):
        for j in range (9):
            print (a[i][j], end=' ')
            text+=str(a[i][j])
            luch=random.choice([a[i][j],0])
            text1+=str(luch)
        print('')
    print (text)
    notsee = open('sudokunotsee.txt', 'w')
    notsee.truncate()
    notsee.write(text)
    notsee.close()
    see = open('sudokusee.txt','w')
    see.truncate()
    see.write(text1)
    see.close()


if __name__ == '__main__':
    main()
