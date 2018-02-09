#Converting milliseconds to hours, minutes, and seconds

def convert_ms():
    num = int(input("Enter time in ms:"))
    second = int(num / 1000)% 60
    minute = int(num / 60000) % 60
    hour = (num / 3600000) % 24

    print ("%d:%d:%d" % (hour, minute, second))

convert_ms()
