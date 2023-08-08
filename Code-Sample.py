# To check the version of the python

# import sys
# print(sys.version)

# print(type(float(9)))


# a = "Thriller is the sixth studio album"
# print("before upper:", a)
# b = a.upper()
# print("After upper:", b)

# L =['Michael Jackson', 10.2, 1982]

# print('the same element using negative and positive indexing:\n Postive:',L[0],
# '\n Negative:' , L[-3]  )
# print('the same element using negative and positive indexing:\n Postive:',L[1],
# '\n Negative:' , L[-2]  )
# print('the same element using negative and positive indexing:\n Postive:',L[2],
# '\n Negative:' , L[-1]  )

# L.append(['pop', 10])
# print(L)
# a="fahad,asif".split(",")
# print(a)

# A= [1,2,3,4]
# print('Before Change: ', A)
# A[0]= 12
# print('After Change: ', A)
# del(A[0])
# print('Delete Change: ', A)



# album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
#               "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
# album_set = set(album_list)             
# print(album_set)

# squares = ['red', 'yellow', 'green', 'purple', 'blue']

# for i in range(0, 5):
#     print("Before square ", i, 'is',  squares[i])
#     squares[i] = 'white'
#     print("After square ", i, 'is',  squares[i])


# squares=['red', 'yellow', 'green', 'purple', 'blue']

# for i, square in enumerate(squares):
#     print(i, square)


# dates = [1982, 1980, 1973, 2000]

# i = 0
# year = dates[0]

# while(year != 1973):    
#     print(year)
#     i = i + 1
#     year = dates[i]
    

# print("It took ", i ,"repetitions to get out of loop.")

# a = 1

# try:
#     b = int(input("Please enter a number to divide a"))
#     a = a/b
#     print("Success a=",a)
# except ZeroDivisionError:
#     print("The number you provided cant divide 1 because it is 0")
# except ValueError:
#     print("You did not provide a number")
# except:
#     print("Something went wrong")


# a = 1

# try:
#     b = int(input("Please enter a number to divide a"))
#     a = a/b
# except ZeroDivisionError:
#     print("The number you provided cant divide 1 because it is 0")
# except ValueError:
#     print("You did not provide a number")
# except:
#     print("Something went wrong")
# else:
#     print("success a=",a)
# finally:
#     print("Processing Complete")
        
# Import the library

# import matplotlib.pyplot as plt
# %matplotlib inline  

# Create a class Circle

# class Circle(object):
    
#     # Constructor
#     def __init__(self, radius=3, color='blue'):
#         self.radius = radius
#         self.color = color 
    
#     # Method
#     def add_radius(self, r):
#         self.radius = self.radius + r
#         return(self.radius)
    
#     # Method
#     def drawCircle(self):
#         plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
#         plt.axis('scaled')
#         plt.show()  



# class Vehicle:
#     color = "white"

#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.seating_capacity = None

#     def assign_seating_capacity(self, seating_capacity):
#         self.seating_capacity = seating_capacity

#     def display_properties(self):
#         print("Properties of the Vehicle:")
#         print("Color:", self.color)
#         print("Maximum Speed:", self.max_speed)
#         print("Mileage:", self.mileage)
#         print("Seating Capacity:", self.seating_capacity)

# # Creating objects of the Vehicle class
# vehicle1 = Vehicle(200, 50000)
# vehicle1.assign_seating_capacity(5)
# vehicle1.display_properties()

# vehicle2 = Vehicle(180, 75000)
# vehicle2.assign_seating_capacity(4)
# vehicle2.display_properties()



import numpy as np
a= np.array([1,2,3,4])
print(a)