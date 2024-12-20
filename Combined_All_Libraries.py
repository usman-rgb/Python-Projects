#Combined Script for Multiple Libraries

#__Math Library__

def add(a, b):
    """Adding Two Numbers"""
    return a + b


def substraction(a, b):
    """Subtracting Two Numbers"""
    return a - b


def multiply(a, b):
    """Multiplying Two Numbers"""
    return a * b


#__String Library__

def uppercase(string):
    """Converting String to Upper Case"""
    return string.upper()


def lowercase(string):
    """Converting String to Lower Case"""
    return string.lower()


def reverse(string):
    """Reversing String"""
    return string[::-1]


#__Data Science Library__

def mean(numbers):
    """Calculating Mean of List of Numbers"""
    return sum(numbers)/len(numbers)

def variance(numbers):
    """Calculating Variance of List of Numbers"""
    mean_value= mean(numbers)
    return sum((x - mean_value)**2 for x in numbers)/len(numbers)

#__File Handling Library__

def write_file(filename, content):
    """Writing Content to a File"""
    with open(filename, "w") as file:
        file.write(content)

def read_file(filename):
    """Reading Content from a File"""
    with open(filename, "r") as file:
        return file.read()
    

#__Geometry Library__

import math

def area_of_circle(radius):
    """Calculating Area of a Circle """
    return math.pi * radius**2

def perimeter_of_rectangle(length, width):
    """Calculating Perimeter of a Rectangle"""
    return 2 * (length + width)


#__Main Functions to Test All The Libraries__

if __name__ == "__main__":
    print("Math Library ")
    print("Adding Two Numbers:", add(15, 20))
    print("Substracting Two Numbers:", substraction(12, 17))
    print("Multiplying Two Numbers:", multiply(20, 10))


if __name__ == "__main__":
    print("String Library ")
    print("Converting String to Upper Case:", uppercase("Sir Kumail Is Very Talented Boy"))
    print("Concerting String to Lower Case:", lowercase("Alisha is Very Hard Working Girl"))
    print("Reversing String:", reverse("Eman Is Very Talented Girl"))


if __name__ == "__main__":
    print("Data Science Library ")
    numbers = [1, 2, 3, 4, 5]
    print("Mean of List of Numbers:", mean(numbers))
    print("Variance of List of Numbers:", variance(numbers))


if __name__ == "__main__":
    print("File Handling Library ")
    write_file("test.txt", "Hello World")
    print("Reading Content from a File:", read_file("test.txt"))


if __name__ == "__main__":
    print("Geometry Library ")
    print("Area of a Circle:", area_of_circle(5))
    print("Perimeter of a Rectangle:", perimeter_of_rectangle(10, 20))