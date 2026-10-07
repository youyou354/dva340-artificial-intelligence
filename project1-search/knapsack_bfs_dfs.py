from collections import deque

queue = deque()

max_w = 420
w = [15,32,60,80,43,120,77,6,93,35,37]
v = [20, 40, 50, 36, 26, 64, 54, 18, 46, 28, 25]
n=len(w)

def knapsackBFS(max_w, curr_w, curr_v, curr_idx, n) :

    queue = deque([(0,0,0, [])]) #initial case, represent the root of the tree
    best_v = 0 #best value found yet
    b_list =[] #best list of objects we took yet

    while queue :
        curr_idx, curr_w, curr_v, list = queue.popleft()
        

        if curr_idx == n:
            if(best_v < curr_v):
                b_list = list
                best_v = curr_v
            continue #jump to the next iteration

        # not considering the item, represent the left node/branch of the tree
        queue.append((curr_idx + 1, curr_w, curr_v, list)) #append puts the element on the right of the queue

        # considering the item, represent the right node/branch of the tree
        if curr_w + w[curr_idx] <= max_w :
            queue.append((curr_idx + 1, curr_w + w[curr_idx], curr_v + v[curr_idx], list + [ (curr_idx, v[curr_idx] ) ] )) #append right so it won't be visited until all the other waiting in line pop

    return (best_v, b_list )

print("BFS ",knapsackBFS(max_w, 0, 0, 0, n))


def knapsackDFS(max_w, curr_w, curr_v, curr_idx, n) :

    queue = deque([(0,0,0,[])]) #initial case,  represent the root of the tree
    best_v = 0 #best value found yet
    b_list = []
    while queue :
        curr_idx, curr_w, curr_v, list = queue.pop()
        

        if curr_idx == n:
            if(best_v < curr_v):
                b_list = list
                best_v = curr_v
            continue #jump to the next iteration 

         # considering the item, represent the right node/branch of the tree, when possible
        if curr_w + w[curr_idx] <= max_w  :
            queue.append( (curr_idx+1, curr_w + w[curr_idx], curr_v + v[curr_idx], list + [(curr_idx, v[curr_idx] ) ] ) )

         # not considering the item, represent the left node/branch of the tree
        queue.append( ( curr_idx+1, curr_w, curr_v, list) ) #will be popped before the append when considering the item, because it will be popped right after this iteration 

        #the queue here is used like a stack 
    return (best_v, b_list)

print("DFS ",knapsackDFS(max_w, 0, 0, 0, n))

#Made by EL OTMANI Youssef
