import __init__
import time
import pytz
import datetime as dt
import settings.settings as settings

def is_epoch_time_earlier_than_current_time(epoch_time):
    if type(epoch_time) == str:
        epoch_time = int(epoch_time)
    current_time = get_current_epoch_time()
    if epoch_time < current_time:
        return True
    return False

def get_current_epoch_time():
    """
    Description: Returns the current epoch time.
    """
    return int(time.time())*(1000)

def get_future_epoch_time(days=0, hours=0, minutes=0, seconds=0):
    """
    Description: Returns the future epoch time.
    """
    seconds = seconds
    minutes = minutes*60
    hours = hours*60*60
    days = days*24*60*60
    
    return int(time.time() + days + hours + minutes + seconds)*(1000)

def convert_epoch_to_readable_pst_time_ampm(epoch_time):
    def get_12hr_from_24hr_pst(pst_24hr_time):
        #Format HH:MM:SS
        t = time.strptime(pst_24hr_time, "%H:%M:%S")
        timevalue_12hour = time.strftime("%I:%M:%S %p PST", t )
        return timevalue_12hour
    
    if type(epoch_time) == str:
        epoch_time = int(epoch_time)
    
    epoch_time = dt.datetime.utcfromtimestamp(epoch_time/1000)
    date_and_time = epoch_time.replace(tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S').split(' ')
    time_12hrs_pst = get_12hr_from_24hr_pst(date_and_time[1])
    date_and_time_12hrs_pst_str = date_and_time[0] + " " + time_12hrs_pst
    return date_and_time_12hrs_pst_str


def convert_epoch_to_readable_ct_time_ampm(epoch_time):
    def get_12hr_from_24hr_pst(pst_24hr_time):
        #Format HH:MM:SS
        t = time.strptime(pst_24hr_time, "%H:%M:%S")
        timevalue_12hour = time.strftime("%I:%M:%S %p CT", t )
        return timevalue_12hour
    
    if type(epoch_time) == str:
        epoch_time = int(epoch_time)
    
    epoch_time = dt.datetime.utcfromtimestamp(epoch_time/1000)
    date_and_time = epoch_time.replace(tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('US/Central')).strftime('%Y-%m-%d %H:%M:%S').split(' ')
    time_12hrs_pst = get_12hr_from_24hr_pst(date_and_time[1])
    date_and_time_12hrs_pst_str = date_and_time[0] + " " + time_12hrs_pst
    return date_and_time_12hrs_pst_str

def elapsed_time_in_HM_S_MS(elapsed_time):
    milliseconds = int(round(elapsed_time * 1000))
    minutes, seconds = divmod(elapsed_time, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:.0f} hours {:.0f} minutes {:.0f} seconds {:03d} milliseconds'.format(hours, minutes, seconds, milliseconds % 1000)



if __name__ == "__main__":
    pass
