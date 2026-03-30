#write a python program to convert a number of seconds into hours, minutes and seconds

time = int(input("Enter time in second: "))

time_hours = time//3600
remaining_time = time%3600
time_minutes = remaining_time//60
remaining_time = remaining_time %60
time_sec = remaining_time

print(f"{time}secs is having {time_hours}hrs,{time_minutes}mins and {time_sec}secs")