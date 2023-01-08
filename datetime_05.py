import datetime
ob=datetime.datetime.now()

str1=str(ob.day)+'_'+str(ob.month)+'_'+str(ob.year)
str2=str1=str(ob.hour)+'_'+str(ob.minute)+'_'+str(ob.second)
str3='Backup_'+str1+'_'+str2+'.db'
print(str3)
