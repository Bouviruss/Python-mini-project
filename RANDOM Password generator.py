import random

lower = "abcdefghijklmopqstxyz"
upper = "ABCDEFGHIJKLMNOPKRUTXYZ"
numbers = "0123456789"
symbols = "@,:/*-"

string = lower + upper + numbers + symbols
length = 20
password ="".join(random.sample(string,length))

print("Your new password is: "+password)
