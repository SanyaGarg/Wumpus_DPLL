import random
import copy
import dpll
from Agent import *

kb = []
visited = []
safe = []

pit = set()
no_pit = [[1,1]]
wumpus = set()
no_wumpus = set()

safe_wump = []
safe_pit= []

call = 0

'''========================================================DPLL======================================================================================================='''

  
'''======================================================================================================================='''
def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif
#wumpus 1 to 16,pit 17to 32, stench 33 to 48, breeze 49 to 64
def knowledge_base(agent):

    for i in range(1,17):
        for j in range(i+1,17):
            lst = []
            lst.append(-1*i)
            lst.append(-1*j)
            kb.append(lst)

    for i in range(17,33):
        for j in range(i+1,33):
            lst = []
            lst.append(-1*i)
            lst.append(-1*j)
            kb.append(lst) 

    for i in range(33,49):
            lst = []
            lst.append(-1*i)
            k = i-32

            if k!=4 and k!=8 and k!=12 and k!=16:
                lst.append(k+1)
            if k!=13 and k!=14 and k!=15 and k!=16:    
                lst.append(k+4)
            if k!=1 and k!=5 and k!=9 and k!=13:
                lst.append(k-1)
            if k!=1 and k!=2 and k!=3 and k!=4:
                lst.append(k-4)
            kb.append(lst)

    for i in range(33,49):
            lst = []
            lst.append(i)
            k = i-32

            if k!=4 and k!=8 and k!=12 and k!=16:
                lst1 = copy.deepcopy(lst)
                lst1.append(-1*(k+1))
                kb.append(lst1)
            if k!=13 and k!=14 and k!=15 and k!=16: 
                lst2 = copy.deepcopy(lst)   
                lst2.append(-1*(k+4))
                kb.append(lst2)
            if k!=1 and k!=5 and k!=9 and k!=13:
                lst3 = copy.deepcopy(lst)
                lst3.append(-1*(k-1))
                kb.append(lst3)
            if k!=1 and k!=2 and k!=3 and k!=4:
                lst4 = copy.deepcopy(lst)
                lst4.append(-1*(k-4))
                kb.append(lst4)  

    for i in range(49,65):
            lst = []
            lst.append(-1*i)
            k = i-32
            
            if k!=20 and k!=24 and k!=28 and k!=32:
                lst.append(k+1)
            if k!=29 and k!=30 and k!=31 and k!=32:    
                lst.append(k+4)
            if k!=17 and k!=21 and k!=25 and k!=29:
                lst.append(k-1)
            if k!=17 and k!=18 and k!=19 and k!=20:
                lst.append(k-4)
            kb.append(lst)

    for i in range(49,65):
            lst = []
            lst.append(i)
            k = i-32
            
            if k!=20 and k!=24 and k!=28 and k!=32:
                lst1 = copy.deepcopy(lst)
                lst1.append(-1*(k+1))
                kb.append(lst1)
            if k!=29 and k!=30 and k!=31 and k!=32:
                lst2 = copy.deepcopy(lst)    
                lst2.append(-1*(k+4))
                kb.append(lst2)
            if k!=17 and k!=21 and k!=25 and k!=29:
                lst3 = copy.deepcopy(lst) 
                lst3.append(-1*(k-1))
                kb.append(lst3)
            if k!=17 and k!=18 and k!=19 and k!=20:
                lst4 = copy.deepcopy(lst)
                lst4.append(-1*(k-4))
                kb.append(lst4)

    kb.append            
              
    #print(kb)
'''=================================================================================================================================================================='''
#wumpus 1 to 16,pit 17to 32, stench 33 to 48, breeze 49 to 64

def update_kb(agent,i,j,k):
    p = -1*k
    for x in kb:
        # print(x)
        # print(k)
        if k in x:
            kb.remove(x)
        elif p in x:
            x.remove(p)    

def check_safe(agent):
    # print("sfp",safe_pit)
    # print("sfw",safe_wump)
    for x in safe_pit:
        if x in safe_wump and x not in safe:
            safe.append(x)
    
    
def check_pit(agent,k,location):
    global call
    i,j = location[0],location[1]
    if k!=20 and k!=24 and k!=28 and k!=32 and j<4:
        lst1 = copy.deepcopy(kb)
        lst1.append([k+1])
        #print(lst1)
        s = dpll.Solver(lst1,call)
        if not s.solve():
                safe_pit.append([i,j+1])
                call += s.getCalls()
                s.setCalls(call)
                #print(safe_pit)
    if k!=29 and k!=30 and k!=31 and k!=32 and i<4:
        lst2 = copy.deepcopy(kb)
        lst2.append([k+4])
        s = dpll.Solver(lst2,call)
        if not dpll.Solver(lst2,call).solve():
                safe_pit.append([i+1,j])
                call += s.getCalls()
                s.setCalls(call)
                #print(safe_pit)
    if k!=17 and k!=21 and k!=25 and k!=29 and j>1:
        lst3 = copy.deepcopy(kb)
        lst3.append([k-1])
        s = dpll.Solver(lst3,call)
        if not s.solve():
                 safe_pit.append([i,j-1])
                 call += s.getCalls()
                 s.setCalls(call)
    if k!=17 and k!=18 and k!=19 and k!=20 and i>1:
        lst4 = copy.deepcopy(kb)
        lst4.append([k-4])
        if not dpll.Solver(lst4,call).solve():
                safe_pit.append([i-1,j])
                call += dpll.Solver(lst4,call).getCalls()
                s.setCalls(call)
    #print("sp",safe_pit)
 
def update_kb_pit(agent,k,location):
    i,j = location[0],location[1]
    if k!=20 and k!=24 and k!=28 and k!=32 and j<4:
        kb.append([-1*(k+1)])
        safe_pit.append([i,j+1])
    if k!=29 and k!=30 and k!=31 and k!=32 and i<4:
        kb.append([-1*(k+4)])
        safe_pit.append([i+1,j])
    if k!=17 and k!=21 and k!=25 and k!=29 and j>1:
        kb.append([-1*(k-1)])
        safe_pit.append([i,j-1])
    if k!=17 and k!=18 and k!=19 and k!=20 and i>1:
        kb.append([-1*(k-4)])
        safe_pit.append([i-1,j])

def update_kb_wump(agent,k,location):
    i,j = location[0],location[1]
    if k!=4 and k!=8 and k!=12 and k!=16 and j<4:
        kb.append([-1*(k+1)])
        safe_wump.append([i,j+1])
    if k!=13 and k!=14 and k!=15 and k!= 16 and i<4:
        kb.append([-1*(k+4)])
        safe_wump.append([i+1,j])
    if k!=1 and k!=5 and k!=9 and k!=13 and j>1:   
        kb.append([-1*(k-1)])
        safe_wump.append([i,j-1])
    if k!=1 and k!=2 and k!=3 and k!=4 and i>1:
         kb.append([-1*(k-4)])
         safe_wump.append([i-1,j])

def check_wump(agent,k,location):
    global call
    i,j = location[0],location[1]
    if k!=4 and k!=8 and k!=12 and k!=16 and j<4:
        lst1 = copy.deepcopy(kb)
        lst1.append([k+1])
        #print(lst1)
        s = dpll.Solver(lst1,call)
        if not s.solve():
                safe_wump.append([i,j+1])
                call += s.getCalls()
                s.setCalls(call)
    if k!=13 and k!=14 and k!=15 and k!= 16 and i<4:
        lst2 = copy.deepcopy(kb)
        lst2.append([k+4])
        s = dpll.Solver(lst2,call)
        if not s.solve():
                safe_wump.append([i+1,j])
                call += s.getCalls()
                s.setCalls(call)
    if k!=1 and k!=5 and k!=9 and k!=13 and j>1:
        lst3 = copy.deepcopy(kb)
        lst3.append([k-1])
        s = dpll.Solver(lst3,call)

        if not s.solve():
                safe_wump.append([i,j-1])
                call += s.getCalls()
                s.setCalls(call)
    if k!=1 and k!=2 and k!=3 and k!=4 and i>1:
        lst4 = copy.deepcopy(kb)
        lst4.append([k-4])
        s = dpll.Solver(lst4,call)

        if not s.solve():
                safe_wump.append([i-1,j])
                call += s.getCalls()
                s.setCalls(call)
    #print("sw",safe_wump)

def check_status(agent,location,b,s):
    i,j = location[0],location[1]
    neighbours = agent._FindAdjacentRooms()
    k = 4*i+j-4
    lst = []

    safe.append(location)

    if b:
        br = k+48
    else:
        br = -1*(k+48)
    #print(br)
    kb.append([-1*(k+16)])
    update_kb(agent,i,j,br) 
    
    if b:
        check_pit(agent,k+16,[i,j])
    else:
        update_kb_pit(agent,k+16,[i,j])

    if s:
        br = k+32
    else:
        br = -1*(k+32)
    #print(br)
    kb.append([-1*(k)])
    update_kb(agent,i,j,br)

    if s:
        check_wump(agent,k,[i,j])
    else:
        update_kb_wump(agent,k,[i,j])
    
    check_safe(agent)
    #print(safe)

def next_step(agent,location):
    
    neighbours = agent._FindAdjacentRooms()
    #print(neighbours)
    #print(safe)
    safe_nbrs = []
    for x in neighbours:
        if x in safe:
            safe_nbrs.append(x)
    #print(safe_nbrs)
    #print(visited)
    #print(safe)
    
    vis_safenbrs =  []
    for x in safe_nbrs:
        if x in visited:
            vis_safenbrs.append(x)

    nonvis_safenbrs = Diff(safe_nbrs, vis_safenbrs)
    # print(nonvis_safenbrs)
    # print(vis_safenbrs)
    k = len(nonvis_safenbrs)
    if k>0:
        n = random.choice(nonvis_safenbrs)
    else:
        n = random.choice(vis_safenbrs)

    if n!= None:
        i,j = n[0],n[1] 
        x,y = agent.FindCurrentLocation()  

    if(i == x+1):
        return "Right"
    if(i==x-1):
        return "Left"
    if(j == y+1):
        return "Up"
    if(j == y-1):
        return "Down"        

def navigate(agent):
    i = 1
    j = 1
   # print(cur_location)
    t = 0
    while (i<=4 and j<=4) and t<1000:
        t =t+1
        cur_location = agent._curLoc
        i,j = cur_location[0],cur_location[1]
        if i==4 and j==4:
            break
        visited.append([i,j])
        for x in visited:
            visited.remove(x)
            temp = copy.deepcopy(visited)
            if x not in temp:
                visited.append(x)
        b,s = agent.PerceiveCurrentLocation()

        #print(visited)
        check_status(agent,[i,j],b,s)
        #print(safe)
        action = next_step(agent,[i,j])
        #knowledge_base(agent)
        agent.TakeAction(action)
        

def main():
    ag = Agent()
    knowledge_base(ag)
   # print(kb)
    print('curLoc',ag.FindCurrentLocation())
    navigate(ag)
    print(call)
    print("original path",safe)
    path_set = set()
    
    # for x in safe:
    #     path_set.add(tuple(x))
    # print("Safe coordinates",path_set)  

if __name__=='__main__':
    main()