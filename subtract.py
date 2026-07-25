a=[[1,2,3],[4,5,6],[7,8,9]]
subtract=0
for row in a:
    for element in row:
        subtract=element-subtract
print(subtract)