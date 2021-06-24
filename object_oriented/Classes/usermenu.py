class Usermenu:
   
    def display_usermenu(self):  # Displaying  user menu
        choice="0"
        option=""
        print("")
        print("     Customer Login Menu")
        print("      *****************")
        print("1.  View Balance")
        print("2.  Top-up")
        print("3.  Change plan")
        print("4.  View Statement")
        print("5.  Exit")
        choice=input("Please enter your option[1/2/3/4/5] : ")

        if (choice=="1"):
            print("")
            input("Enter return to continue")
        elif(choice=="2"):
            print("")
            print("Enter return to continue")
        elif(choice=="3"):
            print("")
            print("Enter return to continue")
        elif(choice=="4"):
            print("")
            print("Enter return to continue")
        elif(choice=="5"):
            exit()
        else:
            option=input("Invalid Entry, Do you want to try again? [Y/N] : ")
            option=option.upper()
            if (option=="Y"):
                print("")
                #usermenu.display_usermenu()
            else:
                exit()


######## function for displaying balance###

    #def view_balance(self,user_list):
    #    phone="0862173794"











#usermenu=Usermenu()
#usermenu.display_usermenu()
    
            

                     

