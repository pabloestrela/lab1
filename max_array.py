def max_array(array):
    max = 0
    for e in array:
        if e > max:
            max = e
    return max

if __name__ == "__main__":
    array = [2,3,4,5,6,7,78,321,2,12,1,2]
    print(max_array(array)) 
