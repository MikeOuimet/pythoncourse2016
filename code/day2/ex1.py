import calendar

def ndays(month, year):
	'''Calculates number of days in given month including leapyear, requires month 
	written as either full name -ex January or abbr Jan (capitalized) and year
	'''
	for m in range(1,13):
		if month == calendar.month_name[m] or month == calendar.month_abbr[m]:
			m_id = m
			break

	if m_id ==2:
		numleapdays = calendar.leapdays(int(year), int(year)+1)
	else:
		numleapdays = 0
	return calendar.mdays[m_id] + numleapdays


if __name__ == '__main__':
	print ndays('February', 2012)

	month = raw_input('Which month? either ex: January or Jan:     ')
	year = raw_input('What year?:     ')
	print ndays(month, year)