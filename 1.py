Number=int(input('Введите число в десятичной системе счисления'))
if Number>0:
    Number_system=input('Введите систему счисления, в которую нужно перевести')
    def translation(k):
        s=''
        if int(Number_system)==2:
            while k>0:
                s=str(k%2)+s
                k=k//2
            return s
        if int(Number_system)==8:
            while k>0:
                s=str(k%8)+s
                k=k//8
            return s
    print(Number,'->',translation(Number))
else:
    print('Error')

