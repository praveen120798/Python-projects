
print('-----------------------------------------------------------------')
print('              Welcome to Tamilnad mercantile bank                ')
print('-----------------------------------------------------------------')
x=input('Enter the username(your name)):')
class password:
    global x
    def pas(self):
        import re
        while True:
            print('Hello ',x)
            print('Note:Password should contain atleast one number,upper case,lower case and symbol(@,#,_)')
            print('Pass should contain 8 characters')
            y=input('Enter the 8 charachter password:')
            if (len(y)!=8):
                print('Password do not have exact 8 characters')
            elif not re.search('[\d]',y):
                print('Password do not have any number')
            elif not re.search('[a-z]',y):
                print('Password do not have any lower case')
            elif not re.search('[A-Z]',y):
                print('Password do not have any upper case')
            elif not re.search('[@#_]',y):
                print('Password do not have any symbol')
            elif re.search('\s',y):
                print('Password has space')
            else:
                print('Processing')
                break
p=password()

p.pas()

print('Please Wait',x)

class bank(password):
    z=int(input('Enter the no of transaction:'))
    cr=[]
    db=[]
    st=[]
    bl=[]
    tn=[]
    def statement(self):
        import time
        global z
        self.balance=10000
        for i in range(1,bank.z+1):
          print('-----------------------------------')
          print('Welcome to Tamilnad mercantile bank')
          print('-----------------------------------')
          print('Transaction no:',i)
          print('Enter the type of transtion:')
          Choice=int(input('(1-credit,2-debit) Enter your choice:'))
          if Choice==1:
              creditamount=float(input('Enter the amount to credit:'))
              bank.cr.append(creditamount)
              bank.db.append(0)
              bank.st.append('cr')
              self.balance+=creditamount
              bank.bl.append(self.balance)
              bank.tn.append(time.ctime())
          elif Choice==2:
              debitamount=float(input('Enter the amount to debit:'))
              if (debitamount>self.balance):
                  print('Insufficient balance')
              else:
                  bank.cr.append(0)
                  bank.db.append(debitamount)
                  bank.st.append('dr')
                  self.balance-=debitamount
                  bank.bl.append(self.balance)
                  bank.tn.append(time.ctime())
          else:
              print('wrong input. Restart the process ')
              
b=bank()

b.statement()

class passbook(bank):
    global x
    def book(statement):
        import random
        print(' ___________________________________________________________________________________________')
        print('|                                                                                           |')
        print('|                             Tamilnad mercantile Bank-Passbook Details                     |')
        print('|___________________________________________________________________________________________|')
        print('Account Holder:',x,'                                  Opening balance:10000')
        print('Account No:69690025',random.randint(100000,999999))
        print('IFSC CODE:JBIB000J028                                           Branch:Beach Road,Thoothukudi')
        print('.............................................................................................')
        print('Type         Credit           Debit            Balance(Rs)                Time           ')
        print('.............................................................................................')
        for i in range(0,bank.z):
            status=bank.st[i]
            credit=bank.cr[i]
            debit=bank.db[i]
            balance=bank.bl[i]
            time=bank.tn[i]
            print(status,' '*9,credit,' '*11,debit,' '*12,balance,' '*12,time)
        print('.............................................................................................')
        print('                                         Thank You                                           ')

d=passbook()

d.book()
    
