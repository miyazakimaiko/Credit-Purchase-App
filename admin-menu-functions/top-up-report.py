from datetime import datetime

# only accept start and end date format -- dd/mm/yyyy

def get_all_topups_by_date_range(start, end):

    # with text file read it and create a list of topups here..
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

    startDate = datetime.strptime(start, "%d/%m/%Y")
    endDate = datetime.strptime(end, "%d/%m/%Y")
    totalTopUp = 0

    for topup in topups:
        topUpDate = datetime.strptime(topup["date"], "%d/%m/%Y")
        if startDate <= topUpDate and endDate >= topUpDate:
            totalTopUp += topup["topup"]
            print(topup)

    print("Total Top Up: ", totalTopUp)

# Test
get_all_topups_by_date_range("17/05/2020", "17/07/2020")



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