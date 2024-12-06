departure = input().strip()
arrival = input().strip()
time_diff = int(input().strip())

s1, m1 = map(int, departure.split(":"))
s2, m2 = map(int, arrival.split(":"))

start_minutes = s1 * 60 + m1
end_minutes = s2 * 60 + m2

end_minutes += time_diff * 60

if end_minutes < start_minutes:
    end_minutes += 1440

delta = end_minutes - start_minutes

hh = delta // 60
mm = delta % 60
hh+=time_diff
print(f"{hh:02}:{mm:02}")
