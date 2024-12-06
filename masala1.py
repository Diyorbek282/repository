departure = input().strip()
arrival = input().strip()
time_diff = int(input().strip())

s1, m1 = map(int, departure.split(":"))
s2, m2 = map(int, arrival.split(":"))
delta=abs(s2-s1)*60+m2-m1


hh = delta // 60
mm = delta % 60

print(f"{hh}:{mm}")
