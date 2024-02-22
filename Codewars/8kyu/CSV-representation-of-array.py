'''
Create a function that returns the CSV representation of a two-dimensional numeric array.

Example:

input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]] 
    
output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'
'''

#first_solution
def to_csv_text(array):
    csv_text = ''
    for arr in array:
        for i in range(len(arr)):
            if i != len(arr)-1:
                csv_text+=str(arr[i])+','
            else:
                csv_text+=str(arr[i])
        
        csv_text+='\n'
    return csv_text[:len(csv_text)-1]