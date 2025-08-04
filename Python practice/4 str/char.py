str1 = "a,a,a,b,b,c,c,c"
str2 = str1.split(",")
visited = []
for i in str2:
    if i not in visited:
        visited.append(i)
        print(f"{i}: {str2.count(i)}", end=",")