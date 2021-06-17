# ===============================================================================
# REQUIREMENTS
# 
# Selection 3. General Plan Report - Two Options: (A)Last Month (B)Date Range 
# - Display all top-ups - Display "Total:" 
# ===============================================================================


from datetime import datetime

# only accept start and end date format -- dd/mm/yyyy

def get_all_topups_by_date_range(startDate, endDate):

    # with text file read it and create a list of topups here..
    topups = []

    topup1 = {"phone_number": "123456", "charged": 30, "plan": 1, "date": "18/05/2021"}
    topup2 = {"phone_number": "343848", "charged": 30, "plan": 2, "date": "17/06/2021"}
    topup3 = {"phone_number": "123456", "charged": 30, "plan": 3, "date": "17/07/2020"}
    topup4 = {"phone_number": "123456", "charged": 30, "plan": 1, "date": "17/04/2020"}
    topup5 = {"phone_number": "123456", "charged": 30, "plan": 1, "date": "17/03/2020"}
    topup6 = {"phone_number": "343848", "charged": 30, "plan": 2, "date": "17/02/2020"}
    topup7 = {"phone_number": "123456", "charged": 30, "plan": 3, "date": "17/01/2020"}
    topup8 = {"phone_number": "123456", "charged": 30, "plan": 1, "date": "17/09/2020"}

    topups.append(topup1)
    topups.append(topup2)
    topups.append(topup3)
    topups.append(topup4)
    topups.append(topup5)
    topups.append(topup6)
    topups.append(topup7)
    topups.append(topup8)
    # demo data end

    print("Start Date: ", startDate)
    print("End Date: ", endDate)

    # Header of the topup history table
    print("\n")
    print("Phone Number".ljust(15) + "Charged".ljust(10) + "Plan".ljust(10) + "Date")
    print("---------------------------------------------------------")

    total_charge = 0

    for topup in topups:
        topUpDate = datetime.strptime(topup["date"], "%d/%m/%Y")

        if startDate <= topUpDate and endDate >= topUpDate:
            total_charge += topup["charged"]
            print(f"{topup['phone_number'].ljust(15)}{str(topup['charged']).ljust(10)}{str(topup['plan']).ljust(10)}{topup['date']}")

    print("\nTotal Charge: ", total_charge, "\n")

# Test



def get_topups(planNumber):

        # in actucal setting read txt file and create a list of topups here..
    topups = []

    topup1 = {"phoneNumber": "123456", "topup": 30, "plan": 1, "date": "17/05/2020"}
    topup2 = {"phoneNumber": "343848", "topup": 30, "plan": 2, "date": "17/06/2020"}
    topup3 = {"phoneNumber": "123456", "topup": 30, "plan": 3, "date": "17/07/2020"}
    topup4 = {"phoneNumber": "123456", "topup": 30, "plan": 1, "date": "17/04/2020"}
    topup5 = {"phoneNumber": "123456", "topup": 30, "plan": 1, "date": "17/03/2020"}
    topup6 = {"phoneNumber": "343848", "topup": 30, "plan": 2, "date": "17/02/2020"}
    topup7 = {"phoneNumber": "123456", "topup": 30, "plan": 3, "date": "17/01/2020"}
    topup8 = {"phoneNumber": "123456", "topup": 30, "plan": 1, "date": "17/09/2020"}

    topups.append(topup1)
    topups.append(topup2)
    topups.append(topup3)
    topups.append(topup4)
    topups.append(topup5)
    topups.append(topup6)
    topups.append(topup7)
    topups.append(topup8)



    print("Total: ")