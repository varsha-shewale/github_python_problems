import datetime as dt

def calc_date_days(start_date,days):
    end_date = start_date + dt.timedelta(days=days)
    return end_date


def calc_date_weeks(start_date,weeks):
    days = 7*weeks
    end_date = calc_date_days(start_date,days)
    return end_date


def which_date(start_date,time):
    """
    This function takes as input a string depicting a date in YYYY/mm/dd
    format and a string stating a time period in the form of "X day(s)" or
    "Y week(s)". Output should be a string in form YYYY/mm/dd with the date
    that is X days or Y weeks after the initial date.
    """
    start_date = dt.datetime.strptime(start_date, "%Y/%m/%d")
    if time.find('day') != -1: # find method returns starting letter index for the string when found in the main string.
        #else returns -1.
        days = int(time.split(' ')[0])
        end_date = calc_date_days(start_date,days)
    elif time.find('week') != -1:
        weeks =int(time.split(' ')[0])
        end_date = calc_date_weeks(start_date,weeks)
    else:
        print 'Enter start date or time in correct format eg. 7 days or 7 weeks'
    end_date = end_date.strftime('%Y/%m/%d')

    return end_date


print which_date('2016/02/10','35 days')
#print which_date('2010/01/01','4 weeks')

def test():
    """
    Here are a few tests to check if your code is working correctly! This
    function will be run when the Test Run button is selected. Additional
    tests that are not part of this function will also be run when the Submit
    Answer button is selected.
    """
    assert which_date('2016/02/10','35 days') == '2016/03/16'
    assert which_date('2016/12/21','3 weeks') == '2017/01/11'
    assert which_date('2015/01/17','1 week') == '2015/01/24'
    print("All tests completed.")


if __name__ == "__main__":
    test()

