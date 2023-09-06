def get_hours_minutes_seconds(total_seconds):
    if total_seconds == 0:
        return '0s'
    
    hours = 0
    while total_seconds >= 3600:
        hours += 1
        total_seconds -= 3600
        
    minutes = 0
    while total_seconds >= 60:
        minutes += 1
        total_seconds -= 60
        
    seconds = total_seconds
    
    hms = []
    if hours > 0:
        hms.append(str(hours) + 'h')
    if minutes > 0:
        hms.append(str(minutes) + 'm')
    if seconds > 0:
        hms.append(str(seconds) + 's')
        
    return ' '.join(hms)
    

assert get_hours_minutes_seconds(30) == '30s'
assert get_hours_minutes_seconds(60) == '1m'
assert get_hours_minutes_seconds(90) == '1m 30s'
assert get_hours_minutes_seconds(3600) == '1h'
assert get_hours_minutes_seconds(3601) == '1h 1s'
assert get_hours_minutes_seconds(3661) == '1h 1m 1s'
assert get_hours_minutes_seconds(90042) == '25h 42s'
assert get_hours_minutes_seconds(0) == '0s'