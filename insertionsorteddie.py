def insertion_sort(list):
  for index in range (1,len(list))
    value = list[index]
    i = index - 1
    while i>=0:
      if value < list[i]:
      list[i+1] = list[i] #shifts number in slot i to slot i+1
      list[i] = value #shifts value into slot i
      i = i - 1
    else:
      break
      
      >>> a = [4,7,3,2,5,7,3]
      >>> insertion_sort(a)
      >>> print a
