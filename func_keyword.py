def person(name, age, **oth):
    print(name,age,oth)

others = {'city':'qweqwe','job':'qwe'}

person('asd',10,**others)