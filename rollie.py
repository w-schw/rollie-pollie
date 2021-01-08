def rollie_pollie():
    print("Make sure your units are consistent!")
    proceed ="n"
    while proceed != "y":
        try:
            paper_thickness = float(input("What is the thickness of the material?"))
            original_length = float(input("What is the total length of the material on the full roll?"))
            transfer_length = float(input("How much of the material do you want to transfer to the new roll?"))
            transfer_diameter = float(input("What is the outer diameter of the empty roll?"))

            print("paper thicknes: "+str(paper_thickness))
            print("original length: " + str(original_length))
            print("length to be transfered: "+str(transfer_length))
            print("new roll diameter: "+ str(transfer_diameter))

            if paper_thickness >=min(original_length, transfer_length, transfer_diameter):
                print("HEY- YOUR PAPER THICKNESS IS TOO GREAT")

            elif transfer_diameter >= min(original_length, transfer_length):
                print("YO- YOUR DIAMETER IS TOO BIG")

            elif original_length <= transfer_length:
                print("FYI- YOU ARE TRYING TO MOVE TOO MUCH PAPER")

            else:
                proceed = input("Is this correct? y/n")

        except ValueError:
            print("Numbers only please")

    transfer_radius = transfer_diameter * .5
    #hardcode 100 digits of pi just because
    pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    new_roll_length = 0
    turns = 0

    while new_roll_length < transfer_length:
        turns += 1
        transfer_radius += paper_thickness
        new_roll_length += 2 * pi * transfer_radius
        original_length -= 2 * pi * transfer_radius
    return(print("Turn the transfer roll (360 degrees)" + str(turns)+ ' times, or (180 degrees)'+str(turns/2)+' times.'))



rollie_pollie()
