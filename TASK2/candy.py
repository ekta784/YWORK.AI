def candy(ratings):
    n=len(ratings)
    candies= [1]*n

    #for l-r
    for i in range(1,n):
        if ratings[i]>ratings[i-1]:
            candies[i]=candies[i-1]+1

    #for r-l
    for i in range(n-2,-1,-1):
        if ratings[i]>ratings[i+1]:
            candies[i]=max(candies[i],candies[i+1]+1)

    return sum(candies)

#ratings = [1, 0, 2]
ratings = [1, 1, 2]
print(candy(ratings)) 
