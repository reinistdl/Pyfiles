import sys
val1=sys.argv[1]
val2=sys.argv[2]

def calcuclate_commision(price=val1, amount=val2):
    one_unit_commision=float(price)
    one_unit_commision=one_unit_commision*float(0.0025)
    total_commision_for_transaction=float(one_unit_commision)*float(amount)

    print "One unit commision: %.6f \nTotal commision for transaction: %.6f \nPrice increase required: %.6f" % (one_unit_commision,total_commision_for_transaction, one_unit_commision*2)

if __name__ == '__main__':
    calcuclate_commision()
