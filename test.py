def Countdown(n):
  if n == 0:
    return
    
  print(n)
  Countdown(n-1)
  print('-->', n)

  
Countdown(10)