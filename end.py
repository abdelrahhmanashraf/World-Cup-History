import matplotlib.pyplot as plt
def Matches_per_cup(Y,N_M):
    
  plt.xlabel("Years")
  plt.ylabel("No. of Matches")
  plt.bar(Y,N_M)
  plt.title("Matches per each Cup.")
  
  
  
def Tot_at_per_cup(Y,Tot_at):
  plt.xlabel("Years")
  plt.ylabel("Total atendance")
  plt.title("Total attendance For each Cup")
  plt.bar(Y,Tot_at)
  
def AVG_at_per_cup(Y,Avg):
  plt.xlabel("Years")
  plt.ylabel("AVG atendance")
  plt.title("Average attendance For each Cup")
  plt.bar(Y,Avg)