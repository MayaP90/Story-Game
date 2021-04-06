# Introduction
print("Welcome to the survival game!")
print("\n")
print("In this game you are stuck in the snowy mountains.\n Your choices will effect your outome.")
print ("You have not eaten in two days and you see frozen berries across a large frozen lake. \n You notice that the ice is very thin")
print("and could potentially break. The lake is large so you want to cross it quickly. \n But, you also don't want to break the ice and risk hypothermia")
print("\n")
print("You have two options.")
print("You can either careful sprint on the lake or craw on all fours slowly to the end of the lake")
print("pick left for sprinting and right for crawling")

while True:
    do = input(":: ") 
    if do == "left":  
        continue
        print(" As you sprint across the lake the ice cracks and you fall into the lake and freeze to death ")
    elif do == "right":                                            
        print("You picked the right choice! While you may have spent a lot of time, \n you safely traveled to the other side of the lake")
        print("After eating a few berries you encounter a wolf. It is snarling at you and being agressive.")
        answer = input("What do you do? left is to run and right is grab a large tree branch and scare it:")
        if answer == "left":
            print ("you could not outrun the wolf and you are dead ")
            break
        else:
            print("You successfully scared the wolf away","r")
            print("You are physically tired and want to find a way out of here and have two opptions: \n 1) climb the mountin to see if you find a better view or 2) follow the valley")
            if answer == "mountain":
                    print ("Good Job! You have found a road that leads to a town! You are gettin out!")
            elif answer ==  "valley":
                    print ("so close! You follwed the vally but, did not escape") 
    else:
        print("try again")
       