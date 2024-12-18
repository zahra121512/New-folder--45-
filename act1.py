import calendar

def print_calendar_year(year):
  """Prints the calendar for the specified year."""
  for month in range(1, 13):
    print(calendar.month(year, month))
    print()

# Call the function to print the calendar for 2024
print_calendar_year(2024)