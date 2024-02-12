#!/usr/bin/env python3

'''
Title: Solving Fermat's last Theorem
File name: fermats_last_theorem.py
External files: N/A
External files created: N/A
Programmers: Matthew Leuck, D'mond Manns, Noah Reyes
Email Address: matthewjleuck@lewisu.edu, dmondmanns@lewisu.edu, noahreyes@lewisu.edu
Course: CPSC 44000-LT1 - Software Engineering 
Date: 2/11/2024 
Explanation: A program that looks for 'near misses' of the formula x^n + y^n = z^n through interactive input.
             This equation is used in Fermat's last theorem to prove that no natural numbers where n is greater than two
             will result in x^n + y^n = z^n.
Resources:
Basic Description of what Fermat's last theorem is:
https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem

Video on Fermat's last theorem:
https://www.youtube.com/watch?v=qiNcEguuFSA
'''

# will make a function fermat_last_theorem()
def test_function(power_int, range_int):

    '''
    Below is a nested look to create the (x + y) combinations that fit the
    range where x and/or y is greater than or equal to 10. Which is the start point of the
    loop. x and/or y is also less than or equal to k. So that is our end point where k is
    upper limit to x and/or y. We add the plus one to the end point to account for the start
    beginning at 0. 
    '''

    # print("n is: {}\nk is: {}\n\n".format(power_int, range_int))
    
    # smallest = []
    smallest = []

    # x,y combo
    combo_pair = []

    # value x: 10 <= x <= k
    for x in range(10, range_int + 1):
    # value y: 10 <= y <= k
        for y in range(10, range_int + 1):

            # sum_xy is the variable assigned to hold the value: (x^n + y^n)
            sum_xy = (pow(x, power_int) + pow(y, power_int))
            # print("Power Total: {}".format(sum_xy))

            # print the x and y values
            print("Value of x: ", x)
            print("Value of y: ", y)
                                    
            # calculates our z value
            z = (x + y)
        
            # z_n is the value of z raised to our n value
            z_n = pow(z, power_int)

            # print the z value
            print("The value of z is: {}".format(z))
            
            # print the z raised to n value - this was for us to check the value of z^n
            # print("z_n: {}".format(z_n))

            # value (z + 1)
            up_z = (z + 1)

            # [(x^n + y^n) - z^n]
            value_one = (z_n - sum_xy)
            # value_one = (sum_xy - z_n) the values are switch, they become negative

            # [(z+1)^n - (x^n+y^n)]
            value_two = ((pow(up_z, power_int) - sum_xy))

            # all values are printed just for show to follow program will delete later
            # print(" ")
            # print("Value One:", value_one)
            # print("Value Two:", value_two)

            # compare near miss size of both value one and value two
            if (value_one < value_two):
                print("Actual miss:", value_one)
                relative_size_miss_one = (value_one / sum_xy)
                print("Near miss one: {0:.2f}".format(relative_size_miss_one))
                small = relative_size_miss_one
                
            else:
                print("Actual miss:", value_two)
                relative_size_miss_two = (value_two / sum_xy)
                print("Near miss two: {0:.2f}".format(relative_size_miss_two))
                small = relative_size_miss_two

            smallest.append(small)
            print("\n")
      
    '''
    this if statement checks on all the relative_size_miss that were put into an array
    it should go over every value in the array, and check for its lowest size, then prints out the lowest size
    '''
    if smallest is not None:
        for x in smallest:
            if x < small:
                small = x
                x += 1
                return small
            print("The smallest possible miss was: {0:.2f}".format(min(smallest)))

# Main function
def main():
    # ask user for input

    # n represents POWER interger in equation
    n = int(input("What will the value of n be? "))
    # k represents RANGE LIMIT of x & y
    k = int(input("What will the value of k be? (Any interger above 10): "))
    while k < 10:
        k = int(input("The integer you selected was too low!\nWhat will k be? (Any interger above 10): "))
        
    # function should take two parameters n and k
    test_function(n, k)
    
# if name == main
if __name__ == '__main__':
    main()
