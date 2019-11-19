




def pares():

    for i in range(0,10,2):
        print (i)


pares()



def diccionario():


    list = ['ramon','pepe','ramon','jose']
    dict = {}

    for i in list:
        key = list.count(i)
        dict[i]=key

    print(dict)


diccionario()



def lista():

    list = ['ramon', 'pepe', 'ramon', 'jose']

    cont= 0

    for i in list:

        print(i,cont )


        cont = cont+1


lista()

def test():
    lst = [4, 3, 3, 5, 6, 7, 8, 5]

    x = set(lst)

    print(x)



test()