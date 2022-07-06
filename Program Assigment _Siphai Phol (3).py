
while True:
  
  Deposit=float(input("Enter Deposit: "))
  month=int(input("Enter month: "))
  Earned=float(input("Enter interest rate: "))
  print("\n{:<10} {:<15} {:<20} {:<25} {:<25} {:<30}".format("Month", "Deposit", "Total Deposit", "This Month's interest", "Total-Interest Earned", "Total-value to-Date"))
  print("="*119)
  counter = 0 
  for i in range(1,month+1):
        F_start  = (1+Earned/1200)**i
        counter += F_start
        final_F = counter * 100
        Total_Deposit = i*100
        Deposit = 100  
        Interest=final_F-Total_Deposit
        month_int = final_F/101
        print(i,format((Deposit),"15"),format((Total_Deposit),"15"),format((month_int),"20.2f"),format((Interest),"26.2f"),format((final_F),"25.2f"))
  print("="*119)
  check = input("Do you want to quit or start again? \n\nEnter Y to restart or N to end: ")
  if check.upper() == "Y": #go back to the top
    
    continue    
    
  print("\nBye. Have a good day...!")
  break #exit