from datetime import timedelta, datetime

now = datetime.now()
past = now - timedelta(days=1)
diff = (now - past).total_seconds()
print("Now:", now)
print("Past:", past)
print("Difference:", diff)