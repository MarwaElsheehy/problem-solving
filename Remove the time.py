def shorten_to_date(long_date):

  return long_date[0:long_date.find(',')]

print(shorten_to_date("Monday February 2, 8pm"))
