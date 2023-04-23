
import math

def run():
    """ my_dict = {}
    for item in range(0,100):
        my_dict[item] = item**3 """
    
    my_dict = {i: i**3 for i in range(1, 101) if (i%3 != 0)}
    my_dict2 = {i: math.sqrt(i) for i in range(1,1001)}

    print(my_dict2)
    

if __name__ == "__main__":
    run()