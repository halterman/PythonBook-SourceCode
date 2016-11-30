print("Help!  My computer doesn't work!")
print("Does the computer make any sounds (fans, etc.)")
choice = input("or show any lights? (y/n):")
#   The troubleshooting control logic
if choice == 'n': # The computer does not have power
    choice = input("Is it plugged in? (y/n):")
    if choice == 'n': # It is not plugged in, plug it in
        print("Plug it in.  If the problem persists, ")
        print("please run this program again.")
    else:  # It is plugged in
        choice = input("Is the switch in the \"on\" position? (y/n):")
        if choice == 'n':  # The switch is off, turn it on!
            print("Turn it on.  If the problem persists, ")
            print("please run this program again.")
        else:  # The switch is on
            choice = input("Does the computer have a fuse?  (y/n):")
            if choice == 'n':  # No fuse
                choice = input("Is the outlet OK? (y/n):")
                if choice == 'n':  # Fix outlet
                    print("Check the outlet's circuit ")
                    print("breaker or fuse.  Move to a")
                    print("new outlet, if necessary. ")
                    print("If the problem persists, ")
                    print("please run this program again.") 
                else:  # Beats me!
                    print("Please consult a service technician.")
            else: # Check fuse
                print("Check the fuse. Replace if ")
                print("necessary.  If the problem ")
                print("persists, then ")
                print("please run this program again.")
else:  # The computer has power
    print("Please consult a service technician.")
