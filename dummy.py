def copy_list(l):
  if type(l) == list:
      return list(l)
  else:
      raise Exception('Input not a list')

print copy_list(1)