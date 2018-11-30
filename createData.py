import time
import random

starttime = 1451631600
endtime = 1483254000
f = open('mainData.csv', 'w')
f.write('key,value,date\n')

while(starttime < endtime):
    if 1466492400 <= starttime < 1468652400:
        row = 'Brexit,' + str(random.uniform(0.2, 1)) + ',' + time.strftime('%m/%d/%y', time.localtime(starttime)) + '\n'
        f.write(row)
    else:
        row = 'Brexit,' + str(0.001) + ',' + time.strftime('%m/%d/%y', time.localtime(starttime)) + '\n'
        f.write(row)

    if 1456038000 <= starttime < 1457679600:
        row = 'Irish General Election,' + str(random.uniform(0.2, 1)) + ',' + time.strftime('%m/%d/%y', time.localtime(starttime)) + '\n'
        f.write(row)
    else:
        row = 'Irish General Election,' + str(0.001) + ',' + time.strftime('%m/%d/%y', time.localtime(starttime)) + '\n'
        f.write(row)

    if 1459062000 <= starttime < 1459926000:
        row = 'Lahore Blast,' + str(random.uniform(0.2, 1)) + ',' + time.strftime('%m/%d/%y', time.localtime(starttime)) + '\n'
        f.write(row)
    else:
        row = 'Lahore Blast,' + str(0.001) + ',' + time.strftime('%m/%d/%y', time.localtime(starttime)) + '\n'
        f.write(row)
    starttime = starttime + 86400
f.close()
