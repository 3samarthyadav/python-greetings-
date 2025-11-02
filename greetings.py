from datetime import datetime
import pytz

# Get current time in India
india_time = datetime.now(pytz.timezone('Asia/Kolkata'))
hour = india_time.hour

# Greeting logic
if hour < 12:
    greeting = "Good Morning!"
elif 12 <= hour < 18:
    greeting = "Good Afternoon!"
else:
    greeting = "Good Evening!"

print(greeting)
