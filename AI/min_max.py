import math 
  
def minimax (c_depth, node_index, max_turn, scores, t_depth): 
  
    if (c_depth == t_depth):  
        return scores[node_index] 
      
    if (max_turn): 
        return max(minimax(c_depth + 1, node_index * 2, False, scores, t_depth),  
                   minimax(c_depth + 1, node_index * 2 + 1, False, scores, t_depth)) 
      
    else: 
        return min(minimax(c_depth + 1, node_index * 2, True, scores, t_depth),  
                   minimax(c_depth + 1, node_index * 2 + 1, True, scores, t_depth)) 
      
scores = [12, 6, 11, 5, 13, 8, 6, 15] 
  
t_depth = math.log(len(scores), 2) 
  
print("Optimal Value: ", end = "") 
print(minimax(0, 0, True, scores, t_depth)) 
  