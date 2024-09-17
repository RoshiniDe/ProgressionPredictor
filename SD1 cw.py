##I declare that my work contains no examples of misconduct, such as plagirism, or collusion.
##Any code taken from other sources is referenced within my code solution.

##Student ID: 20232206 / w2054000
##Date: 13/12/2023

from graphics import*

#Initialize counts for the histogram
progress_count = 0
trailing_count = 0
retriever_count = 0
exclude_count = 0

records = []   #records list to store user inputs and outcomes

#function to predict progression outcome
def predict_progression(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits

    if total_credits != 120:
        return "Total incorrect"
    else:
        if pass_credits == 120:
            return "Progress"
        elif pass_credits == 100 and defer_credits == 20:
            return "Progress (module trailer)"
        elif pass_credits == 100 and fail_credits == 20:
            return "Progress (module trailer)"
        elif pass_credits == 40 and fail_credits == 80:
            return "Exclude"
        elif pass_credits == 20 and defer_credits == 20 and fail_credits == 80:
            return "Exclude"
        elif pass_credits == 20 and fail_credits == 100:
            return "Exclude"
        elif defer_credits == 40 and fail_credits == 80:
            return "Exclude"
        elif defer_credits == 20 and fail_credits == 100:
            return "Exclude"
        elif fail_credits == 120:
            return "Exclude"
        else:
            return "Module retriever"
        
#function to create and display the histogram        
def main():
    win=GraphWin("Histogram",600,600)
    win.setBackground("white")
    text=Text(Point(110,20),"Histogram Results")
    text.draw(win)
    line=Line(Point(10,500),Point(520,500))
    line.draw(win)
    
    aRectangle = Rectangle(Point(50,500), Point(150,500 -(progress_count*20)))
    aRectangle.setFill("light green")
    aRectangle.draw(win)

    bRectangle = Rectangle(Point(160,500), Point(260,500 -(trailing_count*20)))
    bRectangle.setFill("light blue")
    bRectangle.draw(win)

    cRectangle = Rectangle(Point(270,500), Point(370,500 -(retriever_count*20)))
    cRectangle.setFill("yellow")
    cRectangle.draw(win)

    dRectangle = Rectangle(Point(380,500), Point(480,500 -(exclude_count*20)))
    dRectangle.setFill("light pink")
    dRectangle.draw(win)

    text1=Text(Point(100,510),"Progress")
    text1.draw(win)
    
    text2=Text(Point(210,510),"Trailer")
    text2.draw(win)
    
    text3=Text(Point(320,510),"Retriever")
    text3.draw(win)
    
    text4=Text(Point(430,510),"Excluded")
    text4.draw(win)

    #number of students in each progression category
    count1=Text(Point(100,460 -(progress_count*20)),f"{progress_count}")
    count1.draw(win)
    
    count2=Text(Point(210,460 -(trailing_count*20)),f"{trailing_count}")
    count2.draw(win)

    count3=Text(Point(320,460 -(retriever_count*20)),f"{retriever_count}")
    count3.draw(win)

    count4=Text(Point(430,460 -(exclude_count*20)),f"{exclude_count}")
    count4.draw(win)
    
    #total number of students
    total=Text(Point(100,550),f"{progress_count + trailing_count + retriever_count + exclude_count}" " " "outcomes in total")
    total.draw(win)

    win.getMouse()
    win.close()

#Get inputs from the user
while True:
    try:
        pass_credits = int(input("Please enter your credits at pass: "))
        if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:  
            print ("Out of range")                        
            continue                                      
        defer_credits = int(input("Please enter your credits at defer: "))
        if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print ("Out of range")
            continue
        fail_credits = int(input("Please enter your credits at fail: "))
        if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print ("Out of range")
            continue
        break

    except:
         print ("Integer required")

outcome = predict_progression(pass_credits,defer_credits,fail_credits)
print("Progression Outcome:", outcome)

#appending to the list
records.append((outcome,": ",pass_credits,defer_credits,fail_credits))

#Update counts for the histogram
if outcome == "Progress" :
    progress_count += 1
elif outcome == "Progress (module trailer)":
    trailing_count += 1
elif outcome == "Module retriever":
    retriever_count += 1
elif outcome == "Exclude":
    exclude_count += 1

#Loop to predict progression outcomes for multiple students
while True:
    pass_input = input("Would you like to try another set of data?\nEnter 'y' for yes and 'q' to quit:")
    
    if pass_input.lower() == 'q':
        
        #printing the list
        print("")
        print("part #2")
        print("List")
        for i in range(0,len(records)):
            print(*records[i])

        #file handling 
        try:
            f = open("myfile.txt", "x")
        except:
            pass

        with open('myfile.txt', 'w') as n: # opening the text file to write
            for i in range (0,len(records)):
                print (*records[i],file=n) # writing previous records in the text file  
        print("")
        n.close()

        print ("part #3")
        print ("Text file")

        with open('myfile.txt', 'r') as fo: # opening the text file to read
            print (fo.read()) # reading the text file 
        print("")
        fo.close()

        main()  #call to the main function
        break
        
    elif pass_input.lower() != 'y':
        print("Invalid input.Please enter 'y' to continue or 'q' to quit:")
        continue
        
    try:
        pass_credits = int(input("Enter your total pass credits:"))
        if pass_credits not in [0,20,40,60,80,100,120]:
            print ("Out of range")
            continue
        defer_credits = int(input("Enter your total defer credits: "))
        if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print ("Out of range")
            continue
        fail_credits = int(input("Enter your total fail credits: "))
        if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print ("Out of range")
            continue
    except ValueError:
        print("Integer required")
        continue

    outcome = predict_progression(pass_credits, defer_credits, fail_credits)
    print("Progression Outcome:", outcome)
    records.append((outcome,": ",pass_credits,defer_credits,fail_credits))

    #Update counts for the histogram
    if outcome == "Progress" :
        progress_count += 1    
    elif outcome == "Progress (module trailer)":
        trailing_count += 1
    elif outcome == "Module retriever":
        retriever_count += 1
    elif outcome == "Exclude":
        exclude_count += 1
