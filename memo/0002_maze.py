#copy by https://www.twblogs.net/a/5be22ff32b717720b51d166b


# 遞歸求解
dirs=[(0,1),(1,0),(0,-1),(-1,0)] #當前位置四個方向的偏移量
path=[]              #存找到的路徑

def mark(maze,pos):  #給迷宮maze的位置pos標"2"表示“倒過了”
    maze[pos[0]][pos[1]]=2

def passable(maze,pos): #檢查迷宮maze的位置pos是否可通行
    return maze[pos[0]][pos[1]]==0

def find_path(maze,pos,end):
    mark(maze,pos)
    if pos==end:
        print(pos,end=" ")  #已到達出口，輸出這個位置。成功結束
        path.append(pos)
        return True
    for i in range(4):  #否則按四個方向順序檢查
        nextp=pos[0]+dirs[i][0],pos[1]+dirs[i][1]
        #考慮下一個可能方向
        if passable(maze, nextp) and find_path(maze, nextp, end):
            print(pos,end=" ")
            path.append(pos)
            return True
    return False

def see_path(maze,path):     #使尋找到的路徑可視化
    for i,p in enumerate(path):
        if i==0:
            maze[p[0]][p[1]] ="E"
        elif i==len(path)-1:
            maze[p[0]][p[1]]="S"
        else:
            maze[p[0]][p[1]] =3
    print("\n")
    for r in maze:
        for c in r:
            if c==3:
                print('\033[0;31m'+"*"+" "+'\033[0m',end="")
            elif c in ["S", "E"]:
                print('\033[0;34m'+c+" " + '\033[0m', end="")
            elif c==2:
                print('\033[0;32m'+"#"+" "+'\033[0m',end="")
            elif c==1:
                print('\033[0;;40m'+" "*2+'\033[0m',end="")
            else:
                print(" "*2,end="")
        print()
        
#-------------------------------------------------------------
#回溯求解
def maze_solver(maze,start,end):
    if start==end:
        print(start)
        return
    st=SStack()
    mark(maze,start)
    st.push((start,0))             #入口和方向0的序對入棧
    while not st.is_empty():      #走不通時回退
        pos,nxt=st.pop()           #取棧頂及其檢查方向
        for i in range(nxt,4):     #依次檢查未檢查方向，算出下一位置
            nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
            if nextp==end:
                print_path(end,pos,st)  #到達出口，打印位置
                return
            if passable(maze,nextp):    #遇到未探索的新位置
                st.push((pos,i+1))      #原位置和下一方向入棧
                mark(maze,nextp)
                st.push((nextp,0))      #新位置入棧
                break                   #退出內層循環，下次迭代將以新棧頂作爲當前位置繼續
    print("找不到路徑")
#隊列求解
def maze_solver_queue(maze,start,end):
   path.append(start)
   if start==end:
       print("找到路徑")
       return
   qu=SQueue()
   mark(maze,start)
   qu.enqueue(start)                #start位置入隊
   while not qu.is_empty():        #還有候選位置
       pos=qu.dequeue()             #取出下一位置
       for i in range(4):           #檢查每個方向
           nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
           if passable(maze,nextp): #找到新的探索方向
               if nextp==end:       #是出口，成功
                   print("找到路徑")
                   path.append(end)
                   return
               mark(maze,nextp)
               qu.enqueue(nextp)    #新位置入隊
               path.append(nextp)

   print("未找到路徑")
if __name__ == '__main__':
    maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
          [1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
          [1,0,1,0,0,0,0,1,0,1,0,1,0,1],\
          [1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
          [1,0,1,0,0,0,0,0,0,1,1,1,0,1],\
          [1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
          [1,0,1,0,0,0,0,0,0,0,0,1,0,1],\
          [1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
          [1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
          [1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
          [1,0,1,0,0,0,1,0,0,1,0,0,0,1],\
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    start=(1,1)
    end=(10,12)
    find_path(maze,start,end)
    see_path(maze,path)
