from datetime import datetime, timedelta

current = datetime.now()
new_date = current - timedelta(days=5)
print("today:", current.strftime("%Y-%B-%d"))
print("5 days ago:", new_date.strftime("%Y-%B-%d"))