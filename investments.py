def calc_rentab(fixed_val, index, inv_time, months=None, prev_total=0):
	#print("Fixed_val: %s \n Index: %s \n Inv_time: %s \n Months: %s \n Prev_total: %s \n" % (fixed_val, index, inv_time, months, prev_total) )
	#print("Previous total: %s" % prev_total)
	if months is None:
		months = [i+1 for i in range(inv_time)]
	if (inv_time > 0):
		prev_total=(prev_total + ((index/12)/100)*prev_total) + fixed_val
		print("On the %s month, you have %s moneys." % (ord(months[0]), prev_total))
		months.remove(months[0])
		inv_time-=1
		calc_rentab(fixed_val, index, inv_time, months, prev_total)
	else:
		return("By the end of this investment, you'll have around %s moneys." % prev_total)

def ord(number):
	if number == 1:
		return "%sst" % number
	elif number == 2:
		return "%snd" % number
	elif number == 3:
		return "%srd" % number
	else:
		return "%sth" % number