ticket_ids = ["AVT1215M", "TLR0818E", "HPT1012A"]
ticket_cost=0

for code in ticket_ids:
    movie_code=code[0:3]
    seat_no=code[3:5]
    ticket_price=int(code[5:7])
    time=code[-1]
    print("movie_code :",movie_code)
    print("seat_no :",seat_no)
    print("ticket_price : $",ticket_price)
    print("time :",time)
    print("-"*17)
    ticket_cost+=ticket_price
    print("ticket_cost : $",ticket_cost)