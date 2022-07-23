def time_conversion(hours, minutes, seconds):
    return (hours*3600+ minutes*60 + seconds)
def inputtingTime():
    hours = input("Hours : ")
    minutes = input("Minutes : ")
    seconds = input("Seconds : ")
    return int(hours), int(minutes), int(seconds)

H, M, S = inputtingTime()
print("For {} hours, {} Minutes and {} seconds, the total is : {}".format(H, M, S,time_conversion(H, M, S)))

trente = input("Number : ")
print(eval(trente))