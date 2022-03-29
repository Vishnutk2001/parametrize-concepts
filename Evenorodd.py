def Check_Even(x):
    if x%2==0:
        return True
    else:
        return False

if __name__=="__main__":
    x = int(input("enter number"))
    res = Check_Even(x)
    print(res)