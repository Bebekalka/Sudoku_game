# -*- coding:utf-8 -*-
import pgzrun
import random
import gen_field
import sys

WIDTH= 1000
HEIGHT= 700
##ширина и длина окна

def startgame():
    global notsee, see, i1, j1, WIDTH, HEIGHT, chisla, youwin2, kletki, exit2, restart2, sudokupole, see, notsee, hint2, done
    
    try:
        gen_field.main()
    except Exception as e:
        print(e)
    
    i1 = 0
    j1 = 0
    ## координаты синенькой клетки(синенька клетка это та, по которой вы в последнй раз щелкнули курсором)
    
    done = []
    
    notsee = open('sudokunotsee.txt')
    notsee = notsee.read()
    see = open('sudokusee.txt')
    see = see.read()
    ##see - это то, что мы видим, на самом деле просто в одну строчку записано все, что стоит на поле в начальный момент времени слева направо сверху вниз
    ##not see - это уже разгаданный судоку, опять же написанный в одну строчку слева направо сверху вниз

    
    
    sudokupole = Actor("sudokupole", center = (WIDTH/2,600/2+50))
    ##вывод этого поля(просто решеточек), картинки добавляются отдельно

    youwin2 = Actor("youwin2", center = (-10000,-10000))
    ##картинка выигрыша, которая сначала не видна, но потом ее координаты меняют, чтобы она заслонила поле
    exit2 = Actor("exit2", center = (775 + 100, 50 + 32))

    restart2 = Actor("restart2", center = (775 + 100, 50 + 32 + 100 + 10))
    
    hint2 = Actor("hint2", center = (775 + 100, 50 + 32 + 200 + 20))

    chisla = [0]*9
    kletki = [0]*9
    ##создаются пока что обычные массивы для чисел и клеток

    
    a = 0
    ## какая-то переменная, которая вообще нигде не используется

    for i in range(0,9):
        chisla[i] =[0,0]
        ## переделываем в двумерный массив

        chisla[i][1] = Actor("mychislo" + str(i+1), center = (775, 50 + 32 + i*3 + i*64))
        ## вторая ячейка заполняется картинкой данного числа и собственное координатой
        chisla[i][0] = Actor("white", center = (775, 50 + 32 + i*3 + i*64))
        ## первая ячейка заполняется белым цевтом, типа фон и тоже координатой
        kletki[i] = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        ## трехмерный массив создан в нулевой клетке фон, в первой клетке опять ничего, если мы этого не должны видеть, и стоит число если мы должны это видеть
        ## опять же вторая клетка заполнена 0, если первая клетка заполнена ничем и 1 если заполнена числом
        for j in range(0,9):
            kletki[i][j][0] = Actor("white", center = (50 + 3 + j + 32 + j*64 + j//3*3, 50 + 3 + i + 32 + i*64 + i//3*3))
            ## пока что снова ставит заглушку
            if see[i*9+j]=="0":
                kletki[i][j][1] = Actor("false0", center = (50 + 3 + j + 32 + j*64 + j//3*3, 50 + 3 + i + 32 + i*64 + i//3*3))
                done.append((i, j))
            else:
                kletki[i][j][1] = Actor("mychislo" + see[i*9+j], center = (50 + 3 + j + 32 + j*64 + j//3*3, 50 + 3 + i + 32 + i*64 + i//3*3))
                kletki[i][j][2] = 1

    kletki[0][0][0].image = "blue"
    ## изначально левая верхняя клетка считается как будто мы на нее тыкнули и подсвечивается голубым


def stechkin(i1,j1,n):
    ## эта функция подсвечивает серым клетки, на которых записано такое же число что и на голубой клетке(если это число вообще записано) или если клетки в одном столбце или строке или квадрате 3*3 с голубой
    ##также эта функция потом убирает серый цвет, то есть делает белую заливку, когда меняется голубая клетка
    global kletki
    ##пробегается по всем клеткам
    for x in range(0,9):
        for y in range(0,9):
            if (x!=i1 or y!=j1) and kletki[x][y][0].image != "red":
                if kletki[x][y][1].image[-1] == kletki[i1][j1][1].image[-1] != "0":##типа если совпадают чиселки в клеточках, то подсветка
                    kletki[x][y][0].image = n
                if x == i1:## если находятся в одном столбце
                    kletki[x][y][0].image = n
                if y == j1:## если находятся в одной строке
                    kletki[x][y][0].image = n
                if i1//3*3 <= x < (i1//3 + 1)*3 and j1//3*3 <= y < (j1//3 + 1)*3 :##если находятся в одном квадрате 3*3
                    kletki[x][y][0].image = n


def on_mouse_down(pos):##когда щелкаем мышкой
    global i1, j1, b, kletki, done
    b = 0
    if kletki[i1][j1][2] == 0:##это если в голубой клетке ничего не стоит
        for i in range(0,9):
            if chisla[i][1].collidepoint(pos):## если мы нажали на число чтобы его поставить
                stechkin(i1,j1,"white")## у нас опять убирается серый цвет
                if chisla[i][1].image != "mychislo" + notsee[i1*9+j1]:## если поставленное число не совпадает с задуманным, то задний фон красный, иначе остается голубым
                    kletki[i1][j1][0].image = "red"
                else:
                    kletki[i1][j1][0].image = "blue"
                    done.remove((i1, j1))
                kletki[i1][j1][1].image = "chislo" + str(i+1)## в любом случае в клетку записывается новое число
                stechkin(i1,j1,"grey")##опять серая подсветка
                break
    for i in range(0,9):##снова пробегается по всем клеткам
        for j in range(0,9):
            if kletki[i][j][1].image[-1] == notsee[i*9 + j] != 0:##cчитает сколько правильных b-количество уже разгаданных
                b += 1
            if kletki[i][j][0].collidepoint(pos):##если мы нажали на новую клетку. то старые голубые стираются
                stechkin(i1,j1,"white")

                if kletki[i][j][0].image != "red":##если новая клетка не красная, то перекрашиваем ее в синюю
                    kletki[i][j][0].image = "blue"
                if kletki[i1][j1][0].image == "blue" and (i1 != i or j1 != j):##если клетка на которую мы теперь нажали не совпадает с предыдущей, то мы снимаем с нее синий цвет
                    kletki[i1][j1][0].image = "white"
                i1 = i
                j1 = j
                ## теперь задаем координаты новой синей клетки
                stechkin(i1,j1,"grey")## и соответственно подсвечиваем серым все то, что должно быть подсвечено(описано выше)
        
    if exit2.collidepoint(pos):
        sys.exit()
    if restart2.collidepoint(pos):
        startgame()
    if hint2.collidepoint(pos):
        if b != 81:
            suphint = random.choice(done)
            done.remove(suphint)
            asa = suphint[0]
            asa1 = suphint[1]
            kletki[asa][asa1][1]= Actor("mychislo" + notsee[asa*9+asa1], center = (50 + 3 + asa1 + 32 + asa1*64 + asa1//3*3, 50 + 3 + asa + 32 + asa*64 + asa//3*3))
            kletki[i1][j1][0].image = "white"
            stechkin(i1,j1,"white")
            i1 = asa
            j1 = asa1
            kletki[i1][j1][0].image = "blue"
            stechkin(i1,j1,"grey")
        
    if b == 81 :## если все клетки совпадают с задуманными, то мы победили и высвечивается картинка(ее координаты проосто меняются, поэтому она появляется)
        youwin2.x = WIDTH/2
        youwin2.y = 700/2

startgame()

def draw():
    screen.clear()##все убирает с поля
    screen.fill((0,0,0))##заполняет белым
    ##sudokupole.draw()
    if youwin2.x < 0:##если еще не высветилось что мы победили, то рисуются сначала фоны, потом сами картинки для чисеи и для каждой клетки
        for i in range(0,9):
            chisla[i][0].draw()
            chisla[i][1].draw()
            for j in range(0,9):
                kletki[i][j][0].draw()
                kletki[i][j][1].draw()
        exit2.draw()
        restart2.draw()
        hint2.draw()
    youwin2.draw()
pgzrun.go()
