reg=input("registeriin dugaar oruulna uu:")
reg1=reg[:1]
reg2=reg[2:9]
if reg1.isalpha() == True and reg2.isdigit() == True:
    print("registeriin dugaar mon bna")
else:
    print("registeriin dugaar bish bna")