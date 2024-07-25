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

