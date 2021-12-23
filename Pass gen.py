C = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%^&*'
Q1=input("What do you want to encrypt? ")
Q2=int(input("What year were you born? "))
password = ''

for i in Q1:
    position = C.find(i)
    newposition = (position+2)%36
    password += C[newposition]


if Q2 > 2000:
    Q2=Q2/4
    Q2=str(Q2)
    print((password)+(Q2))     
else:
    print (password)