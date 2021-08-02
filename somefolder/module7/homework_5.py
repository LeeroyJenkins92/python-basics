winners = 0
for ticket in 345,19,87,1020,421:
    if ticket % 5 == 0 and ticket > 99 and ticket < 1000:
        print(ticket, "happy ticket")
        winners += 1
print("Winners: ",winners)
    