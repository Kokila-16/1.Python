class multiplefunctions():
    def oddeven():
        n=int(input("Enter a number:"))
        if((n%2)==0):
          print(n,"is Even number")
          Number="Even Number"
        else:
          print("It is odd number")
          Number="odd Number"
        return Number
    oddeven()

    def marelig():
        gender=str(input("Your gender:"))
        age=int(input("Your age:"))
        if(age>=20 and gender=="male"):
           print("It is eligible")
           Marraige="It is eligible"
        elif(age>=18 and gender=="female"):
           print("It is eligible")
           Marraige="It is eligible"
        else:
           print("Not eligible")
           Marraige="Not eligible"
        return Marraige
    marelig()
        
    def percentage(num1,num2,num3,num4,num5):
        total=num1+num2+num3+num4+num5
        print("Total:",total)
        print("Percentage",(total/5))
    percentage(98,87,95,95,93)

    def triangle():
       print("The Area of Triangle")
       n1=int(input("Enter the height:"))
       n2=int(input("Enter the breadth:"))
       area=(n1*n2)/2
       print("The Area of Triangle is", area)
       print("The perimeter of Triangle")
       n3=int(input("Enter the height1:"))
       n4=int(input("Enter the height2:"))
       n5=int(input("Enter the breadth:"))
       perimeter=n3+n4+n5
       print("The perimeter of Triangle is", perimeter)
    triangle()

    def subfields():
        list=["machine learning", "neural networks", "vision", "robotics", "speech processing", "natural language processing"]
        for temp in list:
            print(temp)
    subfields()
    
      








        