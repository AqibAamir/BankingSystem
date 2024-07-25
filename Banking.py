import gc
import time

import sys
import fileinput


class BankingSystem:
  
  balance = 0
  
  def __init__(self, username, password, balance,rank):
    self.username = username
    self.balance = balance
    self.password = password
    self.rank = rank


  def checkbalance(self):
    print(self.username+"'s balance: ", self.balance)

  def withdraw(self, amount):
    print("\n") #white spaces

    if self.balance >= amount:
      previousbalance = self.balance
      self.balance = self.balance - amount

      print(amount,"has been withdrawn from account:",self.username)
      print("Previous Balance:",previousbalance,"\nNew Balance:",self.balance)
      print("\n") #white spaces

    else:
      print("Insufficient balance.")

  def deposit(self, amount):
    previousbalance = self.balance
    print("\n") # white spaces
    self.balance = self.balance + amount

print(amount,"has been deposited into account:",self.username)
    print("Previous Balance:",previousbalance,"\nNew Balance:",self.balance)
    print("\n") # white spaces

  def sendmoney(self,receiver,amount):
    print("\n") #white spaces
    if self.balance >= amount:

      previousbalance = self.balance
      self.balance = self.balance - amount
      receiver.balance = receiver.balance + amount

      print(self.username," has sent", amount,"to",receiver.username)
      print(self.username,"Info- \nPrevious Balance:",previousbalance,"\nNew Balance:",self.balance)
      print("\n") #white spaces

    else:
      print("Insufficient balance to send money.")


class ceo(BankingSystem):
  
  def __init__(self, username, password, balance,rank):
    super().__init__(username,password,balance,rank)
  
  def set_balance(self,target,newbalance):
    target.balance = newbalance
    print(target.username,"balance has been set to:",newbalance)
  
  def deduct_balance(self,target,amount):
    target.balance = target.balance - amount
    print(self.username,"has deducted",amount,"from",target.username)
  
  def add_balance(self,target,amount):
    target.balance = target.balance + amount
    print(self.username,"has added",amount,"to",target.username)



#objects


#load data
with open('bankdatabackup.txt') as f:
  for line in f:
    attributes = line.split(':')
    fuser = attributes[0]
    fpass = attributes[1]
    fbalance = int(attributes[2])
    frank = attributes[3].replace("\n", "")
   if frank == "CEO":
     globals()[str(attributes[0])] = ceo(fuser, fpass, fbalance, frank)
   else:
     globals()[str(attributes[0])] = BankingSystem(fuser, fpass, fbalance, frank)
      



def authentication():
  validuser = False
  validpassword = False

  while validuser == False:
    useraccess = input("Which account do you want to sign into: ").lower()

    for object in gc.get_objects():
      if isinstance(object, BankingSystem):
        if str(object.username).lower() == useraccess:
          authenticateduser = object
          validuser = True
  else:
    print("Account found.")
    time.sleep(1)
  print("Username:",useraccess)

  while validpassword == False:
    enterpassword = input("Password: ")

    for object in gc.get_objects():
      if isinstance(object, BankingSystem):
        if object.password == enterpassword:
          print("Authenticated.")
          validpassword = True
  return "Authenticated", authenticateduser




def access(login):
  
  changestouser = []
  with open('bankdatabackup.txt') as f:
    for line in f:
      
      attributes = line.split(':')
      fuser = attributes[0]
      fbalance = int(attributes[2])
      changestouser.append([fuser,fbalance])

action = "Logged in."
  print("Welcome to Aqib's Banking system,",login.username)
  print("You are a:",str(login.rank))
  print("\nYour options:")
  time.sleep(0.5)
  print("Check balance, deposit, withdraw, send money.")
  
  if login.rank == "CEO":
    print("\nAs you have the CEO rank, you have these extra options:")
    print("- Set balance")
    print("- Deduct balance")
    print("- Add to balance")

  time.sleep(0.1)
  print("\n\nIf you wish to exit and logout, type 'logout'.")
  time.sleep(0.1)


  
  while action != "logout":
    action = input("Enter action: ").lower()
    if action == "check balance":
      login.checkbalance()
    elif action == "deposit":
      depositamount = int(input("How much do you want to deposit: "))
      login.deposit(depositamount)
    elif action == "withdraw":
      withdrawamount = int(input("How much do you want to withdraw: "))
      login.withdraw(withdrawamount)
    elif action == "send money":
      correcttarget = False
      while correcttarget == False:
        target = str(input("Who do you want to send money to: ")).lower()
        for object in gc.get_objects():
          if isinstance(object, BankingSystem):
            if str(object.username).lower() == target:
              correcttarget = True
              targetuser = object
      else:
        print("User found.")
      sendamount = int(input("Enter amount to send to user: "))
      login.sendmoney(targetuser,sendamount)




