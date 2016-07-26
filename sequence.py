"""
This function takes in a list adds from x position and adds numbers to get the needed position
"""

def sequence (list,x,seq):
	[list.append(sum(list[-x:])) for i in range(seq-len(list)) if x<=len(list) ]
	return (list[:seq])

print (sequence([0,1,1],2,100))