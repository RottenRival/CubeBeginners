from unittest import case
i=3
j=3
front = [['o' for a in range(j)] for c in range(i)]

back = [['r' for a in range(j)] for c in range(i)]
left = [['b' for a in range(j)] for c in range(i)]
right = [['g' for a in range(j)] for c in range(i)]
up = [['w' for a in range(j)] for c in range(i)]
down = [['y' for a in range(j)] for c in range(i)]

def print_state():

    print("FRONT(ORANGE)")
    for i in range(0,3):
        for j in range(0,3):
            if (j ==2):
                print(front[i][j])
            else:
                print(front[i][j],end=" ")
    print("\n")
    print("LEFT(BLUE)")
    for i in range(0,3):
        for j in range(0,3):
            if (j ==2):
                print(left[i][j])
            else:
                print(left[i][j],end=" ")
    print("\n")
    print("RIGHT(GREEN)")
    for i in range(0, 3):
        for j in range(0, 3):
            if (j == 2):
                print(right[i][j])
            else:
                print(right[i][j],end=" ")
    print("\n")
    print("UP(WHITE)")

    for i in range(0, 3):
        for j in range(0, 3):
            if (j == 2):
                print(up[i][j])
            else:
                print(up[i][j],end=" ")
    print("\n")
    print("BACK(RED)")
    for i in range(0, 3):
        for j in range(0, 3):
            if (j == 2):
                print(back[i][j])
            else:
                print(back[i][j],end=" ")
    print("\n")
    print("DOWN(YELLOW)")
    for i in range(0, 3):
        for j in range(0, 3):
            if (j == 2):
                print(down[i][j])
            else:
                print(down[i][j],end=" ")
    print("\n")


    """ print("BACK(RED):")
    for i in range(0,3):
        for j in  range(0,3):
            if j == 2:
                print(back[i][j])
            else:
                print(back[i][j], end=" ")
    print("\n")

    print("LEFT(BLUE):")
    for i in range(0,3):
        for j in  range(0,3):
            if j == 2:
                print(left[i][j])
            else:
                print(left[i][j], end=" ")
    print("\n")
    print("RIGHT(GREEN):")
    for i in range(0,3):
        for j in  range(0,3):
            if j == 2:
                print(right[i][j])
            else:
                print(right[i][j], end=" ")
    print("\n")
    print("UP(WHITE):")
    for i in range(0,3):
        for j in  range(0,3):
            if j == 2:
                print(up[i][j])
            else:
                print(up[i][j], end=" ")
    print("\n")
    print("DOWN(YELLOW):")
    for i in range(0,3):
        for j in  range(0,3):
            if j == 2:
                print(down[i][j])
            else:
                print(down[i][j], end=" ")
    print("\n")
    """


def l_prime():
    temp_1 = up[0][0]
    temp_2 = up[1][0]
    temp_3 = up[2][0]
    x = left[0][2]
    y = left[1][2]
    left[0][2] = left[2][2]
    left[2][2] = left[2][0]
    left[2][0] = left[0][0]
    left[0][0] = x
    left[1][1] = left[1][1]
    left[1][2] = left[2][1]
    left[2][1] = left[1][0]
    left[1][0] = left[0][1]
    left[0][1] = y
    up[0][0] = front[0][0]
    up[1][0] = front[1][0]
    up[2][0] = front[2][0]
    front[0][0] = down[0][0]
    front[1][0] = down[1][0]
    front[2][0] = down[2][0]
    down[0][0] = back[2][2]
    down[1][0] = back[1][2]
    down[2][0] = back[0][2]
    back[2][2] = temp_1
    back[1][2] = temp_2
    back[0][2] = temp_3



def l():
    temp_1 = front[0][0]
    temp_2 = front[1][0]
    temp_3 = front[2][0]
    x = left[0][2]
    y = left[1][2]
    left[0][2] = left[0][0]
    left[0][0] = left[2][0]
    left[2][0] = left[2][2]
    left[2][2] = x
    left[1][1] = left[1][1]
    left[1][2] = left[0][1]
    left[0][1] = left[1][0]
    left[1][0] = left[2][1]
    left[2][1] = y
    front[0][0] = up[0][0]
    front[1][0] = up[1][0]
    front[2][0] = up[2][0]
    up[0][0] = back[2][2]
    up[1][0] = back[1][2]
    up[2][0] = back[0][2]
    back[2][2] = down[0][0]
    back[1][2] = down[1][0]
    back[0][2] = down[2][0]
    down[0][0] = temp_1
    down[1][0] = temp_2
    down[2][0] = temp_3

def r():
    temp_1 = up[0][2]
    temp_2 = up[1][2]
    temp_3 = up[2][2]
    x = right[0][2]
    y = right[1][2]
    right[0][2] = right[0][0]
    right[0][0] = right[2][0]
    right[2][0] = right[2][2]
    right[2][2] = x
    right[1][1] = right[1][1]
    right[1][2] = right[0][1]
    right[0][1] = right[1][0]
    right[1][0] = right[2][1]
    right[2][1] = y

    up[0][2] = front[0][2]
    up[1][2] = front[1][2]
    up[2][2] = front[2][2]
    front[0][2] = down[0][2]
    front[1][2] = down[1][2]
    front[2][2] = down[2][2]
    down[0][2] = back[2][0]
    down[1][2] = back[1][0]
    down[2][2] = back[0][0]
    back[2][0] = temp_1
    back[1][0] = temp_2
    back[0][0] = temp_3


def r_prime():
    temp_1 = up[0][2]
    temp_2 = up[1][2]
    temp_3 = up[2][2]
    x = right[0][2]
    y = right[1][2]
    right[0][2] = right[2][2]
    right[2][2] = right[2][0]
    right[2][0] = right[0][0]
    right[0][0] = x
    right[1][1] = right[1][1]
    right[1][2] = right[2][1]
    right[2][1] = right[1][0]
    right[1][0] = right[0][1]
    right[0][1] = y
    up[0][2] = back[2][0]
    up[1][2] = back[1][0]
    up[2][2] = back[0][0]
    back[2][0] = down[0][2]
    back[1][0] = down[1][2]
    back[0][0] = down[2][2]
    down[0][2] = front[0][2]
    down[1][2] = front[1][2]
    down[2][2] = front[2][2]
    front[0][2] = temp_1
    front[1][2] = temp_2
    front[2][2] = temp_3




def u():
    temp_1 = front[0][0]
    temp_2 = front[0][1]
    temp_3 = front[0][2]
    x = up[0][2]
    y = up[1][2]
    up[0][2] = up[0][0]
    up[0][0] = up[2][0]
    up[2][0] = up[2][2]
    up[2][2] = x
    up[1][1] = up[1][1]
    up[1][2] = up[0][1]
    up[0][1] = up[1][0]
    up[1][0] = up[2][1]
    up[2][1] = y


    front[0][0] = right[0][0]

    front[0][1] = right[0][1]
    front[0][2] = right[0][2]

    right[0][0] = back[0][0]
    right[0][1] = back[0][1]
    right[0][2] = back[0][2]


    back[0][0] = left[0][0]
    back[0][1] = left[0][1]
    back[0][2] = left[0][2]

    left[0][0] = temp_1
    left[0][1] = temp_2
    left[0][2] = temp_3

def u_prime():

    temp_1 = front[0][0]
    temp_2 = front[0][1]
    temp_3 = front[0][2]
    x = up[0][2]
    y = up[1][2]
    up[0][2] = up[2][2]
    up[2][2] = up[2][0]
    up[2][0] = up[0][0]
    up[0][0] = x
    up[1][1] = up[1][1]
    up[1][2] = up[2][1]
    up[2][1] = up[1][0]
    up[1][0] = up[0][1]
    up[0][1] = y

    front[0][0] = left[0][0]
    front[0][1] = left[0][1]
    front[0][2] = left[0][2]

    left[0][0] = back[0][0]
    left[0][1] = back[0][1]
    left[0][2] = back[0][2]

    back[0][0] = right[0][0]
    back[0][1] = right[0][1]
    back[0][2] = right[0][2]
    right[0][0] = temp_1
    right[0][1] = temp_2
    right[0][2] = temp_3



def d():
    temp_1 = front[2][0]
    temp_2 = front[2][1]
    temp_3 = front[2][2]
    x = down[0][2]
    y = down[1][2]
    down[0][2] = down[0][0]
    down[0][0] = down[2][0]
    down[2][0] = down[2][2]
    down[2][2] = x
    down[1][1] = down[1][1]
    down[1][2] = down[0][1]
    down[0][1] = down[1][0]
    down[1][0] = down[2][1]
    down[2][1] = y

    front[2][0] = left[2][0]
    front[2][1] = left[2][1]
    front[2][2] = left[2][2]
    left[2][0] = back[2][0]
    left[2][1] = back[2][1]
    left[2][2] = back[2][2]
    back[2][0] = right[2][0]
    back[2][1] = right[2][1]
    back[2][2] = right[2][2]
    right[2][0] = temp_1
    right[2][1] = temp_2
    right[2][2] = temp_3



def d_prime():
    temp_1 = front[2][0]
    temp_2 = front[2][1]
    temp_3 = front[2][2]
    x = down[0][2]
    y = down[1][2]
    down[0][2] = down[2][2]
    down[2][2] = down[2][0]
    down[2][0] = down[0][0]
    down[0][0] = x
    down[1][1] = down[1][1]
    down[1][2] = down[2][1]
    down[2][1] = down[1][0]
    down[1][0] = down[0][1]
    down[0][1] = y
    front[2][0] = right[2][0]
    front[2][1] = right[2][1]
    front[2][2] = right[2][2]
    right[2][0] = back[2][0]
    right[2][1] = back[2][1]
    right[2][2] = back[2][2]
    back[2][0] = left[2][0]
    back[2][1] = left[2][1]
    back[2][2] = left[2][2]
    left[2][0] = temp_1
    left[2][1] = temp_2
    left[2][2] = temp_3

def m_1():
    temp_1 = up[0][1]
    temp_2 = up[1][1]
    temp_3 = up[2][1]
    up[0][1] = front[0][1]
    up[1][1] = front[1][1]
    up[2][1] = front[2][1]
    front[0][1] = down[0][1]
    front[1][1] = down[1][1]
    front[2][1] = down[2][1]
    down[0][1] = back[0][1]
    down[1][1] = back[1][1]
    down[2][1] = back[2][1]
    back[0][1] = temp_1
    back[1][1] = temp_2
    back[2][1] = temp_3


def m_1_prime():
    temp_1 = up[0][1]
    temp_2 = up[1][1]
    temp_3 = up[2][1]
    up[0][1] = back[0][1]
    up[1][1] = back[1][1]
    up[2][1] = back[2][1]
    back[0][1] = down[0][1]
    back[1][1] = down[1][1]
    back[2][1] = down[2][1]
    down[0][1] = front[0][1]
    down[1][1] = front[1][1]
    down[2][1] = front[2][1]
    front[0][1] = temp_1
    front[1][1] = temp_2
    front[2][1] = temp_3




def m_2():
    temp_1 = front[1][0]
    temp_2 = front[1][1]
    temp_3 = front[1][2]
    front[1][0] = left[1][0]
    front[1][1] = left[1][1]
    front[1][2] = left[1][2]
    right[1][0] = back[1][0]
    right[1][1] = back[1][1]
    right[1][2] = back[1][2]
    back[1][0] = left[1][0]
    back[1][1] = left[1][1]
    back[1][2] = left[1][2]
    left[1][0] = temp_1
    left[1][1] = temp_2
    left[1][2] = temp_3

def m_2_prime():
    temp_1 = front[1][0]
    temp_2 = front[1][1]
    temp_3 = front[1][2]
    front[1][0] = left[1][0]
    front[1][1] = left[1][1]
    front[1][2] = left[1][2]
    left[1][0] = back[1][0]
    left[1][1] = back[1][1]
    left[1][2] = back[1][2]
    back[1][0] = left[1][0]
    back[1][1] = left[1][1]
    back[1][2] = left[1][2]
    right[1][0] = temp_1
    right[1][1] = temp_2
    right[1][2] = temp_3



def b():
    temp_1 = up[0][0]
    temp_2 = up[0][1]
    temp_3 = up[0][2]
    x = back[0][2]
    y = back[1][2]
    back[0][2] = back[0][0]
    back[0][0] = back[2][0]
    back[2][0] = back[2][2]
    back[2][2] = x
    back[1][1] = back[1][1]
    back[1][2] = back[0][1]
    back[0][1] = back[1][0]
    back[1][0] = back[2][1]
    back[2][1] = y

    up[0][0] = right[0][2]
    up[0][1] = right[1][2]
    up[0][2] = right[2][2]
    right[0][2] = down[2][2]
    right[1][2] = down[2][1]
    right[2][2] = down[2][0]
    down[2][0] = left[0][0]
    down[2][1] = left[1][0]
    down[2][2] = left[2][0]
    left[2][0] = temp_1
    left[1][0] = temp_2
    left[0][0] = temp_3

def b_prime():
    temp_1 = up[0][0]
    temp_2 = up[0][1]
    temp_3 = up[0][2]
    x = back[0][2]
    y = back[1][2]
    back[0][2] = back[2][2]
    back[2][2] = back[2][0]
    back[2][0] = back[0][0]
    back[0][0] = x
    back[1][1] = back[1][1]
    back[1][2] = back[2][1]
    back[2][1] = back[1][0]
    back[1][0] = back[0][1]
    back[0][1] = y
    up[0][0] = left[2][0]
    up[0][1] = left[1][0]
    up[0][2] = left[0][0]
    left[0][0] = down[2][0]
    left[1][0] = down[2][1]
    left[2][0] = down[2][2]
    down[2][0] = right[2][2]
    down[2][1] = right[1][2]
    down[2][2] = right[0][2]
    right[0][2] = temp_1
    right[1][2] = temp_2
    right[2][2] = temp_3



def f():
    temp_1 = up[2][0]
    temp_2 = up[2][1]
    temp_3 = up[2][2]
    x = front[0][2]
    y = front[1][2]
    front[0][2] = front[0][0]
    front[0][0] = front[2][0]
    front[2][0] = front[2][2]
    front[2][2] = x
    front[1][1] = front[1][1]
    front[1][2] = front[0][1]
    front[0][1] = front[1][0]
    front[1][0] = front[2][1]
    front[2][1] = y

    up[2][0] = left[2][2]
    up[2][1] = left[1][2]
    up[2][2] = left[0][2]
    left[0][2] = down[0][0]
    left[1][2] = down[0][1]
    left[2][2] = down[0][2]
    down[0][0] = right[2][0]
    down[0][1] = right[1][0]
    down[0][2] = right[0][0]
    right[0][0] = temp_1
    right[1][0] = temp_2
    right[2][0] = temp_3

def f_prime():
    temp_1 = up[2][0]
    temp_2 = up[2][1]
    temp_3 = up[2][2]
    x = front[0][2]
    y = front[1][2]
    front[0][2] = front[2][2]
    front[2][2] = front[2][0]
    front[2][0] = front[0][0]
    front[0][0] = x
    front[1][1] = front[1][1]
    front[1][2] = front[2][1]
    front[2][1] = front[1][0]
    front[1][0] = front[0][1]
    front[0][1] = y
    up[2][0] = right[0][0]
    up[2][1] = right[1][0]
    up[2][2] = right[2][0]
    right[0][0] = down[0][2]
    right[1][0] = down[0][1]
    right[2][0] = down[0][0]
    down[0][0] = left[0][2]
    down[0][1] = left[1][2]
    down[0][2] = left[2][2]
    left[0][2] = temp_3
    left[1][2] = temp_2
    left[2][2] = temp_1



def u_m():
    temp_1 = up[1][0]
    temp_2 = up[1][1]
    temp_3 = up[1][2]
    up[1][0] = left[2][1]
    up[1][1] = left[1][1]
    up[1][2] = left[0][1]
    left[0][1] = down[1][0]
    left[1][1] = down[1][1]
    left[2][1] = down[1][2]
    down[1][0] = left[2][1]
    down[1][1] = left[1][1]
    down[1][2] = left[0][1]
    right[0][1] = temp_1
    right[1][1] = temp_2
    right[2][1] = temp_3




def u_m_prime():
    temp_1 = up[1][0]
    temp_2 = up[1][1]
    temp_3 = up[1][2]
    up[1][0] = left[0][1]
    up[1][1] = left[1][1]
    up[1][2] = left[2][1]
    right[0][1] = down[1][2]
    right[1][1] = down[1][1]
    right[2][1] = down[1][0]
    down[1][0] = left[0][1]
    down[1][1] = left[1][1]
    down[1][2] = left[2][1]
    left[0][1] = temp_1
    left[1][1] = temp_2
    left[2][1] = temp_3





def http_error(status):
    match status:
        case 'l':
            l()
            print_state()

        case 'lp':
            l_prime()
            print_state()

        case 'r':
            r()
            print_state()
        case 'rp':
            r_prime()
            print_state()
        case 'u':
            u()
            print_state()
        case 'up':
            u_prime()
            print_state()
        case 'f':
            f()
            print_state()
        case 'fp':
            f_prime()
            print_state()
        case 'b':
            b()
            print_state()
        case 'bp':
            b_prime()
            print_state()
        case 'm':
            m_1()
            print_state()
        case 'mp':
            m_1_prime()
            print_state()
        case 'd':
            d()
            print_state()
        case 'dp':
            d_prime()
            print_state()
        case 'um':
            u_m()
            print_state()
        case 'ump':
            u_m_prime()
            print_state()
        case 'm2':
            m_2()
            print_state()
        case 'm2p':
            m_2_prime()
            print_state()

# 1: l prime
# 2: l
# 3: r
# 4: r prime
# 5 :m1
# 6 : m1 prime, 7:u,8:u prime,9:d,10:d prime,11:m2,12:m2 prime
# 13: f, 14: f prime, 15:b,16:b prime,17:um2,18:um2 prime



for i in range(0,1000):
    inp = input("enter operation and click 0 to finish")
    if inp=='0':
        break
    http_error(inp)


print("Solving the cross ")
def white_cross():
    flag=False

    if ((up[0][1] == 'w') and (up[1][0] == 'w') and (up[2][1] == 'w') and (up[1][2] == 'w') and (front[0][1] == 'o') and (right[0][1] == 'g') and (back[0][1]=='r') and (left[0][1]=='b')):
        flag=True



    while flag == False:
        if up[2][1]=='w':
            if front[0][1]=='g':
                print("f2 d r2",end=" ")
                f()
                f()
                d()
                r()
                r()
                print_state()
            if front[0][1]=='b':
                print("f2 dp l2 ",end=" ")
                f()
                f()
                d_prime()
                l()
                l()
                print_state()
            if front[0][1]=='r':
                print("f2 d2 b2 ",end=" ")
                f()
                f()
                d()
                d()
                b()
                b()
                print_state()


        if up[0][1]=='w':

            if back[0][1]=='o':

                print("b2 d2 f2 ",end=" ")
                b()
                b()
                d()
                d()
                f()
                f()
                print_state()

            if back[0][1]=='b':
                print("b2 d l2 ",end=" ")
                b()
                b()
                d()
                l()
                l()
                print_state()

            if back[0][1]=='g':
                print("b2 dp r2 ",end=" ")
                b()
                b()
                d_prime()
                r()
                r()
                print_state()

        if up[1][2]=='w':
            if right[0][1]=='o':
                    print("r2 dp f2",end=" ")
                    r()
                    r()
                    d_prime()
                    f()
                    f()
                    print_state()
            if right[0][1]=='r':
                    print("r2 d b2",end=" ")
                    r()
                    r()
                    d()
                    b()
                    b()
                    print_state()
            if right[0][1]=='b':
                    print("r2 d2 l2",end=" ")
                    r()
                    r()
                    d()
                    d()
                    l()
                    l()
                    print_state()

        if up[1][0]=='w':
            if left[0][1]=='o':
                    print("l2 d f2",end=" ")
                    l()
                    l()
                    d()
                    f()
                    f()
                    print_state()
            if left[0][1]=='r':
                    print("l2 dp b2",end=" ")
                    l()
                    l()
                    d_prime()
                    b()
                    b()
                    print_state()
            if left[0][1]=='g':
                    print("l2 d2 r2",end=" ")
                    l()
                    l()
                    d()
                    d()
                    r()
                    r()
                    print_state()

        if front[0][1]=='w':
            if up[2][1]=='o':
                print("f up r u ",end=" ")
                f()
                u_prime()
                r()
                u()
                print_state()
            if up[2][1]=='r':
                print("f u r up ", end=" ")
                f()
                u()
                r()
                u_prime()
                print_state()
            if up[2][1]=='g':
                print("f r ", end=" ")
                f()
                r()
                print_state()
            if up[2][1]=='b':
                print("fp lp ", end=" ")
                f_prime()
                l_prime()

                print_state()

        if right[0][1]=='w':
            if up[1][2]=='r':
                print("r b ", end=" ")
                r()
                b()

                print_state()
            if up[1][2] == 'o':
                print("rp fp ", end=" ")
                r_prime()
                f_prime()

                print_state()
            if up[1][2] == 'b':
                print("r2 d2 l2 ")
                r()
                r()
                d()
                d()
                l()
                l()

                print_state()
            if up[1][2] == 'g':
                print("rp u fp up ", end=" ")
                r_prime()
                u()
                f_prime()
                u_prime()

                print_state()

        if left[0][1]=='w':
            if up[1][0]=='o':
                print("l f ", end=" ")
                l()
                f()

                print_state()
            if up[1][0] == 'r':
                print("lp bp ", end=" ")
                l_prime()
                b_prime()

                print_state()
            if up[1][0] == 'g':
                print("l u f up ", end=" ")

                l()
                u()
                f()
                u_prime()

                print_state()

                print_state()
            if up[1][0] == 'b':
                print("l up f u ", end=" ")
                l()
                u_prime()
                f()
                u()

                print_state()

        if back[0][1]=='w':
            if up[0][1]=='g':
                print("bp rp ", end=" ")
                b_prime()
                r_prime()

                print_state()
            if up[0][1]=='b':
                print("b l ", end=" ")
                b()
                l()

                print_state()
            if up[0][1]=='o':
                print("b2 dp r fp rp ", end=" ")
                b()
                b()
                d_prime()
                r()
                f_prime()

                r_prime()

                print_state()
            if up[0][1]=='r':
                print("bp u rp up ", end=" ")
                b_prime()
                u()
                r_prime()
                u_prime()

                print_state()



        if front[1][2]=='w':
            if right[1][0]=='o':
                print("rp dp r f2",end=" ")
                r_prime()
                d_prime()
                r()
                f()
                f()
                print_state()
            if right[1][0]=='g':
                print("r",end=" ")
                r()
                print_state()

            if right[1][0]=='b':
                print("rp d2 l2 r",end=" ")
                r_prime()
                d()
                d()
                l()
                l()
                r()
                print_state()
            if right[1][0]=='r':
                print("u r up",end=" ")
                u()
                r()
                u_prime()
                print_state()

        if right[1][2]=='w':
            if back[1][0]=='o':
                print("bp d2 f2 b",end=" ")
                b_prime()
                d()
                d()
                f()
                f()
                b()
                print_state()
            if back[1][0]=='r':
                print("b",end=" ")
                b()
                print_state()
            if back[1][0]=='g':
                print("bp dp b r2",end=" ")
                b_prime()
                d_prime()
                b()
                r()
                r()
                print_state()
            if back[1][0]=='b':
                print("bp d b l2",end=" ")
                b_prime()
                d()
                b()
                l()
                l()
                print_state()

        if back[1][2]=='w':
            if left[1][0]=='o':
                print("lp d l f2",end=" ")
                l_prime()
                d()
                l()
                f()
                f()
                print_state()
            if left[1][0]=='g':
                print("lp d2 l r2",end=" ")
                l_prime()
                d()
                d()
                l()
                r()
                r()
                print_state()
            if left[1][0]=='b':
                print("lp",end=" ")
                l_prime()
                print_state()
            if left[1][0]=='r':
                print("lp dp l b2",end=" ")
                l_prime()
                d_prime()
                l()
                b()
                b()
                print_state()

        if left[1][2]=='w':
            if front[1][0]=='o':
                print("f",end=" ")
                f()
                print_state()
            if front[1][0]=='g':
                print("l d lp fp r f",end=" ")
                l()
                d()
                l_prime()
                f_prime()
                r()
                f()
                print_state()
            if front[1][0]=='r':
                print("fp d2 f b2",end=" ")
                f_prime()
                d()
                d()
                f()
                b()
                b()
                print_state()
            if front[1][0]=='b':
                print("up f u",end=" ")
                u_prime()
                f()
                u()
                print_state()

        if front[1][0]=='w':
            if left[1][2]=='o':
                print("l d lp f2",end=" ")
                l()
                d()
                l_prime()
                f()
                f()
                print_state()
            if left[1][2]=='g':
                print("l d2 lp r2",end=" ")
                l()
                d()
                d()
                l_prime()
                r()
                r()
                print_state()
            if left[1][2]=='b':
                print("lp",end=" ")
                l_prime()
                print_state()
            if left[1][2]=='r':
                print("l dp lp b2",end=" ")
                l()
                d_prime()
                l_prime()
                b()
                b()
                print_state()

        if right[1][0]=='w':
            if front [1][2]=='o':
                print("fp",end=" ")
                f_prime()
                print_state()
            if front [1][2]=='g':
                print("f d fp r2",end=" ")
                f()
                d()
                f_prime()
                r()
                r()
                print_state()
            if front [1][2]=='b':
                print("f dp fp l2",end=" ")
                f()
                d_prime()
                f_prime()
                l()
                l()
            if front [1][2]=='r':
                print("f d2 fp b2",end=" ")
                f()
                d()
                d()
                f_prime()
                b()
                b()
                print_state()

        if back[1][0]=='w':
            if right[1][2]=='o':
                print("r dp rp f2",end=" ")
                r()
                d_prime()
                r_prime()
                f()
                f()
                print_state()
            if right[1][2]=='g':
                print("rp",end=" ")
                r_prime()
                print_state()
            if right[1][2]=='b':
                print("r d2 rp l2",end=" ")
                r()
                d()
                d()
                r_prime()
                l()
                l()
                print_state()
            if right[1][2]=='r':
                print("r d rp b2",end=" ")
                r()
                d()
                r_prime()
                b()
                b()
                print_state()

        if left[1][0]=='w':
            if back[1][2]=='o':
                print("b d2 bp f2",end=" ")
                b()
                d()
                d()
                b_prime()
                f()
                f()
                print_state()
            if back[1][2]=='g':
                print("b dp bp r2",end=" ")
                b()
                d_prime()
                b_prime()
                r()
                r()
                print_state()
            if back[1][2]=='b':
                print("b d bp l2",end=" ")
                b()
                d()
                b_prime()
                l()
                l()
            if back[1][2]=='r':
                print("bp",end=" ")
                b_prime()
                print_state()


        if front[2][1]=='w':
            if down[0][1]=='o':
                print("fp up r u",end=" ")
                f_prime()
                u_prime()
                r()
                u()
                print_state()
            if down[0][1]=='g':
                print("fp r f",end=" ")
                f_prime()
                r()
                f()
                print_state()
            if down[0][1]=='b':
                print("f lp fp",end=" ")
                f()
                l_prime()
                f_prime()
            if down[0][1]=='r':
                print("u fp r f up ",end=" ")
                u()
                f_prime()
                r()
                f()
                u_prime()

        if right[2][1]=='w':
            if down[1][2]=='o':
                print("r fp rp",end=" ")
                r()
                f_prime()
                r_prime()
                print_state()
            if down[1][2]=='g':
                print("r u fp up",end=" ")
                r()
                u()
                f_prime()
                u_prime()
                print_state()
            if down[1][2]=='b':
                print("r up fp u rp",end=" ")
                r()
                u_prime()
                f_prime()
                u()
                r_prime()
                print_state()
            if down[1][2]=='r':
                print("rp b r",end=" ")
                r_prime()
                b()
                r()
                print_state()

        if back[2][1]=='w':
            if down[2][1]=='o':
                print("b up rp u bp",end=" ")
                b()
                u_prime()
                r_prime()
                u()
                b_prime()
                print_state()
            if down[2][1]=='g':
                print("b rp bp",end=" ")
                b()
                r_prime()
                b_prime()
                print_state()
            if down[2][1]=='b':
                print("bp l b",end=" ")
                b_prime()
                l()
                b()
                print_state()
            if down[2][1]=='r':
                print("b u rp up",end=" ")
                b()
                u()
                r_prime()
                u_prime()
                print_state()

        if left[2][1]=='w':
            if down[1][0]=='o':
                print("lp f l",end=" ")
                l_prime()
                f()
                l()
                print_state()
            if down[1][0]=='g':
                print("d fp r f",end=" ")
                d()
                f_prime()
                r()
                f()
                print_state()
            if down[1][0]=='b':
                print("lp up f u",end=" ")
                l_prime()
                u_prime()
                f()
                u()
                print_state()
            if down[1][0]=='r':
                print("l bp lp",end=" ")
                l()
                b_prime()
                l_prime()
                print_state()
        if down[0][1]=='w':
            if front[2][1]=='o':
                print("f2",end=" ")
                f()
                f()
                print_state()
            if front[2][1]=='g':
                print("d r2",end=" ")
                d()
                r()
                r()
                print_state()
            if front[2][1]=='b':
                print("dp l2",end=" ")
                d_prime()
                l()
                l()
                print_state()
            if front[2][1]=='r':
                print("d2 b2",end=" ")
                d()
                d()
                b()
                b()
                print_state()
        if down[1][2]=='w':
            if right[2][1]=='o':
                print("dp f2",end=" ")
                d_prime()
                f()
                f()
                print_state()
            if right[2][1]=='g':
                print("r2",end=" ")
                r()
                r()
                print_state()
            if right[2][1]=='b':
                print("d2 l2",end=" ")
                d()
                d()
                l()
                l()
                print_state()
            if right[2][1]=='r':
                print("d b2",end=" ")
                d()
                b()
                b()
                print_state()
        if down[2][1]=='w':
            if back[2][1]=='o':
                print("d2 f2",end=" ")
                d()
                d()
                f()
                f()
                print_state()
            if back[2][1]=='g':
                print("dp r2",end=" ")
                d_prime()
                r()
                r()
                print_state()
            if back[2][1]=='b':
                print("d l2",end=" ")
                d()
                l()
                l()
                print_state()
            if back[2][1]=='r':
                print("b2",end=" ")
                b()
                b()
                print_state()

        if down[1][0]=='w':
            if left[2][1]=='o':
                print("d f2",end=" ")
                d()
                f()
                f()
                print_state()
            if left[2][1]=='g':
                print("d2 r2",end=" ")
                d()
                d()
                r()
                r()
                print_state()
            if left[2][1]=='b':
                print("l2",end=" ")
                l()
                l()
                print_state()
            if left[2][1]=='r':
                print("dp b2",end=" ")
                d_prime()
                b()
                b()
                print_state()
        if ((up[0][1] == 'w') and (up[1][0] == 'w') and (up[2][1] == 'w') and (up[1][2] == 'w') and (front[0][1] == 'o') and (right[0][1] == 'g') and (back[0][1] == 'r') and (left[0][1] == 'b')):
            flag=True


white_cross()

def first_layer():
    flag2=False
    if ((up[0][0]=='w') and (up[0][2]=='w') and (up[2][0]=='w') and (up[2][2]=='w') and (front[0][0]=='o') and (front[0][2]=='o') and (right[0][0]=='g') and (right[0][2]=='g') and (back[0][0]=='r') and (back[0][2]=='r') and (left[0][0]=='b') and (left[0][2]=='b')):
        flag2=True

    while flag2==False:
        if front[2][2]=='w':
            if right[2][0]=='g':
                print("dp rp d r",end=" ")
                d_prime()
                r_prime()
                d()
                r()
                print_state()
            if right[2][0]=='r':
                print("bp d b",end=" ")
                b_prime()
                d()
                b()
                print_state()
            if right[2][0]=='o':
                print("d2 fp d f",end=" ")
                d()
                d()
                f_prime()
                d()
                f()
                print_state()
            if right[2][0]=='b':
                print("lp d2 l",end=" ")
                l_prime()
                d()
                d()
                l()
                print_state()

        if right[2][0]=='w':
            if front[2][2]=='o':
                print("rp dp r",end=" ")
                r_prime()
                d_prime()
                r()
                print_state()
            if front[2][2]=='g':
                print("d bp dp b ",end=" ")
                d()
                b_prime()
                d_prime()
                b()
                print_state()
            if front[2][2]=='r':
                print("d2 lp dp l",end=" ")
                d()
                d()
                l_prime()
                d_prime()
                l()
                print_state()
            if front[2][2]=='b':
                print("dp fp dp f",end=" ")
                d_prime()
                f_prime()
                d_prime()
                f()
                print_state()

        if down[0][2]=='w':
            if front[2][2]=='g':
                print("rp d2 r d rp dp r",end=" ")
                r_prime()
                d()
                d()
                r()
                d()
                r_prime()
                d_prime()
                r()
                print_state()
            if front[2][2]=='r':
                print("d bp d2 b d bp dp b")
                d()
                b_prime()
                d()
                d()
                b()
                d()
                b_prime()
                d_prime()
                b()
                print_state()
                print_state()
            if front[2][2]=='o':
                print("dp fp d2 f d fp dp f",end=" ")
                d_prime()
                f_prime()
                d()
                d()
                f()
                d()
                f_prime()
                d_prime()
                f()
                print_state()
            if front[2][2]=='b':
                print("d2 lp d2 l d lp dp l",end=" ")
                d()
                d()
                l_prime()
                d()
                d()
                l()
                d()
                l_prime()
                d_prime()
                l()
                print_state()

        if left[2][2]=='w':
            if front[2][0]=='g':
                print("rp d r",end=" ")
                r_prime()
                d()
                r()
                print_state()
            if front[2][0]=='o':
                print("dp fp d f",end=" ")
                d_prime()
                f_prime()
                d()
                f()
                print_state()
            if front[2][0]=='r':
                print("d bp d b",end=" ")
                d()
                b_prime()
                d()
                b()
                print_state()
            if front[2][0]=='b':
                print("d2 lp d l",end=" ")
                d()
                d()
                l_prime()
                d()
                l()
                print_state()

        if front[2][0]=='w':
            if down[0][0]=='g':
                print("d rp dp r",end=" ")
                d()
                r_prime()
                d_prime()
                r()
                print_state()
            if down[0][0]=='o':
                print("fp dp f",end=" ")
                f_prime()
                d_prime()
                f()
                print_state()
            if down[0][0]=='r':
                print("d2 bp dp",end=" ")
                d()
                d()
                b_prime()
                d_prime()
                print_state()
            if down[0][0]=='b':
                print("b dp bp",end=" ")
                b()
                d_prime()
                b_prime()
                print_state()

        if down[0][0]=='w':
            if front[2][0]=='o':
                print("d rp d2 r d rp dp r",end=" ")
                d()
                r_prime()
                d()
                d()
                r()
                d()
                r_prime()
                d_prime()
                r()
                print_state()
            if front[2][0]=='g':
                print("d2 bp d2 b d bp dp b",end=" ")
                d()
                d()
                b_prime()
                d()
                d()
                b()
                d()
                b_prime()
                d_prime()
                b()
                print_state()
            if front[2][0]=='b':
                print("fp d2 f d fp dp f",end=" ")
                f_prime()
                d()
                d()
                f()
                d()
                f_prime()
                d_prime()
                f()
                print_state()
            if front[2][0]=='r':
                print("dp lp d2 l d lp dp l",end=" ")
                d_prime()
                l_prime()
                d()
                d()
                l()
                d()
                l_prime()
                d_prime()
                l()
                print_state()

        if right[2][2]=='w':
            if down[2][2]=='o':
                print("d2 rp d r",end=" ")
                d()
                d()
                r_prime()
                d()
                r()
                print_state()
            if down[2][2]=='g':
                print("dp bp d b",end=" ")
                d_prime()
                b_prime()
                d()
                b()
                print_state()
            if down[2][2]=='b':
                print("d fp d f",end=" ")
                d()
                f_prime()
                d()
                f()
                print_state()
            if down[2][2]=='r':
                print("lp d l",end=" ")
                l_prime()
                d()
                l()
                print_state()

        if back[2][0]=='w':
            if right[2][2]=='o':
                print("dp rp dp r",end=" ")
                d_prime()
                r_prime()
                d_prime()
                r()
                print_state()
            if right[2][2]=='g':
                print("bp dp b",end=" ")
                b_prime()
                d_prime()
                b()
                print_state()
            if right[2][2]=='b':
                print("d2 fp dp f",end=" ")
                d()
                d()
                f_prime()
                d_prime()
                f()
                print_state()
            if right[2][2]=='r':
                print("d lp dp l",end=" ")
                d()
                l_prime()
                d_prime()
                l()
                print_state()

        if down[2][2]=='w':
            if right[2][2]=='g':
                print("dp rp d2 r d rp dp r")
                d_prime()
                r_prime()
                d()
                d()
                r()
                d()
                r_prime()
                d_prime()
                r()
                print_state()
            if right[2][2]=='o':
                print("d2 fp d2 f d fp dp f",end=" ")
                d()
                d()
                f_prime()
                d()
                d()
                f()
                d()
                f_prime()
                d_prime()
                f()
                print_state()
            if right[2][2]=='b':
                print("d lp d2 l d lp dp l",end=" ")
                d()
                l_prime()
                d()
                d()
                l()
                d()
                l_prime()
                d_prime()
                l()
                print_state()
            if right[2][2]=='r':
                print("bp d2 b d bp dp b",end=" ")
                b_prime()
                d()
                d()
                b()
                d()
                b_prime()
                d_prime()
                b()
                print_state()

        if back[2][2]=='w':
            if down[2][0]=='o':
                print("d rp d r",end=" ")
                d()
                r_prime()
                d()
                r()
                print_state()
            if down[2][0]=='b':
                print("fp d f",end=" ")
                f_prime()
                d()
                f()
                print_state()
            if down[2][0]=='g':
                print("d2 bp d b",end=" ")
                d()
                d()
                b_prime()
                d()
                b()
                print_state()
            if down[2][0]=='r':
                print("dp lp d l",end=" ")
                d_prime()
                l_prime()
                d()
                l()
                print_state()

        if left[2][0]=='w':
            if down[2][0]=='g':
                print("d2 rp dp r",end=" ")
                d()
                d()
                r_prime()
                d_prime()
                r()
                print_state()
            if down[2][0]=='o':
                print("d fp dp f",end=" ")
                d()
                f_prime()
                d_prime()
                f()
                print_state()
            if down[2][0]=='b':
                print("lp dp l",end=" ")
                l_prime()
                d_prime()
                l()
                print_state()
            if down[2][0]=='r':
                print("dp bp dp b",end=" ")
                d_prime()
                b_prime()
                d_prime()
                b()
                print_state()

        if down[2][0]=='w':
            if left[2][0]=='o':
                print("d2 rp d2 r d rp dp r",end=" ")
                d()
                d()
                r_prime()
                d()
                d()
                r()
                d()
                r_prime()
                d_prime()
                r()
                print_state()
            if left[2][0]=='g':
                print("dp bp d2 b d bp dp b",end=" ")
                d_prime()
                b_prime()
                d()
                d()
                b()
                d()
                b_prime()
                d_prime()
                b()
                print_state()
            if left[2][0]=='b':
                print("d fp d2 f d fp dp f",end=" ")
                d()
                f_prime()
                d()
                d()
                f()
                d()
                f_prime()
                d_prime()
                f()
                print_state()
            if left[2][0]=='r':
                print("lp d2 l d lp dp l",end=" ")
                l_prime()
                d()
                d()
                l()
                d()
                l_prime()
                d_prime()
                l()
                print_state()

        if front[0][2]=='w':
            if right[0][0]=='o':
                print("f d fp d2 rp d r",end=" ")
                f()
                d()
                f_prime()
                d()
                d()
                r_prime()
                d()
                r()
                print_state()
            if right[0][0]=='b':
                print("f d fp d fp d f",end=" ")
                f()
                d()
                f_prime()
                d()
                f_prime()
                d()
                f()
                print_state()
            if right[0][0]=='g':
                print("f d fp dp bp d b",end=" ")
                f()
                d()
                f_prime()
                d_prime()
                b_prime()
                d()
                b()
                print_state()
            if right[0][0]=='r':
                print("f d fp lp d l",end=" ")
                f()
                d()
                f_prime()
                l_prime()
                d()
                l()
                print_state()

        if right[0][0]=='w':
            if front[0][2]=='o':
                print("rp dp r fp dp f",end=" ")
                r_prime()
                d_prime()
                r()
                f_prime()
                d_prime()
                f()
                print_state()
            if front[0][2]=='g':
                print("rp dp r d rp dp r",end=" ")
                r_prime()
                d_prime()
                r()
                d()
                r_prime()
                d_prime()
                r()
                print_state()
            if front[0][2]=='b':
                print("rp d2 r lp dp l",end=" ")
                r_prime()
                d()
                d()
                r()
                l_prime()
                d_prime()
                l()
                print_state()
            if front[0][2]=='r':
                print("rp dp r d2 bp dp b",end=" ")
                r_prime()
                d_prime()
                r()
                d()
                d()
                b_prime()
                d_prime()
                b()
                print_state()




        if right[0][2]=='w':
            if up[0][2]=='r':
                print("bp dp b d bp d2 b d bp dp b",end=" ")
                b_prime()
                d_prime()
                b()
                d()
                b_prime()
                d()
                d()
                b()
                d()
                b_prime()
                d_prime()
                b()
                print_state()
            if up[0][2]=='o':
                print("r d rp fp d f",end=" ")
                r()
                d()
                r_prime()
                f_prime()
                d()
                f()
                print_state()
            if up[0][2]=='g':
                print("r d2 r2 d r",end=" ")
                r()
                d()
                d()
                r()
                r()
                d()
                r()
                print_state()
            if up[0][2]=='b':
                print("r d rp dp lp d l",end=" ")
                r()
                d()
                r_prime()
                d_prime()
                l_prime()
                d()
                l()
                print_state()

        if back[0][2]=='w':
            if left[0][0]=='r':
                print("b d2 bp d lp d l")
                b()
                d()
                d()
                b_prime()
                d()
                l_prime()
                d()
                l()
                print_state()
            if left[0][0]=='b':
                print("b d bp dp fp d f")
                b()
                d()
                b_prime()
                d_prime()
                f_prime()
                d()
                f()
                print_state()
            if left[0][0]=='o':
                print("b d bp d bp d b")
                b()
                d()
                b_prime()
                d()
                b_prime()
                d()
                b()
                print_state()
            if left[0][0]=='g':
                print("b d2 b2 d b")
                b()
                d()
                d()
                b()
                b()
                d()
                b()
                print_state()
        if left[0][2]=='w':
            if front[0][0]=='b':
                print("l d lp d2 fp d f")
                l()
                d()
                l_prime()
                d()
                d()
                f_prime()
                d()
                f()
                print_state()
            if front[0][0]=='o':
                print("l d lp dp rp d r")
                l()
                d()
                l_prime()
                d_prime()
                r_prime()
                d()
                r()
                print_state()
            if front[0][0]=='g':
                print("l d lp bp d b")
                l()
                d()
                l_prime()
                b_prime()
                d()
                b()
                print_state()
            if front[0][0]=='r':
                print("l d l2 d2 l")
                l()
                d()
                l()
                l()
                d()
                d()
                l()
                print_state()

        if back[0][0]=='w':
            if up[0][2]=='o':
                print("bp dp b rp dp r",end=" ")
                b_prime()
                d_prime()
                b()
                r_prime()
                d_prime()
                r()
                print_state()
            if up[0][2]=='g':
                print("bp dp b d bp dp b",end=" ")
                b_prime()
                d_prime()
                b()
                d()
                b_prime()
                d_prime()
                b()
                print_state()
            if up[0][2]=='b':
                print("bp d2 b fp dp f",end=" ")
                b_prime()
                d()
                d()
                b()
                f_prime()
                d_prime()
                f()
                print_state()
            if up[0][2]=='r':
                print("bp d2 b dp lp dp l",end=" ")
                b_prime()
                d()
                d()
                b()
                d_prime()
                l_prime()
                d_prime()
                l()
                print_state()


        if up[0][2]=='w':
            if right[0][2]=='o':
                print("bp d2 b rp d r",end=" ")
                b_prime()
                d()
                d()
                b()
                r_prime()
                d()
                r()
                print_state()
            if right[0][2]=='b':
                print("bp d2 b dp fp d f",end=" ")
                b_prime()
                d()
                d()
                b()
                d_prime()
                f_prime()
                d()
                f()
                print_state()
            if right[0][2]=='r':
                print("bp dp b d lp d l")
                b_prime()
                d_prime()
                b()
                d()
                l_prime()
                d()
                l()
                print_state()
                print_state()
                

        if up[2][2]=='w':
            if right[0][0]=='b':
                print("rp d2 r b d bp",end=" ")
                r_prime()
                d()
                d()
                r()
                b()
                d()
                b_prime()
                print_state()
            if right[0][0]=='o':
                print("rp d2 r fp d f",end=" ")
                r_prime()
                d()
                d()
                r()
                f_prime()
                d()
                f()
                print_state()
            if right[0][0]=='r':
                print("rp dp r d bp d b",end=" ")
                r_prime()
                d_prime()
                r()
                d()
                b_prime()
                d()
                b()
                print_state()

        if up[2][0]=='w':
            if front[0][0]=='g':
                print("l d lp rp dp r",end=" ")
                l()
                d()
                l_prime()
                r_prime()
                d_prime()
                r()
                print_state()
            if front[0][0]=='b':
                print("l d2 lp d lp dp l",end=" ")
                l()
                d()
                d()
                l_prime()
                d()
                l_prime()
                d_prime()
                l()
                print_state()

            if front[0][0]=='r':
                print("l d2 lp d r dp rp",end=" ")
                l()
                d()
                d()
                l_prime()
                d()
                r()
                d_prime()
                r_prime()
                print_state()

        if up[0][0]=='w':
            if left[0][0]=='g':
                print("lp d2 l dp rp d r",end=" ")
                l_prime()
                d()
                d()
                l()
                d_prime()
                r_prime()
                d()
                r()
                print_state()
            if left[0][0]=='o':
                print("lp d2 l d2 fp d f")

            if left[0][0]=='r':
                print("lp d2 l bp d b",end=" ")
                l_prime()
                d()
                d()
                l()
                b_prime()
                d()
                b()
                print_state()

        if right[0][0]=='w':
            if front[0][2]=='g':
                print("rp dp r d rp dp r",end=" ")
                r_prime()
                d_prime()
                r()
                d()
                r_prime()
                d_prime()
                r()
                print_state()
            if front[0][2]=='r':
                print("rp dp r d2 bp dp b",end=" ")
                r_prime()
                d_prime()
                r()
                d()
                d()
                b_prime()
                d_prime()
                b()
                print_state()
            if front[0][2]=='o':
                print("rp dp r fp dp f",end=" ")
                r_prime()
                d_prime()
                r()
                f_prime()
                d_prime()
                f()
                print_state()
                print_state()
            if front[0][2]=='b':
                print("rp d2 r lp dp l",end=" ")
                r_prime()
                d()
                d()
                r()
                l_prime()
                d_prime()
                l()
                print_state()

        if front[0][0]=='w':
            if left[0][2]=='g':
                print("fp d2 f dp rp dp r",end=" ")
                f_prime()
                d()
                d()
                f()
                d_prime()
                r_prime()
                d_prime()
                r()
                print_state()
            if left[0][2]=='o':
                print("fp dp f d fp dp f",end=" ")
                f_prime()
                d_prime()
                f()
                d()
                f_prime()
                d_prime()
                f()
                print_state()
            if left[0][2]=='r':
                print("fp d2 f bp dp b",end=" ")
                f_prime()
                d()
                d()
                f()
                b_prime()
                d_prime()
                b()
                print_state()
            if left[0][2]=='b':
                print("fp dp f lp dp l",end=" ")
                f_prime()
                d_prime()
                f()
                l_prime()
                d_prime()
                l()
                print_state()
        if back[0][0]=='w':
            if right[0][2]=='g':
                print("bp dp b rp dp r",end=" ")
                b_prime()
                d_prime()
                b()
                r_prime()
                d_prime()
                r()
                print_state()
            if right[0][2]=='o':
                print("bp d2 b fp dp f",end=" ")
                b_prime()
                d()
                d()
                b()
                f_prime()
                d_prime()
                f()
                print_state()
            if right[0][2]=='r':
                print("bp dp b d bp dp b",end=" ")
                b_prime()
                d_prime()
                b()
                d()
                b_prime()
                d_prime()
                b()
                print_state()
            if right[0][2]=='b':
                print("bp d2 b dp lp dp l",end=" ")
                b_prime()
                d()
                d()
                b()
                d_prime()
                l_prime()
                d_prime()
                l()
                print_state()

        if left[0][0]=='w':
            if back[0][2]=='g':
                print("lp d2 l rp dp r",end=" ")
                l_prime()
                d()
                d()
                l()
                r_prime()
                d_prime()
                r()
                print_state()
            if back[0][2]=='o':
                print("lp d2 l dp fp dp f",end=" ")
                l_prime()
                d()
                d()
                l()
                d_prime()
                f_prime()
                d_prime()
                f()
                print_state()
            if back[0][2]=='r':
                print("lp d l bp dp b",end=" ")
                l_prime()
                d()
                l()
                b_prime()
                d_prime()
                b()
                print_state()
            if back[0][2]=='b':
                print("lp dp l d lp dp l",end=" ")
                l_prime()
                d_prime()
                l()
                d()
                l_prime()
                d_prime()
                l()
                print_state()
        if ((up[0][0] == 'w') and (up[0][2] == 'w') and (up[2][0] == 'w') and (up[2][2] == 'w') and (front[0][0] == 'o') and (front[0][2] == 'o') and (right[0][0] == 'g') and (right[0][2] == 'g') and (back[0][0] == 'r') and (back[0][2] == 'r') and (left[0][0] == 'b') and (left[0][2] == 'b')):
            flag2 = True


first_layer()
print("Solving the middle layer.Flip the cube so that white is facing down and yellow is facing up keeping orange as the front face")
def middle_layer():
    flag_3=False
    if (front[1][0]=='o') and (front[1][2]=='o') and (right[1][0]=='g' and right[1][2]=='g') and (left[1][0]=='b') and (left[1][2]=='b') and (back[1][0]=='r') and (back[1][2]=='r'):
        flag_3=True

    def ob():
        print("keeping the orange side as the front face with yellow on top:")
        print("u r up rp up fp u f", end=" ")
        d()
        l()
        d_prime()
        l_prime()
        d_prime()
        f_prime()
        d()
        f()
        print_state()

    def og():
        print("keeping the orange side as the front face with yellow on top:")
        print("up lp u l u f up fp", end=" ")
        d_prime()
        r_prime()
        d()
        r()
        d()
        f()
        d_prime()
        f_prime()
        print_state()

    def bo():
        print("keeping the blue side as the front face with yellow on top:")
        print("up lp u l u f up fp", end=" ")
        d_prime()
        f_prime()
        d()
        f()
        d()
        l()
        d_prime()
        l_prime()
        print_state()

    def br():
        print("keeping the blue side as the front face with yellow on top:")
        print("u r up rp up fp u f", end=" ")
        d()
        b()
        d_prime()
        b_prime()
        d_prime()
        l_prime()
        d()
        l()
        print_state()

    def go():
        print("turn the cube such that green is facing front with yellow on top:")
        print("u r up rp up fp u f", end=" ")

        d()
        f()
        d_prime()
        f_prime()
        d_prime()
        r_prime()
        d()
        r()
        print_state()

    def gr():
        print("turn the cube such that green is facing front with yellow on top:")
        print("up lp u l u f up fp", end=" ")

        d_prime()
        b_prime()
        d()
        b()
        d()
        r()
        d_prime()
        r_prime()
        print_state()

    def rb():
        print("turn the cube such that red is facing front with yellow on top:")
        print("up lp u l u f up fp", end=" ")
        d_prime()
        l_prime()
        d()
        l()
        d()
        b()
        d_prime()
        b_prime()
        print_state()

    def rg():
        print("turn the cube such that red is facing front with yellow on top:")
        print("u r up rp up fp u f", end=" ")
        d()
        r()
        d_prime()
        r_prime()
        d_prime()
        b_prime()
        d()
        b()
        print_state()

    while flag_3==False:
        if front[2][1]=='o':
            if down[0][1]=='b':

                ob()
            if down[0][1]=='g':

                og()
        if left[2][1]=='b':
            if down[1][0]=='o':

                bo()
            if down[1][0]=='r':

                br()

        if right[2][1] == 'g':
            if down[1][2] == 'o':

                go()
            if down[1][2]=='r':

                gr()
        if back[2][1]=='r':
            if down[2][1]=='b':

                rb()
            if down[2][1]=='g':

                rg()
        if down[0][1]=='o':
            if front[2][1]=='b':
                print("up")
                d_prime()
                bo()
            if front[2][1]=='g':
                print("u")
                d()
                go()
        if down[1][0]=='b':
            if left[2][1]=='o':
                print("u")
                d()
                ob()
            if left[2][1]=='r':
                print("up")
                d_prime()
                rb()
        if down[1][2]=='g':
            if right[2][1]=='o':
                print("up")
                d_prime()
                og()
            if right[2][1]=='r':
                print("u")
                d()
                rg()
        if down[2][1]=='r':
            if back[2][1]=='b':
                print("u")
                d()
                br()
            if back[2][1]=='g':
                print("up")
                d_prime()
                print_state()
                gr()
        if front[2][1]=='g':
            if down[0][1]=='r':
                print("u")
                d()
                gr()
        if left[2][1]=='o':
            if down[1][2]=='g':
                print("up")
                d_prime()
                og()
        if right[2][1]=='o':
            if down[1][0]=='b':
                print("u")
                d()
                ob()
        if back[2][1]=='o':
            if down[2][1]=='g':
                print("u2")
                d()
                d()
                og()
            if down[2][1]=='b':
                print("u2")
                d()
                d()
                ob()
        if back[2][1]=='b':
            if down[2][1]=='o':
                print("u")
                d()
                bo()
        if back[2][1]=='g':
            if down[2][1]=='o':
                print("up")
                d_prime()
                go()

        if front[1][0]=='b':
            if left[1][2]=='o':
                print("holding the orange side as the front face with yellow on top:")
                print("u r up rp up fp u f u2",end=" ")
                ob()
            if left[1][2]=='r':
                print("holding the orange side as the front face with yellow on top:")
                print("u r up rp up fp u f", end=" ")
                rb()
        if front[1][0]=='g':
            if left[1][2]=='o':
                print("holding the orange side as the front face with yellow on top:")
                print("u r up rp up fp u f u2", end=" ")
                d()
                l()
                d_prime()
                l_prime()
                d_prime()
                f_prime()
                d()
                f()
                d()
                d()
                og()
            if left[1][2]=='r':
                print("holding the orange side as the front face with yellow on top:")
                print("u r up rp up fp u f", end=" ")
                d()
                l()
                d_prime()
                l_prime()
                d_prime()
                f_prime()
                d()
                f()
                rg()
        if front[1][0]=='o':
            if left[1][2]=='g':
                print("holding the orange side as the front face with yellow on top:")
                print("u r up rp up fp u f up", end=" ")
                d()
                l()
                d_prime()
                l_prime()
                d_prime()
                f_prime()
                d()
                f()
                d_prime()
                go()

        if front[1][0] == 'r':
            if left[1][2]=='b':
                print("holding the orange side as the front face with yellow on top:")
                print("u r up rp up fp u f u", end=" ")
                d()
                l()
                d_prime()
                l_prime()
                d_prime()
                f_prime()
                d()
                f()
                d()
                br()
            if left[1][2]=='g':
                print("holding the orange side as the front face with yellow on top:")
                print("u r up rp up fp u f up", end=" ")
                d()
                l()
                d_prime()
                l_prime()
                d_prime()
                f_prime()
                d()
                f()
                d_prime()
                gr()



        if front[1][2]=='g':
            if right[1][0]=='o':
                print("holding the green side as the front face with yellow on top:")
                print("u r up rp up fp u f u2", end=" ")
                d()
                f()
                d_prime()
                f_prime()
                d_prime()
                r_prime()
                d()
                r()
                d()
                d()
                go()
            if right[1][0]=='r':
                print("holding the green side as the front face with yellow on top:")
                print("u r up rp up fp u f u2", end=" ")
                d()
                f()
                d_prime()
                f_prime()
                d_prime()
                r_prime()
                d()
                r()
                d()
                d()
                gr()
        if front[1][2]=='o':
            if right[1][0]=='b':
                print("holding the green side as the front face with yellow on top:")
                print("u r up rp up fp u f u", end=" ")
                d()
                f()
                d_prime()
                f_prime()
                d_prime()
                r_prime()
                d()
                r()
                d()
                ob()
        if front[1][2]=='b':
            if right[1][0]=='o':
                print("holding the green side as the front face with yellow on top:")
                print("u r up rp up fp u f", end=" ")
                d()
                f()
                d_prime()
                f_prime()
                d_prime()
                r_prime()
                d()
                r()
                bo()
            if right[1][0]=='r':
                print("holding the green side as the front face with yellow on top:")
                print("u r up rp up fp u f", end=" ")
                d()
                f()
                d_prime()
                f_prime()
                d_prime()
                r_prime()
                d()
                r()
                br()
        if front[1][2]=='r':
            if right[1][0]=='g':
                print("holding the green side as the front face with yellow on top:")
                print("u r up rp up fp u f up", end=" ")
                d()
                f()
                d_prime()
                f_prime()
                d_prime()
                r_prime()
                d()
                r()
                d_prime()
                rg()
            if right[1][0]=='b':
                print("holding the green side as the front face with yellow on top:")
                print("u r up rp up fp u f up", end=" ")
                d()
                f()
                d_prime()
                f_prime()
                d_prime()
                r_prime()
                d()
                r()
                d_prime()
                rb()

        if right[1][2]=='g':
            if back[1][0]=='o':
                print("holding the red side as the front face with yellow on top:")
                print("u r up rp up fp u f u", end=" ")
                d()
                r()
                d_prime()
                r_prime()
                d_prime()
                b_prime()
                d()
                b()
                d()
                go()
        if right[1][2]=='o':
            if back[1][0]=='g':
                print("holding the red side as the front face with yellow on top:")
                print("u r up rp up fp u f", end=" ")
                d()
                r()
                d_prime()
                r_prime()
                d_prime()
                b_prime()
                d()
                b()
                og()
            if back[1][0]=='b':
                print("holding the red side as the front face with yellow on top:")
                print("u r up rp up fp u f", end=" ")
                d()
                r()
                d_prime()
                r_prime()
                d_prime()
                b_prime()
                d()
                b()
                ob()
        if right[1][2]=='b':
            if back[1][0]=='o':
                print("holding the red side as the front face with yellow on top:")
                print("u r up rp up fp u f up", end=" ")
                d()
                r()
                d_prime()
                r_prime()
                d_prime()
                b_prime()
                d()
                b()
                d_prime()
                bo()
            if back[1][0]=='r':
                print("holding the red side as the front face with yellow on top:")
                print("u r up rp up fp u f up", end=" ")
                d()
                r()
                d_prime()
                r_prime()
                d_prime()
                b_prime()
                d()
                b()
                d_prime()
                br()
        if right[1][2]=='r':
            if back[1][0]=='g':
                print("holding the red side as the front face with yellow on top:")
                print("u r up rp up fp u f u2", end=" ")
                d()
                r()
                d_prime()
                r_prime()
                d_prime()
                b_prime()
                d()
                b()
                d()
                d()
                rg()
            if back[1][0]=='b':
                print("holding the red side as the front face with yellow on top:")
                print("u r up rp up fp u f u2", end=" ")
                d()
                r()
                d_prime()
                r_prime()
                d_prime()
                b_prime()
                d()
                b()
                d()
                d()
                rb()


        if left[1][0]=='g':
            if back[1][2]=='o':
                print("holding the blue side as the front face with yellow on top:")
                print("u r up rp up fp u f up", end=" ")
                d()
                b()
                d_prime()
                b_prime()
                d_prime()
                l_prime()
                d()
                l()
                d_prime()
                og()
            if back[1][2]=='r':
                print("holding the blue side as the front face with yellow on top:")
                print("u r up rp up fp u f u", end=" ")
                d()
                b()
                d_prime()
                b_prime()
                d_prime()
                l_prime()
                d()
                l()
                d()
                rg()
        if left[1][0]=='o':
            if back[1][2]=='g':
                print("holding the blue side as the front face with yellow on top:")
                print("u r up rp up fp u f", end=" ")
                d()
                b()
                d_prime()
                b_prime()
                d_prime()
                l_prime()
                d()
                l()
                go()
            if back[1][2]=='b':
                print("holding the blue side as the front face with yellow on top:")
                print("u r up rp up fp u f u2", end=" ")
                d()
                b()
                d_prime()
                b_prime()
                d_prime()
                l_prime()
                d()
                l()
                d()
                d()
                bo()
        if left[1][0]=='b':
            if back[1][2]=='o':
                print("holding the blue side as the front face with yellow on top:")
                print("u r up rp up fp u f up", end=" ")
                d()
                b()
                d_prime()
                b_prime()
                d_prime()
                l_prime()
                d()
                l()
                d_prime()
                ob()
        if left[1][0]=='r':
            if back[1][2]=='g':
                print("holding the blue side as the front face with yellow on top:")
                print("u r up rp up fp u f", end=" ")
                d()
                b()
                d_prime()
                b_prime()
                d_prime()
                l_prime()
                d()
                l()
                gr()
            if back[1][2]=='b':
                print("holding the blue side as the front face with yellow on top:")
                print("u r up rp up fp u f u2", end=" ")
                d()
                b()
                d_prime()
                b_prime()
                d_prime()
                l_prime()
                d()
                l()
                d()
                d()
                br()
        if front[2][1]=='r':
            if down[0][1] == 'g':
                print("u2")
                d()
                d()
                rg()
                print_state()

            if down[0][1]=='b':
                print("u2")
                d()
                d()
                rb()
                print_state()

        if right[2][1]=='b':
            if down[1][2]=='o':
                print("u2")
                d()
                d()
                bo()
                print_state()

            if down[1][2]=='r':
                print("u2")
                d()
                d()
                br()
                print_state()

        if left[2][1]=='g':
            if down[1][0]=='o':
                print("u2")
                d()
                d()
                go()
                print_state()

            if down[1][0]=='r':
                print("u2")
                d()
                d()
                gr()
                print_state()
        if (front[1][0] == 'o') and (front[1][2] == 'o') and (right[1][0] == 'g' and right[1][2] == 'g') and (
                left[1][0] == 'b') and (left[1][2] == 'b') and (back[1][0] == 'r') and (back[1][2] == 'r'):
            flag_3 = True




middle_layer()

print("solving the yellow cross")
def yellow_cross():
    flag_5=False
    if down[0][1] == 'y' and down[1][0] == 'y' and down[1][2] == 'y' and down[2][1] == 'y':
        flag_5=True
    while flag_5==False:
        if down[0][1] == 'y' and down[1][0] == 'y' and down[1][2] == 'y' and down[2][1] == 'y':
            flag_5 = True

        if down[0][1]!='y' and down[1][0]!='y' and down[1][2]!='y' and down[2][1]!='y':
            print("holding the orange side as the front face with yellow on top:")
            print("f r u rp up fp")
            f()
            l()
            d()
            l_prime()
            d_prime()
            f_prime()
            print_state()

            if down[0][1]=='y' and down[1][0]=='y':
                print("holding the orange side as the front face with yellow on top:")
                print("u2 f u r up rp fp")
                d()
                d()
                f()
                d()
                l()
                d_prime()
                l_prime()
                f_prime()
                print_state()
                break
            if down[0][1]=='y' and down[1][2]=='y':
                print("holding the orange side as the front face with yellow on top:")
                print("u f u r up rp fp")
                d()
                f()
                d()
                l()
                d_prime()
                l_prime()
                f_prime()
                print_state()
                break
            if down[1][0]=='y' and down[2][1]=='y':
                print("holding the orange side as the front face with yellow on top:")
                print("up f u r up rp fp")
                d_prime()
                f()
                d()
                l()
                d_prime()
                l_prime()
                f_prime()
                print_state()
                break
            if down[2][1]=='y' and down[1][2]=='y':
                print("holding the orange side as the front face with yellow on top:")
                print("f u r up rp fp")

                f()
                d()
                l()
                d_prime()
                l_prime()
                f_prime()
                print_state()
                break

        if down[0][1] == 'y' and down[1][0] == 'y':
            print("holding the orange side as the front face with yellow on top:")
            print("u2 f u r up rp fp")
            d()
            d()
            f()
            d()
            l()
            d_prime()
            l_prime()
            f_prime()
            print_state()
            break
        if down[0][1] == 'y' and down[1][2] == 'y':
            print("holding the orange side as the front face with yellow on top:")
            print("u f u r up rp fp")
            d()
            f()
            d()
            l()
            d_prime()
            l_prime()
            f_prime()
            print_state()
            break
        if down[1][0] == 'y' and down[2][1] == 'y':
            print("holding the orange side as the front face with yellow on top:")
            print("up f u r up rp fp")
            d_prime()
            f()
            d()
            l()
            d_prime()
            l_prime()
            f_prime()
            print_state()
            break
        if down[2][1] == 'y' and down[1][2] == 'y':
            print("holding the orange side as the front face with yellow on top:")
            print("f u r up rp fp")

            f()
            d()
            l()
            d_prime()
            l_prime()
            f_prime()
            print_state()
            break
        if down[0][1]=='y' and down[2][1]=='y':
            print("holding the orange side as the front face with yellow on top:")
            print("u f r u rp up fp")
            d()
            f()
            l()
            d()
            l_prime()
            d_prime()
            f_prime()
            print_state()
            break
        if down[1][0]=='y' and down[1][2]=='y':
            print("holding the orange side as the front face with yellow on top:")
            print("f r u rp up fp")

            f()
            l()
            d()
            l_prime()
            d_prime()
            f_prime()
            print_state()
            break

yellow_cross()
print("solving the last layer")
def last_layer():
    def ob():
        print("holding the green side as the front face with yellow on top:")
        print('r u rp u r u2 rp u')
        f()
        d()
        f_prime()
        d()
        f()
        d()
        d()
        f_prime()
        d()
        print_state()
    def og():
        print("holding the red side as the front face with yellow on top:")
        print('r u rp u r u2 rp u')
        r()
        d()
        r_prime()
        d()
        r()
        d()
        d()
        r_prime()
        d()
        print_state()
    def orange_red():
        print("holding the orange side as the front face with yellow on top:")
        print('r u rp u r u2 rp')
        l()
        d()
        l_prime()
        d()
        l()
        d()
        d()
        l_prime()

        print_state()
    def gr():
        print("holding the blue side as the front face with yellow on top:")
        print('r u rp u r u2 rp u')
        b()
        d()
        b_prime()
        d()
        b()
        d()
        d()
        b_prime()
        d()
        print_state()

    def bg():
        print("holding the green side as the front face with yellow on top:")
        print('r u rp u r u2 rp')
        f()
        d()
        f_prime()
        d()
        f()
        d()
        d()
        f_prime()

        print_state()
    def br():
        print("holding the orange side as the front face with yellow on top:")
        print('r u rp u r u2 rp u')
        l()
        d()
        l_prime()
        d()
        l()
        d()
        d()
        l_prime()
        d()

        print_state()
    flag_6=False

    if front[2][1]=='o' and right[2][1]=='g' and back[2][1]=='r' and left[2][1]=='b':
        flag_6=True

    while flag_6==False:

        if front[2][1]=='o':
            if left[2][1]=='b':
                ob()
                break

            if right[2][1]=='g':
                og()
                break
            if back[2][1]=='r':
                orange_red()
                ob()
                break
        if right[2][1]=='g':
            if back[2][1]=='r':
                gr()
                break
            if left[2][1]=='b':
                bg()
                og()
                break

        if left[2][1]=='b':
            if back[2][1]=='r':
                br()
                break
        if right[2][1]=='o':
            if front[2][1]=='b':
                print("up")
                d_prime()
                ob()
                break
            if back[2][1]=='g':
                print("up")
                d_prime()
                og()
                break
            if left[2][1]=='r':
                print("up")
                d_prime()
                orange_red()
                ob()
                break
        if left[2][1]=='o':
            if front[2][1]=='g':
                print("u")
                d()
                og()
                break
            if back[2][1]=='b':
                print("u")
                d()
                ob()
                break
            if right[2][1]=='r':
                print("u")
                d()
                orange_red()
                ob()
                break
        if back[2][1]=='o':
            if left[2][1]=='g':
                print("u2")
                d()
                d()
                og()
                break
            if right[2][1]=='b':
                print("u2")
                d()
                d()
                ob()
                break
            if front[2][1]=='r':
                print("u2")
                d()
                d()
                orange_red()
                ob()
                break
        if front[2][1]=='g':
            if right[2][1]=='r':
                print("u")
                d()
                gr()
                break
            if left[2][1]=='o':
                print("u")
                d()
                og()
                break
            if back[2][1]=='b':
                print("u")
                d()
                bg()
                og()
                break
        if back[2][1]=='g':
            if right[2][1]=='o':
                print("up")
                d_prime()
                og()
                break
            if left[2][1]=='r':
                print("up")
                d_prime()
                gr()
                break
            if front[2][1]=='b':
                print("up")
                d_prime()
                bg()
                og()
                break
        if left[2][1]=='g':
            if front[2][1]=='r':
                print("u2")
                d()
                d()
                gr()
                break
            if back[2][1]=='o':
                print("u2")
                d()
                d()
                og()
                break
            if right[2][1]=='b':
                print("u2")
                d()
                d()
                bg()
                og()
                break
        if front[2][1]=='b':
            if left[2][1]=='r':
                print("up")
                d_prime()
                br()
                break
            if right[2][1]=='o':
                print("up")
                d_prime()
                ob()
                break
            if back[2][1]=='g':
                print("up")
                d_prime()

                bg()
                og()
                break
        if back[2][1]=='b':
            if right[2][1]=='r':
                print("u")
                d()
                br()
                break
            if left[2][1]=='o':
                print("u")
                d()
                ob()
                break
            if front[2][1]=='g':
                print("u")
                d()
                bg()
                og()
                break
        if right[2][1]=='b':
            if front[2][1]=='r':
                print("u2")
                d()
                d()
                br()
                break
            if back[2][1]=='o':
                print("u2")
                d()
                d()
                ob()
                break
            if left[2][1]=='g':
                print("u2")
                d()
                d()
                bg()
                og()
                break
        if right[2][1]=='r':
            if front[2][1]=='g':
                print("u")
                d()
                gr()
                break
            if back[2][1]=='b':
                print("u")
                d()
                br()
                break
            if left[2][1]=='o':
                print("u")
                d()
                orange_red()
                ob()
                break
        if left[2][1]=='r':
            if front[2][1]=='b':
                print("up")
                d_prime()
                br()
                break
            if back[2][1]=='g':
                print("up")
                d_prime()
                gr()
                break
            if right[2][1]=='o':
                print("up")
                d_prime()
                orange_red()
                ob()
                break
        if front[2][1]=='r':
            if right[2][1]=='b':
                print("u2")
                d()
                d()
                br()
                break
            if left[2][1]=='g':
                print("u2")
                d()
                d()
                gr()
                break
            if back[2][1]=='o':
                print("u2")
                d()
                d()
                orange_red()
                ob()
                break
        if front[2][1] == 'o' and right[2][1] == 'g' and back[2][1] == 'r' and left[2][1] == 'b':
            flag_6 = True
last_layer()
e=0
w=0
g=0
h=0
if (front[2][0]=='o' or front[2][0]=='b' or front[2][0]=='y') and (left[2][2]=='b' or left[2][2]=='o' or left[2][2]=='y') and (down[0][0]=='o' or down[0][0]=='b' or down[0][0]=='y'):
    e=1
if (front[2][2]=='o' or front[2][2]=='g' or front[2][2]=='y') and (right[2][0]=='o' or right[2][0]=='g' or right[2][0]=='y') and (down[0][2]=='o' or down[0][2]=='g' or down[0][2]=='y'):
    w=1
if (right[2][2]=='g' or right[2][2]=='r' or right[2][2]=='y') and (back[2][0]=='g' or back[2][0]=='r' or back[2][0]=='y') and (down[2][2]=='g' or down[2][2]=='r' or down[2][2]=='y'):
    g=1
if (back[2][2]=='r' or back[2][2]=='b' or back[2][2]=='y') and (left[2][0]=='r' or left[2][0]=='b' or left[2][0]=='y') and (down[2][0]=='r' or down[2][0]=='b' or down[2][0]=='y'):
    h=1


def orient():

    def yob():
        if (front[2][0]=='o' or front[2][0]=='b' or front[2][0]=='y') and (left[2][2]=='b' or left[2][2]=='o' or left[2][2]=='y') and (down[0][0]=='o' or down[0][0]=='b' or down[0][0]=='y'):


            print("holding the orange side as the front face with yellow on top")
            print("u r up lp u rp up l")
            d()
            l()
            d_prime()
            r_prime()
            d()
            l_prime()
            d_prime()
            r()
            print_state()

    def yog():
        if (front[2][2]=='o' or front[2][2]=='g' or front[2][2]=='y') and (right[2][0]=='o' or right[2][0]=='g' or right[2][0]=='y') and (down[0][2]=='o' or down[0][2]=='g' or down[0][2]=='y'):
            print("holding the green side as the front face with yellow on top")
            print("u r up lp u rp up l")
            d()
            f()
            d_prime()
            b_prime()
            d()
            f_prime()
            d_prime()
            b()
            print_state()

    def ygr():
        if (right[2][2]=='g' or right[2][2]=='r' or right[2][2]=='y') and (back[2][0]=='g' or back[2][0]=='r' or back[2][0]=='y') and (down[2][2]=='g' or down[2][2]=='r' or down[2][2]=='y'):
            print("holding the red side as the front face with yellow on top")
            print("u r up lp u rp up l")
            d()
            r()
            d_prime()
            l_prime()
            d()
            r_prime()
            d_prime()
            l()
            print_state()
    def ybr():
        if (back[2][2]=='r' or back[2][2]=='b' or back[2][2]=='y') and (left[2][0]=='r' or left[2][0]=='b' or left[2][0]=='y') and (down[2][0]=='r' or down[2][0]=='b' or down[2][0]=='y'):
            print("holding the blue side as the front face with yellow on top")
            print("u r up lp u rp up l")
            d()
            b()
            d_prime()
            f_prime()
            d()
            b_prime()
            d_prime()
            f()
            print_state()


    flag_8=False




    while flag_8==False:
        if ((front[2][0] == 'o' or front[2][0] == 'b' or front[2][0] == 'y') and (left[2][2] == 'b' or left[2][2] == 'o' or left[2][2] == 'y') and (down[0][0] == 'o' or down[0][0] == 'b' or down[0][0] == 'y')) and ((front[2][2] == 'o' or front[2][2] == 'g' or front[2][2] == 'y') and (right[2][0] == 'o' or right[2][0] == 'g' or right[2][0] == 'y') and (down[0][2] == 'o' or down[0][2] == 'g' or down[0][2] == 'y')) and ((right[2][2] == 'g' or right[2][2] == 'r' or right[2][2] == 'y') and (back[2][0] == 'g' or back[2][0] == 'r' or back[2][0] == 'y') and (down[2][2] == 'g' or down[2][2] == 'r' or down[2][2] == 'y')) and ((back[2][2] == 'r' or back[2][2] == 'b' or back[2][2] == 'y') and (left[2][0] == 'r' or left[2][0] == 'b' or left[2][0] == 'y') and (down[2][0] == 'r' or down[2][0] == 'b' or down[2][0] == 'y')):
            flag_8=True
            continue


        if (front[2][0] == 'o' or front[2][0] == 'b' or front[2][0] == 'y') and (left[2][2] == 'b' or left[2][2] == 'o' or left[2][2] == 'y') and (down[0][0] == 'o' or down[0][0] == 'b' or down[0][0] == 'y'):
            yob()
            continue

        if (front[2][2] == 'o' or front[2][2] == 'g' or front[2][2] == 'y') and (right[2][0] == 'o' or right[2][0] == 'g' or right[2][0] == 'y') and (down[0][2] == 'o' or down[0][2] == 'g' or down[0][2] == 'y'):
            yog()
            continue

        if (right[2][2] == 'g' or right[2][2] == 'r' or right[2][2] == 'y') and (back[2][0] == 'g' or back[2][0] == 'r' or back[2][0] == 'y') and (down[2][2] == 'g' or down[2][2] == 'r' or down[2][2] == 'y'):
            ygr()
            continue

        if (back[2][2] == 'r' or back[2][2] == 'b' or back[2][2] == 'y') and (left[2][0] == 'r' or left[2][0] == 'b' or left[2][0] == 'y') and (down[2][0] == 'r' or down[2][0] == 'b' or down[2][0] == 'y'):
            ybr()
            continue

        if e==0 and w==0 and g==0 and h==0:
            print("holding the orange side as the front face with yellow on top:")
            print("u r up lp u rp up up l")
            d()
            l()
            d_prime()
            r_prime()
            d()
            l_prime()
            d_prime()
            r()
            print_state()
            continue


orient()
def rdrd():
    if (down[0][0]=='y' and down[2][2]=='y') or (down[0][2]=='y' and down[2][0]=='y'):
        if (front[2][2]=='y' and left[2][0]=='y') or (right[2][2]=='y' and front[2][0]=='y') or (back[2][2]=='y' and right[2][0]=='y') or (left[2][2]=='y' and back[2][0]=='y'):
            print("holding one yellow corner on the right as the front face with yellow on top:")
            print("rp dp r d rp dp r d rp dp r d rp dp r d u2 rp dp r d rp dp r d")
    if (front[2][0]=='y' and front[2][2]=='y') or (right[2][0]=='y' and right[2][2]=='y') or (left[2][0]=='y' and left[2][2]=='y') or (back[2][0]=='y' and back[2][2]=='y'):
        if ((down[0][0]=='y' and down[0][2]=='y') or (down[0][2]=='y' and down[2][2]=='y') or (down[0][0]=='y' and down[2][0]=='y') or (down[2][0]=='y' and down[2][2]=='y')):
            print("holding the headlights to the right with yellow on top:")
            print("rp dp r d rp dp r d u rp dp r d rp dp r d rp dp r d rp dp r d")

    if down[0][0]!='y' and down[0][2]!='y' and down[2][0]!='y' and down[2][2]!='y':
        print("holding the headlights to the right:")
        print("(rp dp r d)x2 u (rp dp r d)x4 u (rp dp r d)x4 u (rp dp r d)x2")

    if down[0][0]=='y' or down[0][2]=='y' or down[2][0]=='y' or down[2][2]=='y':
        if (front[2][2]=='y' and left[2][2]=='y' and back[2][2]=='y') or (right[2][2]=='y' and front[2][2]=='y' and left[2][2]=='y') or (left[2][2]=='y' and back[2][2]=='y' and right[2][2]=='y') or (back[2][2]=='y' and right[2][2]=='y' and front[2][2]=='y'):
            print("holding the leftmost yellow corner to the right:")
            print("(rp dp r d)x2 u (rp dp r d)x2 u (rp dp r d)x2")
        if (front[2][0]=='y' and left[2][0]=='y' and back[2][0]=='y') or (right[2][0]=='y' and front[2][0]=='y' and left[2][0]=='y') or (left[2][0]=='y' and back[2][0]=='y' and right[2][0]=='y') or (back[2][0]=='y' and right[2][0]=='y' and front[2][0]=='y'):
            print("holding the rightmost yellow corner as the front face:")
            print("(rp dp r d)x4 u (rp dp r d)x4 u (rp dp r d)x4 ")



rdrd()






























                
            
            
                    
                
                
                
                
                



















































