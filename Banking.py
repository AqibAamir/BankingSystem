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
