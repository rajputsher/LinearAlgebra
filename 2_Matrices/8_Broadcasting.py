import numpy as np

# create a matrix
A = np.reshape(np.arange(1,13),(3,4),'F') # F=column, C=row
#A = np.reshape(np.arange(1,13),(3,4),'C') # F=column, C=row

# and two vectors
r = [ 10, 20, 30, 40 ]
c = [ 100, 200, 300 ]

print(A), print(' ')
print(r), print(' ')
print(c), print(' ')

# broadcast on the rows
#print(A+r), print(' ')

# broadcast on the columns
#print(A+c) #this does not work as it worked for column hence we need to do this :
print(A+np.reshape(c,(len(c),1))) # only works for explicit column vectors
