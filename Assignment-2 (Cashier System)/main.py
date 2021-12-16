       
        #DIRECTORY
#Adue = Amount due                      
#titem = total number of items
#itemn = name of an item
#itemp = price of an item


        #CALL FUNCTIONS 1
#Each time function runs, it returns a new amount to be accumulated
def Amount_Due(Adue, i):
        i = float(i)
        i = round(i, 2)
        Adue = Adue + i
        Adue = round(Adue, 2)
        return Adue

# Program runs Function 1 the exact number of times for how many items purchased
def items(t):
    f = 0 
    for x in range(t):
        itemn = input("Please enter the NAME of the item, ")
        itemp = input("Please enter the PRICE of the item, $")
        print (f"{itemn:<15} ${itemp}")
        f = Amount_Due(f, itemp)
        print ("Amount Due =         $", f)
        print()  
    return f    


# Total, plus GST, Discount is calculated 
def calc(t, d):
    g = t * 1.05           #Adds GST
    g = round(g, 2)
    print(  "+GST                 $",g)

    print(  "Discount            ", d,"%")
    d = d/100              #Discount
    d = g * d
    d = round(d, 2)
    print(  "                  = -$",d)

    f = g - d              #Subtracts 
    f = round(f, 2)
    return f





        #BEGINS PROGRAM
# Welcome screen
print()
print("      🥰 WELCOME!🥰")
print()
input("Click ENTER to begin checkout")
print()


print("Thank you for using Self-Cheakout")
# User inputs how many items they will be purchasing
titem= int(input("How many items will you be purchasing today?, "))

print()
#Loop calls Function 1: User inputs name and cost of each item
f = items(titem)


#Apply a random Discount (10, 20, 30 %)
import random                        
d = random.choice (["10", "20", "30"])
d = float(d)

# Calls the function to add GST & Discount
f = calc(f, d)


print("------------------------------------")
print(  "Final Amount Due        $",f)
print()

print("🤗Thank you for shopping at TIC-TAC-TOE")
print()
input("Press ENTER to continue")
print()




# FUNCTION 2: Advertising Graphic included at the end with store logo design and on screen message

# Seperates the square to smaller squares
def squares():
    qwe.forward(300)
    qwe.left(90)
    qwe.forward(100)
    qwe.left(90)
    qwe.forward(300)

# draws the X
def lx():
    qwe.color("blue")
    qwe.right(140)
    qwe.pendown()
    qwe.forward(80)
    qwe.penup()
    qwe.right(130)
    qwe.forward(53)
    qwe.pendown()
    qwe.right(135)
    qwe.forward(80)

    qwe.penup()
    qwe.right(45)

def lo():
    qwe.color("red")
    qwe.pendown()
    qwe.circle(35)
    qwe.penup()

 

#Calls turtle
import turtle


wn = turtle.Screen()  
wn.bgcolor("black")

qwe = turtle.Turtle()  

qwe.color("white")
qwe.pensize(4)
# qwe.speed(0.5)                                  #Contols Speed 

qwe.penup()

qwe.goto(-150,150)
qwe.left(180)

qwe.pendown()
for x in range(4):
    qwe.left(90)
    qwe.forward(300)



qwe.goto(-150,-50)

# Calls Square
qwe.left(180)
squares()


qwe.penup()
qwe.goto(-50,150)

qwe.pendown()
qwe.left(90)
squares()

# Call the X
qwe.pensize(5)

qwe.penup()
qwe.goto(-130,130)
lx()

qwe.goto(-70,-75)
lx()

qwe.goto(125,-130)
lx()


# Calls the O
qwe.goto(0,35)
lo()

qwe.goto(0,-65)
lo()

qwe.goto(-100,35)
lo()


wn.exitonclick()


