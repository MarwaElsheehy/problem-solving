def was_package_received_yesterday(tz_from, tz_to, start, duration):
   
    utc_time = start - tz_from + duration
   
    local_delivery_time = utc_time + tz_to

    return local_delivery_time < 0

print(was_package_received_yesterday(3, 0, 13, 1))
