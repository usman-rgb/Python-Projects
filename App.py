import Combined_All_Libraries as cal

file=cal.read_file("test.txt")
print(file)

name= cal.uppercase("Sir Kumail Is Very Talented Boy")
print(name)

reverse=cal.reverse("Eman Is Very Talented Girl")
print(reverse)

add=cal.add(15,20)
print(add)

substraction=cal.substraction(12,17)
print(substraction)

multiply=cal.multiply(20,10)
print(multiply)

mean=cal.mean([1,2,3,4,5])
print(mean)

variance=cal.variance([1,2,3,4,5])
print(variance)

area_of_circle=cal.area_of_circle(5)
print(area_of_circle)

perimeter_of_rectangle=cal.perimeter_of_rectangle(10,20)
print(perimeter_of_rectangle)