# show share time between users

# return free time in certan calendar
def share_time(calendar, shift_time):
    free_time = []
    # if shift starts before first meeting
    if shift_time[0] < calendar[0][0]:
        free_time.append([])
        free_time[0].append(shift_time[0])
        free_time[0].append(calendar[0][0])
        j = 1
        for i in range(1, len(calendar)):
            if calendar[i - 1][1] != calendar[i][0]:
                free_time.append([])
                free_time[j].append(calendar[i - 1][1])
                free_time[j].append(calendar[i][0])
                j += 1
    # if shift starts at the same time or later first meeting
    else:
        j = 0
        for i in range(0, len(calendar) - 1):
            if calendar[i][1] != calendar[i + 1][0]:
                free_time.append([])
                free_time[j].append(calendar[i][1])
                free_time[j].append(calendar[i + 1][0])
                j += 1
    # if mettings ends earlyer then shift
    if shift_time[1] > calendar[len(calendar) - 1][1]:
        free_time.append([])
        free_time[len(free_time) - 1].append(calendar[len(calendar) - 1][1])
        free_time[len(free_time) - 1].append(shift_time[1])
    return free_time


# show free times that crosses in users calendars
def cross_time(shift_1, shift_2, minutes=0):
    AND_time = []
    j = 0
    for item1 in shift_1:
        for item2 in shift_2:
            if (item2[0] <= item1[1]) and (item1[0] <= item2[1]):
                AND_time.append([])
                AND_time[j].extend(item1)
                AND_time[j].extend(item2)
                AND_time[j].sort()
                AND_time[j] = AND_time[j][1:3]
                j += 1
    return cross_time_more_then(AND_time, minutes)


def cross_time_more_then(array, minutes):
    result = []
    for item in array:
        hour1, minute1 = item[0].split(".")
        hour2, minute2 = item[1].split(".")
        time1 = int(hour1) * 60 + int(minute1)
        time2 = int(hour2) * 60 + int(minute2)
        difference = time2 - time1
        if difference >= minutes:
            result.append(item)
    return result


calendar_1 = [["09.00", '10.30'], ["12.00", '13.00'], ["16.00", '18.00']]
calendar_1_shift = ["08.00", '20.00']

calendar_2 = [["10.00", '11.30'], ["12.30", '14.30'],
              ["14.30", '15.00'], ["16.00", '17.00']]
calendar_2_shift = ["08.00", '18.30']
meeting_duration = 30


avaliable_time_1 = share_time(calendar_1, calendar_1_shift)
avaliable_time_2 = share_time(calendar_2, calendar_2_shift)

# print(avaliable_time_1)
# print(avaliable_time_2)

cross = cross_time(avaliable_time_1, avaliable_time_2, meeting_duration)
print(cross)
