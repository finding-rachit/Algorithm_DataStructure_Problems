def phone_book(lst,lst2,look):
    
    dic = {}

    for i in range(len(lst)):
        dic[lst[i]] = lst2[i]
    print(dic)

    output = []
    for name in look:
        if (name in dic):
            output.append(name+'='+str(dic[name]))
        else:
            output.append('Not Found')
    print(output)

x=['Sam','Pete','Raj']
y=[123,456,789]
z=['Raj','Mo','Sam']
phone_book(x,y,z)
