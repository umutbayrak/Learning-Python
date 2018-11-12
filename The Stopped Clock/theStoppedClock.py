# Reading the inputs

hour_left_home = int(input("Enter the hour she left her own house between 0 included and 24 excluded: "))
minute_left_home = int(input("Enter the minute she left her own house between 0 included and 60 excluded: "))

hour_arrival_to_friend = int(input("The hour she arrives at friend's house between 0 included and 24 excluded: "))
minute_arrival_to_friend = int(input("The minute she arrives at friend's house between 0 included and 60 excluded: "))

hour_leaves_friend_house = int(input("The hour she leaves friend's house between 0 included and 24 excluded: "))
minute_leaves_friend_house = int(input("The minute she leaves friend's house between 0 included and 60 excluded: "))

hour_returns_home = int(input("The hour she returns to her own house between 0 included and 24 excluded: "))
minute_returns_home = int(input("The minute she returns to her own house between 0 included and 60 excluded: "))

# Time conversion to minutes
time_left_home_minute = hour_left_home * 60 + minute_left_home
time_arrival_to_friend_minute = hour_arrival_to_friend * 60 + minute_arrival_to_friend
time_leaves_friend_house_minute = hour_leaves_friend_house * 60 + minute_leaves_friend_house
time_returns_home_minute = hour_returns_home * 60 + minute_returns_home

# Calculation steps for time spent at friend's house and for travel
# For the watch at home, time difference might be negative in some cases
# E.g. She left at 3 pm then come back at 2 am actual time difference is 11 hours not -1 hours

time_spent_with_friend = time_leaves_friend_house_minute - time_arrival_to_friend_minute

if time_spent_with_friend <= 0:
    time_spent_with_friend += 24*60
else:
    time_spent_with_friend = time_spent_with_friend

time_spent_outside = time_returns_home_minute - time_left_home_minute

if time_spent_outside <= 0:
    time_spent_outside += 24*60
else:
    time_spent_outside = time_spent_outside

time_spent_for_travel_oneWay = (time_spent_outside - time_spent_with_friend)/2

# To set the real time, travel time and the real time when she left friend's house is summed.

real_time = time_leaves_friend_house_minute + time_spent_for_travel_oneWay

# Converting minutes back to hours and minutes with using quotient and remainder operations

hour = int((real_time // 60) %24)
minutes = int((real_time - hour*60) % 60)

print(hour)
print(minutes)






