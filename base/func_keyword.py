def person(name, age, **oth):
    print(name,age,oth)


person('asd',10,city='qwe1',job='asd1', bank='123')

others = {'city':'qweqwe2','job':'qwe2'}

person('asd',10,**others)