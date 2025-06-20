#Python 中的 time

#系統的初始時間 epoch

import time

print(time.ctime(0))
print(time.time())  #計算機的時間

local_time=time.localtime()
print(local_time)
print("格式化的時間:",time.strftime("%Y-%m-%d %H:%M:%S"))
#字串轉時間物件
#strftime>時間轉字串
#strptime>字串轉時間
time_string="2025-06-21 12:12:30"  #字串
time_object=time.strptime(time_string,"%Y-%m-%d %H:%M:%S")  #轉換時間
print(time_object)