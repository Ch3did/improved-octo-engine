import re


def test_um():
    lista=[]
    for i in range(1,101,1):
        if i % 3 == 0 and i % 5 == 0:
            lista.append('FizzBuzz')
        elif i % 3 == 0:
            lista.append('Fizz')
        elif i % 5 == 0:
            lista.append('Buzz')
        else:
            lista.append(i)
    return(lista)




def test_dois(di):
    new_di = {}
    for j in di:
        z = list(j.title())
        y = []
        for i in range(len(z)):
            if z[i]!= "_":
                y.append(z[i])
        y[0]= y[0].lower()
        y = "".join(y)
        new_di[y] = di[j]
    return(new_di)



if __name__ =="__main__": 

    sla  = {
        "nome_user": "lorem ipsum",
        "pass": "lorem ipsum",
        "e_mail_used": "lorem ipsum",
        "some_pame": "lorem ipsum",
        "some_qame": "lorem ipsum"
    }
    # test_um()
    cc = test_dois(sla)

    for i in cc:
        print(i,"\n")