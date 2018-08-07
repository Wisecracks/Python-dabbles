# test drive
def sumof(*args):
    print "Sum of given numbers equals ", sum(list(args))

#sumof(1,2,3,4)

def facto(args):
    if args < 0:
        print "Sorry, factorial doesn't exists for negative numbers."
#    elif args == 0:
#        print "0! is 1"
    else:
        print args,"! is: ", reduce((lambda x,y: x*y),[1]+range(1,args+1))