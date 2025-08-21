    height= heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1 
            max_area= max(max_area,height*width)
            stack.append(i)