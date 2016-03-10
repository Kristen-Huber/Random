balance=5000
annualInterestRate=.18


epsilon = 10
step = 10
monPayment = 10
updatedBalance=0
list=[]
counter=0

monthlyInterestRate=annualInterestRate/12
monthlyUnpaidBalance = balance - monPayment
updatedBalance = (1+monthlyInterestRate)*monthlyUnpaidBalance

list.append(updatedBalance)

while monthlyUnpaidBalance < sum(list):
    if abs((monPayment*12)-balance) < epsilon:
        break
    else:
        monPayment += step
        monthlyUnpaidBalance = updatedBalance - monPayment
        updatedBalance = (monthlyInterestRate*monthlyUnpaidBalance)+monthlyUnpaidBalance


        list.append(updatedBalance)
        counter+=1
        
print "Lowest Payment: " + str(monPayment)
