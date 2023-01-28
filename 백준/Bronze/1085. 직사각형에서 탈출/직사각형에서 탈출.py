x,y,w,h= map(int,input().split())
if 1 <= w <= 1000 and 1 <= h <= 1000 and 1 <= x <= w-1 and 1 <= y <= h-1 : pass

horDist= x if x<w-x else w-x
verDist= y if y<h-y else h-y
print(min(horDist,verDist))