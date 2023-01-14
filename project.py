import pandas as pd
import numpy as np
import end
import matplotlib.pyplot as plt
plt.style.use("bmh")

df = pd.read_csv("mydata.txt")

Year=np.array(df.iloc[:,1])

Hosts=np.array(df.iloc[:,2])

Total_at=np.array(df.iloc[:,3])

No_Matches=np.array(df.iloc[:,4])

Average_at=np.array(df.iloc[:,5])
#----------------------------------------

print("Welcome\n ------\n|FotMob|\n ------\nToday's Informations is about World Cup\n")
print("""1-A barchart express the relationship between No. of matches in each cup
2-A barchart express the relationship between Total attendance in each cup
3-A barchart express the relationship between AVG attendance in each cup
4-Show all cups and the host of cup in each year
5-Show all info""")

i=str(input("Choose a number, what did you want to know?\n"))

if(i=="1"):
    end.Matches_per_cup(Year, No_Matches)
    
elif(i=="2"):
    end.Tot_at_per_cup(Year,Total_at)
    
elif(i=="3"):
    end.AVG_at_per_cup(Year,Average_at)
    
elif(i=="4"):
  c=1
  for i in range(len(Hosts)):
    print(c,"-",Hosts[i],"-->",Year[i])
    c+=1
    
elif(i=="5"):
    
  plt.subplot(221)
  end.Matches_per_cup(Year, No_Matches)

  plt.subplot(222)
  end.Tot_at_per_cup(Year,Total_at)

  plt.subplots_adjust(wspace=0.4,hspace=0.6)

  plt.subplot(223)
  end.AVG_at_per_cup(Year,Average_at)

  c=1
  for i in range(len(Hosts)):
    print(c,"-",Hosts[i],"-->",Year[i])
    c+=1
    
else:
    print("Wrong Input, Please try again...\n2")