from datetime import datetime
import pytz

time='europe'

if time == 'europe':
    hour =datetime.now(pytz.timezone('Europe/London')).hour
elif time == 'india':
    hour = datetime.now(pytz.timezone('Asia/Kolkata')).hour
elif time == 'USA':
    hour = datetime.now(pytz.timezone('USA')).hour
elif time == 'UTC':
    hour = datetime.now(pytz.timezone('UTC')).hour

# Greeting logic
if hour >= 0 and hour < 5:
    greeting = "Good Night!"
if hour > 5 and hour < 12:
    greeting = "Good Morning!"
elif 12 <= hour < 18:
    greeting = "Good Afternoon!"
else:
    greeting = "Good Evening!"

print(greeting)
