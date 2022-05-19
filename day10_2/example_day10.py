
# def format_name(f_name, l_name):
#     if f_name == "" or l_name =="" :
#         return "no input"
#     formated_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formatted_l_name}"
# print(format_name(input("What is your first name?\n "), input("What is your last name?\n")  )),




def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def days_in_month(year, month):
    if month > 12 or month < 1 :
        return "invalid input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month == 2:
      return 29
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
