################ here we are checking the Second example ###############################

d={'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}
D={}
for ele in d:
    dt=ele 
    year, month, day = (int(x) for x in dt.split('-'))  # here year,month and day will be stored from the key of the dictionary 
    ans = datetime.date(year, month, day)       
    daynumber=ans.weekday()                #here the number of the weekday will be stored starting from 0 i.e. Monday
    if (daynumber==0):
        D['Mon']=D.get('Mon',0)+d[dt]
    elif (daynumber==1):
        D['Tue']=D.get('Tue',0)+d[dt]
    elif (daynumber==2):
        D['Wed']=D.get('Wed',0)+d[dt]
    elif (daynumber==3):
        D['Thu']=D.get('Thu',0)+d[dt]
    elif (daynumber==4):
        D['Fri']=D.get('Fri',0)+d[dt]
    elif (daynumber==5):
        D['Sat']=D.get('Sat',0)+d[dt]
    else:
        D['Sun']=D.get('Sun',0)+d[dt]
print(D)


################### Here we are checking the third example ########################

d= {'2020-01-01':6,'2020-01-04': 12,'2020-01-05': 14,'2020-01-06':2,'2020-01-07':4}
D={}
for ele in d:
    dt=ele 
    year, month, day = (int(x) for x in dt.split('-'))  # here year,month and day will be stored from the key of the dictionary 
    ans = datetime.date(year, month, day)       
    daynumber=ans.weekday()                #here the number of the weekday will be stored starting from 0 i.e. Monday
    if (daynumber==0):
        D['Mon']=D.get('Mon',0)+d[dt]
    elif (daynumber==1):
        D['Tue']=D.get('Tue',0)+d[dt]
    elif (daynumber==2):
        D['Wed']=D.get('Wed',0)+d[dt]
    elif (daynumber==3):
        D['Thu']=D.get('Thu',0)+d[dt]
    elif (daynumber==4):
        D['Fri']=D.get('Fri',0)+d[dt]
    elif (daynumber==5):
        D['Sat']=D.get('Sat',0)+d[dt]
    else:
        D['Sun']=D.get('Sun',0)+d[dt]
print(D)

#from here we will check that if we missed any day 
day=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
for ele in day:
    if ele not in D:
        curr_index=day.index(ele)
        #if next day is present
        if D.get(day[curr_index+1],'no')!='no':
            D[day[curr_index]]=(D[day[curr_index-1]]+D[day[curr_index+1]])//2
        #if the next day is not present
        else:
            D[day[curr_index]]=2*D[day[curr_index-1]]-D.get(day[curr_index-2],0)
print(D)