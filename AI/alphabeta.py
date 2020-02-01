MAX, MIN = 1000, -1000 
prune=0

def minimax(depth, nodeIndex, maxPlayer, values, alpha, beta):  
    global prune
    if depth == 3:  
        return values[nodeIndex]  
  
    if maxPlayer:  
        best = MIN 
        for i in range(0, 2):        
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)  
            best = max(best, val)  
            alpha = max(alpha, best)  
  
            if beta <= alpha:  
                prune+=1
                break   

        return best  
       
    else: 
        best = MAX 
        for i in range(0, 2):  
           
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)  
            best = min(best, val)  
            beta = min(beta, best)  
            
            if beta <= alpha:  
                prune+=1
                break 

        return best

if __name__ == "__main__":  

    values = [-1, 3, 5, 1, -6, -4, 0, 9]   
    print(minimax(0, 0, True, values, MIN, MAX)) 
    print("Pruned", prune, "times.") 