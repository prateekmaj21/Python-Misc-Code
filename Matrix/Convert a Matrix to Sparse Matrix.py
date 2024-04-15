#Convert a Matrix to Sparse Matrix

import numpy as np

#CHANGE COMMENT TO TEST GITHUB

#function to convert normal matrix to sparse
def convertSparse(matrix):
    
    #first element of sparse matrix showing the order of matrix and the number of non zero elements
    sparse=[]
    first_element=[]
    first_element.append(len(matrix))
    first_element.append(len(matrix[0]))
    first_element.append(np.count_nonzero(matrix))
    
    sparse.append(first_element)
    
    #checking the non zero elements
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0 :
                temp=[]
                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])
                
                sparse.append(temp)
                
    return sparse
                
normalMatrix =[[15, 0, 0, 0],  
               [0, 7, 21, 0],  
               [0, 0, 31, 0],  
               [0, 0, 0, 41],  
               [52, 0, 0, 0]] 

a= convertSparse(normalMatrix)

#display the sparse matrix
def displayMatrix(matrix): 
      
    for row in matrix: 
        for element in row: 
            print(element, end =" ") 
        print() 

displayMatrix(a)
