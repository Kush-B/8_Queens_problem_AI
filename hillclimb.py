import random
import math

class st:
    global h_
#   constructor initializing size, data, and h for the board.
    def __init__(self, sz, data=None):
        self.sz = sz
        self.data = data
        self.h = -1
    
# initial config for board
    def gen_initial(self):
        brd_s=[]
        for i in range(int(self.sz)):
            col=[None]*int(self.sz)
            r = random.randint(0,int(self.sz)-1)
            for j in range(int(self.sz)):
                if j == r:
                    col[j]='Q'
                else:
                    col[j]='-'
            brd_s.append(col)
        self.data = brd_s
        
        return self.data
    
#  generate new board and change position of queens
    def gen_new(self, old_position, new_position):
        x = new_position[0]
        y = new_position[1] 
        old_x = old_position[0]
        old_y = old_position[1]
        
        next = self.copy(self.data)
        
        for i in range(0, len(next)):
            for j in range(0, len(next)):
                if i==x and j==y:
                    next[i][j]='Q'

                if i==old_x and j==old_y:
                    next[i][j]='-'
        return next
    
#function to copy positions to new board..
    def copy(self,previous):
        cpy_board=[]
        
        for i in previous:
            sqrs=[]
            for j in i:
                sqrs.append(j)
            cpy_board.append(sqrs)
        return cpy_board
 
    def h_calculate(self):
        counter=0
                    
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i][j]=='Q':
                    pos = [None]*2
                    pos[0]=i
                    pos[1]=j
                    v,d = self.findAttkPosition(pos)

                    for k in range(len(self.data)):
                        for l in range(len(self.data)):
                                if self.data[k][l]=='Q':
                                    for e in v:
                                        if e[0] == k and e[1] == l:
                                            counter+=1
                                    for e in d:
                                        if e[0] == k and e[1] == l:
                                            counter+=1
        return math.ceil(counter/2)
        
#Attack Positions..    
    def findAttkPosition(self,pos): 
        vertical = []#vertical attack positions    
        x=pos[0]
        y=pos[1]
        
        if x==0:
            while(x < len(self.data)-1):
                v_attk=[None]*2
                x+=1

                v_attk[0]=x
                v_attk[1]=y
                vertical.append(v_attk)
        
        elif x==len(self.data):
            while(x>=0):
                v_attk=[None]*2
                x-=1

                v_attk[0]=x
                v_attk[1]=y
                vertical.append(v_attk)
        
        else:
            while(x < len(self.data)-1):
                v_attk=[None]*2
                x+=1

                v_attk[0]=x
                v_attk[1]=y
                vertical.append(v_attk)
                
            x=pos[0]
            y=pos[1]
                
            while(x>=0):
                v_attk=[None]*2
                x-=1

                v_attk[0]=x
                v_attk[1]=y
                vertical.append(v_attk)
                
        diagonal = []#diagonal attack positions
        x=pos[0]
        y=pos[1]  
        #Check top left squares
        while x>0 and x<len(self.data) and y>0 and y<len(self.data):
            d_attack=[None]*2
            x-=1
            y-=1
            d_attack[0]=x
            d_attack[1]=y
            diagonal.append(d_attack)
        x=pos[0]
        y=pos[1]    
        #Check bottom left squares
        while x>=0 and x<len(self.data)-1 and y>0 and y<len(self.data):
            d_attack=[None]*2
            x+=1
            y-=1
            d_attack[0]=x
            d_attack[1]=y
            diagonal.append(d_attack)
            
        x=pos[0]
        y=pos[1]
        # Check top right squares
        while x>0 and x<len(self.data) and y>=0 and y<len(self.data)-1:
            d_attack=[None]*2
            x-=1
            y+=1

            d_attack[0]=x
            d_attack[1]=y
            diagonal.append(d_attack)
        
        x=pos[0]
        y=pos[1]
        #Check bottom right squares
        while x>=0 and x<len(self.data)-1 and y>=0 and y<len(self.data)-1:
            d_attack=[None]*2
            x+=1
            y+=1

            d_attack[0]=x
            d_attack[1]=y
            diagonal.append(d_attack) 
        
        return vertical, diagonal
    
class brd:
    
    def __init__(self):
        self.succs = 0
        self.fails = 0
        self.stps = 0
        self.t_s_stps = 0
        self.t_f_stps = 0
        self.count_init = 0

#   find position of queen in row
    def fnd_rPos(self,data,r_num):    
        for j in range(len(data)):
            if data[r_num][j] == 'Q':
                pos = [None]*2
                pos[0]= r_num
                pos[1]= j     
                break
        return pos
    
#   main
    def main(self):
#       Call for Hill-Climbing search.
        print("Hill-Climbing search:")
        for x in range(int(1000)):
            self.stps = 0
            self.cal_brd(x)
        print()
        print("---------------------------------------------")
        print()
        print("Hill-Climbing search: ")
        print("Success Ratio: ", 100*self.succs/int(1000),"%")
        print("Failure Ratio: ", 100*self.fails/int(1000), "%")
        if self.succs == 0:
            print("Number of steps for successes:", self.t_s_stps)
        else:
            print("Average steps for successes: ", self.t_s_stps/self.succs)
        if self.fails == 0:
            print("Number of steps for failure:", self.t_f_stps)
        else:
            print("Average steps for failures: ", self.t_f_stps/self.fails)
        print()

#   Hill-Climbing search.    
    def cal_brd(self, call):
        h_=-1
        
        in_brd = st(8)
        in_brd.data = in_brd.gen_initial()
        in_brd.h = in_brd.h_calculate()
        if call < 4:
            print("Sequence for searching..." + str(call+1) + ":")
            print("Initial state:")
            for x in in_brd.data:
                for y in x:
                    print(y, end=" ")
                print()
            print("h: ", in_brd.h)
            print()

        min_brd = in_brd.data
        while h_ !=0:
            store_m_h_pos = []
            prev_brd = st(8, min_brd)
            prev_brd.h = prev_brd.h_calculate()
            h_ = prev_brd.h
            for i in range(int(8)):
                pos = self.fnd_rPos(prev_brd.data,i)
                for j in range(int(8)):
                    n_position = [None]*2
                    n_position[0]=i
                    n_position[1]=j
                    if n_position == pos:
                        continue    

                    succ_brd = st(8)
                    succ_brd.data = prev_brd.gen_new(pos, n_position)
                    succ_brd.h = succ_brd.h_calculate()

                    if succ_brd.h <= h_:
                        h_ = succ_brd.h
                        store_pos =n_position
                        store_pos.append(succ_brd.h)
                        store_m_h_pos.append(store_pos)
                        
            if store_m_h_pos:            
                l = len(store_m_h_pos)-1
                while l>=0:
                    y = store_m_h_pos[l]
                    if y[2] != h_:
                        del store_m_h_pos[l]
                    l-=1

                r = random.randint(0,len(store_m_h_pos)-1)
                positon_ = store_m_h_pos[r]
                del positon_[2]
                parent_pps = self.fnd_rPos(prev_brd.data,positon_[0])
                min_brd = prev_brd.gen_new(parent_pps, positon_)

            if h_ == prev_brd.h:
                if h_ == 0:
                    if call < 4:
                        print("Found the Solution!!!")
                    self.succs +=1
                else:
                    self.t_f_stps +=self.stps
                    if call < 4:
                        for x in min_brd:
                            for y in x:
                                print(y, end=" ")

                            print()
                        print("h: " + str(h_))
                        print()
                        print("No solution found!")
                        print()
                    self.fails +=1
                break

            else:
                self.stps +=1
                if call < 4:
                    print("New State:")
                    for x in min_brd:
                        for y in x:
                            print(y, end=" ")

                        print()
                    print("h:", h_)
                    print()

                if h_==0:
                    self.t_s_stps += self.stps
                    if call < 4:
                        print("Found the Solution!!!")
                        print()
                    self.succs += 1
start = brd()
start.main()