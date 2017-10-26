import sys
val1 = sys.argv[1]
val2 = sys.argv[2]

def percentage(newValue=val1, original=val2):
    price1=float(original)
    price2=float(newValue)

    change =((price1-price2)/price2)*100
    print "Change: %.2f %% \nOrigianl: %.6f \nNew: %.6f" % (change, price1, price2)

if __name__ == "__main__":
    percentage()
