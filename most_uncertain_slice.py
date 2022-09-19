"""
The most uncertain slices in the 

"""

import numpy as np 
import time 


#make the numpy array 

global array_1 
array_1= np.random.randint(low=0,high=2, size = (4,4) ,dtype=int)

global array_2 
array_2 = np.random.randint(low=0,high=2, size = (4,4) ,dtype=int)



def most_uncertain_values():
	"""
	The function gets the data and gives most uncertain rows and column of the matrix with non
	combined data
	Args:
		None
	Return:
		row, cloumn (int): the colum and row width max uncertain values 
	"""
	shape1, shape2 = array_1.shape

	holes_arry = np.zeros((shape1,shape2))

	count_rows = 0
	count_coloumns = 0
	max_rows = 0
	max_columns = 0
	for i in range(shape1):
		for j in range(shape1):
			#add the condition for the equal checking 
			if array_1[i,j] == array_2[i,j]:
				holes_arry[i,j] = array_1[i,j]
			else:
				holes_arry[i,j] = -1



	return holes_arry


if __name__ == '__main__':
	res  = most_uncertain_values()
	print(res)