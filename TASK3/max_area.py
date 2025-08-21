def maxarea(matrix):
    if not matrix:
        return 0
    
    rows,cols= len(matrix),len(matrix[0])
    heights=[0]*(cols+1)
    max_area= 0

    for row in matrix:
        for i in range(cols):
            if row[i]=="1":
                heights[i]+=1
            else:
                heights[i] = 0
    
        stack=[]
        for i,h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1 
                max_area= max(max_area,height*width)
            stack.append(i)
    return max_area

matrix = [
  ["1","0","1","1","1"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(maxarea(matrix))

