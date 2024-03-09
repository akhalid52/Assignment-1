
#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2021
Program: assign1.py akhalid52 (replace student_id with your Seneca User name)
Author: "Abdulmanan Khalid"
The python code in this file (assign1.py) is original work written by
"Abdulmanan Khalid". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: This Python script calculates the end date based on a given start date and number of days,
considering leap years and valid date formats and prints the result.
It uses functions to validate dates, handle leap years, and perform date calculations while also providing error messages for invalid inputs.

Date: 08/03/2024
'''

def usage():
   "This function returns the usage of the script."
    return "Usage: python3 assign1.py DD-MM-YYYY N"

def days_in_mon(year):
    "This function returns a dictionary containing the total number of days in each month for the given year."
   days = {
      1: 31,
      2: 29 if leap_year(year) else 28,
      3: 31,
      4: 30,
      5: 31,
      6: 30,
      7: 31,
      8: 31,
      9: 30,
      10: 31,
      11: 30,
      12: 31,
   }
   return days

def valid_date(date):
    "This function checks if the given date is valid."
    try:
       day, month, year = map(int, date.split('-'))
       if month < 1 or month > 12:
          return False, "Error: wrong month entered"
       if day < 1 or day > 31:
          return False, "Error: wrong day entered"
       if month in [4, 6, 9, 11] and day > 30:
          return False, "Error: wrong day entered"
       if month == 2:
          if (year % 4 == 0 and year % 100 !=0) or year %400 == 0:
             if day > 29:
                return False, "Error: wrong day entered"
          elif day > 28:
             return False, "Error: wrong day entered"
       if year < 1000 or year > 9999:
          return False, "Error: wrong date entered"
       return True
    except ValueError:
       return False, "Error: wrong date entered"

def leap_year(year):
    "takes a year in YYYY format, and returns True if it's a leap year, False otherwise."
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def after(today):
    "after takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the next day in DD-MM-YYYY format."
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        lyear = year % 4 # TODO: put this into the function leap_year.
        if lyear == 0:
            feb_max = 29 # this is a leap year
        else:
            feb_max = 28 # this is not a leap year

        lyear = year % 100
        if lyear == 0:
            feb_max = 28 # this is not a leap year

        lyear = year % 400
        if lyear == 0:
            feb_max = 29 # this is a leap year

        tmp_day = day + 1 # next day

        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before(today):
    "before takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the previous day in DD-MM-YYYY format."
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        lyear = year % 4
        if lyear == 0:
            feb_max = 29 # this is a leap year
        else:
            feb_max = 28 # this is not a leap year

        lyear = year % 100
        if lyear == 0:
            feb_max = 28 # this is not a leap year

        lyear = year % 400
        if lyear == 0:
            feb_max = 29 # this is a leap year

        tmp_day = day - 1 # previous day

        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if tmp_day < 1:
            prev_month = month - 1
            if prev_month < 1:
                prev_month = 12
                year = year - 1
            to_day = mon_max[prev_month]  # if tmp_day < 1, set to the last day of previous month
        else:
            to_day = tmp_day
            prev_month = month

        prev_date = str(to_day).zfill(2)+"-"+str(prev_month).zfill(2)+"-"+str(year)
        return prev_date

def dbda(start_date, num_days):
    end_date = 0
    # create a loop
    # call before() or after() as appropriate
    # return end_date

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    pass
