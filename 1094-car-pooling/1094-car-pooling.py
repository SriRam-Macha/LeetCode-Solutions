class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dicc = dict()
        
        maxi = 0
        
        for i in trips:
            number_passengers = i[0]
            pick_up = i[1]
            drop_off = i[2]
            
            if drop_off > maxi : maxi = drop_off 
            
            P = dicc.get(pick_up,[0,0])
            D = dicc.get(drop_off,[0,0])
            
            P[0] += number_passengers
            D[1] += number_passengers
            
            dicc[pick_up] = P
            dicc[drop_off] = D
        
        current_cap = 0
        
        for i in range(0,maxi+1):
            car_stop = dicc.get(i,[0,0])
            if car_stop != [0,0]:
                current_cap -= car_stop[1]
                current_cap += car_stop[0]
                if current_cap > capacity:
                    return False
                
        return True
            
                
            