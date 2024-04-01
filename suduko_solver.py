import time as t
import pyautogui as pg



grid = []
str_grid = []

while True:
    row = input('Row: ')
    dum = []

    for i in row:
        dum.append(int(i))
    grid.append(dum)

    if len(grid)==9:
        break
    t.sleep(0.2)
    print('row',len(grid),'completed')

t.sleep(3)


def print_board(gr):
    
    print()
    for i in range(len(gr)):
        if i%3==0 and i!=0:
            print("---------------------")
        for j in range(len(gr)):
            if j%3==0 and j!=0:
                print("|",end='')

            if j==8:
                print(gr[i][j])
            else:
                print(str(gr[i][j]),end=' ')
    print()

    for i in grid:
        for j in i:
            str_grid.append(str(j))

    count = []
    for num in str_grid:
        pg.press(num)
        pg.hotkey('right')
        count.append(num)
        if len(count)%9==0:
            pg.hotkey('down')
            for k in range(8):
                pg.hotkey('left')

def possible(row,col,num,gr):

    #check row
    for i in range(len(gr)):
        if gr[row][i]==num:
            return False

    #check col
    for i in range(len(gr)):
        if gr[i][col]==num:
            return False

    #check internal square
    
    x=(row//3)*3
    y=(col//3)*3

    for i in range(3):
        for j in range(3):
            if gr[x+i][y+j]==num:
                return False
    
    return True

    
def solve():
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y]==0:
                for i in range(1,10):
                    if possible(x,y,i,grid):
                        grid[x][y]=i
                        solve()
                        grid[x][y]=0
                return  
    print_board(grid)

solve()

