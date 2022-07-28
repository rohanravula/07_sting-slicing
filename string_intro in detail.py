x="department"
# print(x)
# print(x,type(x))

"Index: the index will always starts with postion zero. the index tell the at which position the variable it is"
"eg:"
"0123456789"
"department"
# print(x[0]) #d
# print(x[4]) #r
# print(x[6]) #m
# print(x[8]) #n
# print(x[9]) #t
# print(x[10]) # Index Error : str index out of range
"form the word department we need only the word depart. so we can do like this"
# print(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]) #depart
"form the word department we need only the word apartment. so we can do like this"
print(x[3]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]) #apartment 
"the above pocess is too much leangthy process"
"NOW THIS BELOW PORCESS IS SHORT PORCESS TO DO THE INDEX THAT PROCESS IS CALLED SLICING"
"SLICING WHICH MENAS MAKING THE STRING INTO PEICES"
'now againg lets try with the word department. form the word department we need only the word depart we can do in this way'
print(x[0:6]) #to get depart. the last word "t" is at 5th positon but while slicing we need to take one number extra at last i,e. "6".
"same as for apartment. first we need to take like this"
print(x[3]+x[2:10]) #same as for to get apartment "t" position is at 9 we need to take 10 or we can keep as empty also at last for last string.


