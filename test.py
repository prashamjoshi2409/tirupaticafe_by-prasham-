import datetime

name = input("Enter your name: ")
current_time = datetime.datetime.now()

print(f"\nHello {name}!")
print(f"You are running code on a MacBook Pro M5 Pro.")
print(f"Current Date and Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
print("GitHub connection test: Successful!")

