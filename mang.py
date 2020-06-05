tickets = {'concert': 500, 'workshop': 700, 'seminar': '300'}
while True:
    buy = int(input('Which ticket to buy:1-concert,2-workshop,3-seminar'))
    q = int(input("How many tickets would you like to buy?"))
    if buy==1:
        print('Here is your concert ticket. Enjoy!')
    elif buy==2:
        print('Here is your workshop ticket.Enjoy!')
    elif buy==3:
        print("Here is your seminar ticket. Enjoy!")
    else:
        print('Invalid Selection')
