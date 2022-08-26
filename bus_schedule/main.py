def bus_schedule(schedule, time):
    cur_time = time.split(':')
    min_time = (int(cur_time[0]) * 60) + int(cur_time[1])

    schedule_min = []

    for sched in schedule:
        split_sched = sched.split(':')
        schedule_min.append((int(split_sched[0]) * 60) + int(split_sched[1]))

    if schedule[0] == time or min_time < schedule_min[0]:
        return -1

    last_time = 0

    for i in range(0, len(schedule_min)):
        if schedule_min[i] < min_time:
            last_time = schedule_min[i]

    return min_time - last_time


bus = ["10:00", "12:00", "14:30", "15:45"]
time1 = "12:30"
time2 = "00:00"
time3 = "16:00"

print(bus_schedule(bus, time1))
print(bus_schedule(bus, time2))
print(bus_schedule(bus, time3))
