import numpy as np
import chinese_calendar
import datetime
import math
import pandas as pd
import pickle

def get_workload(date,xx):
    return len(xx.get_group(date))

def get_cuworkload(date,xx):
    dd = 0
    for key,value in xx:
        if(0<=(key-date).days<27):
            dd += len(xx.get_group(key))
    return math.log(dd+1)

def get_isworkday(date):
    return 1 if(chinese_calendar.is_workday(date)) else 0

def get_numofworkdays(date):
    return math.log((date-datetime.date(2015, 5, 5)).days+1)

def get_timeall(date,xx):
    times = [0.0]*10
    workrecord = xx.get_group(date)
    workrecord = workrecord[workrecord.moduleid==2]
    for h in workrecord.hour:
        times[h-8] += 1
    count = sum(times)
    if(count==0):
        return 1
    else:
        times = [e/count for e in times]
        times = [e**2 for e in times]
        return 1-sum(times)
    
def get_effortall(date,xx):
    workrecord = xx.get_group(date)
    times = {}
    sum_ = 0
    for m in workrecord.moduleid:
        if(times.get(m,"x")=="x"):
            times[m] = 1
        else:
            times[m] += 1
        sum_ += 1
    if(sum_==0):
        return 0
    pro = []
    for key in times.keys():
        pro.append(times[key]/sum_)
    return 1-sum([p**2 for p in pro])
    
def get_numberoftaskcate(date,xx):
    return math.log(len(xx.get_group(date).moduleid.unique())+1)

def get_year(date):
    year = date.year
    years = [0,0,0,0]
    if(2016<=year<=2019):
        years[year-2016] = 1
    
    return years

def get_month(date):
    month = date.month
    months = [0]*11
    if(2<=month<=12):
        months[month-2] = 1
    return months

if __name__ == '__main__':
    res = []
    data = pd.read_csv("data_220426.csv",parse_dates=["operatetime"])
    data.sort_values(by="operatetime",inplace=True)
    data = data.reset_index(drop=True)
    data["date"] = data.operatetime.apply(lambda x: x.date())
    data["year"] = data.operatetime.apply(lambda x: x.date().year)
    data["month"] = data.operatetime.apply(lambda x: x.date().month)
    data["hour"] = data.operatetime.apply(lambda x: x.hour)
    data = data[data.year<2023]
    xx = data.groupby("date")
    for d in data.date.unique():
        r = []
        if((d-datetime.date(2015, 5, 5)).days<28):
            continue
        r.append(get_workload(d,xx))
        r.append(get_cuworkload(d,xx))
        r.append(get_isworkday(d))
        r.append(get_numofworkdays(d))
        r.append(get_timeall(d,xx))
        r.append(get_effortall(d,xx))
        r.append(get_numberoftaskcate(d,xx))
        r.extend(get_year(d))
        r.extend(get_month(d))
        res.append(r)
    newres = np.array(res)
    pickle.dump(newres,open("data.pkl","wb"))