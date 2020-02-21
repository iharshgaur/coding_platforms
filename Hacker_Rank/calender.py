import sys
import calendar
i=sys.stdin.readline().split(" ")
sys.stdout.write((calendar.day_name[calendar.weekday(int(i[2]), int(i[0]),int(i[1]))]).upper())