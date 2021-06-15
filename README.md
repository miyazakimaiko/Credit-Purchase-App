# Overview

An console app that allows the users of our mobile phone service plan to login, check the credit remaining on their account, purchase additional credit, and/or request a service call. 
All records should be stored for reporting purposes.
Reports will be available to users logged in using specific admin account details.


# Requirements

### Customer wants to..

**Menu 1: Login or Register**
1. Login - For pre-existing customers:

Username = `Email` or `Phone Number` `Password` 

2. Register - For New Customers: 

`Phone Number`

`First Name`

`Last Name`

`Email`

`Password`(Match Password)


Plan Menu - Selection of Plans

    1. Pay As You Go (Can top up by any amount, no expiration)

        Q. Is there a range? 

        A. No, from the business point of view this customer is allowed to top up as much as they want 

    2. Top-Up-20 Plan (Minimum top-up is 20, credit expires in 1 month)

    3. Premium Plan (Minimum top-up is 30, receive 5 euro free credit, expires in 1 month) "Plan ' ' chosen..Thank You" 


**Menu 2 - For Login Users (Customers)**

Display Details - *"Hello 'username' Would You Like to.."*

1. Check Your Current Balance - Include Expiration date

2. Top-Up *"How Much Would You Like To Top-Up?"* Check Requirements of users Current Plan, Add to current balance value with new expiration date 

3. Change Your Current Plan - Plan Menu Appears 

    Q. What happens with reminder of current balance?

A. The balance remains with the client until it expires if it’s the case. (some top ups expire some don’t)

4. Request for a Service Call - *"We Will be in touch Soon"* 

5. Exit - Returns Menu 1 or logs out user, if user's top-up - *"Thank You 'username' See You Again"*

## Admin wants to...

**Menu 1: Login**

Login - For Admin: `Username` = "Username/Employee No." `Password`

**Menu 2 - For Admin**
1. Reports per User specified by Phone Number

- Two Options: (A)Last Month (B)Date Range

After selection

- Reports display all customer's details (`name`, `plan`, `phone number`), `top-ups` with dates, `current balance`

Q. Does it start from a search function or a list of customers?

A. The search is by `phone number`. The system will prompt for this input (*Please, enter the phone number*)

2. Per Plan Report - Menu appears including

1.Pay as You Go

2.Top-Up-20 Plan

3.Premium Plan - Two Options: (A)Last Month (B)Date Range 

- Display all top-ups for that plan  

    Q. Are they a list of users?

    A. No, it’s a list of top ups per plan per date range (last month or data range)

    Q. Anything else to include beside user names (Current balance etc)
    
    A. Its not for user names and current balance, its about top ups made that month or period range. It could include the name of the clients who made the top up but the aim of this report is to check income per plan 

- Display Total of specified plan (*Total: ...*) 

    Q. Is it the total amount of all the users’ balance? 

    A. Total in top ups… for example… in June the company had 2.456.875,00 in top ups of users of Premium Plan.