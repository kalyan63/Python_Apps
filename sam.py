def addnum(a,b):
    return (a+b)

def sb(a,b):
    return (a-b)

par={"Add":addnum,"Sub":sb}

print(par["Add"](4,5),par["Sub"](10,5))

print("Hello world")