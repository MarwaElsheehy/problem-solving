def to_csv_text(array):
  return '\n'.join([','.join(map(str, row)) for row in array])
    
print(to_csv_text([[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]]))
