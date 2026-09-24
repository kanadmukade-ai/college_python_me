seconds=int(input("enter seconds:"))

hours = seconds//3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print("hours=", hours)
print("minutes=", minutes)
print("seconds=", seconds)
