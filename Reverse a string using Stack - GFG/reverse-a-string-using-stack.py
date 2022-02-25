#{ 
#Driver Code Starts

 # } Driver Code Ends
def reverse(S):
    s = ''
    arr = []
    for i in S:
        arr.append(i)
    for i in range(len(arr)):
        s += arr.pop()    
    
    return s

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends