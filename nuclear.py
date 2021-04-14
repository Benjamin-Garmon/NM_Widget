import datetime
dt = datetime.datetime
now = dt.now()

# decay equation for Tc99m, need 25 uCi(.025mCi)
def mCineeded(time):
	mCi = 0.025/(2**(-time/6))
	return mCi

# cross multiplication to find needed concentration (mCi/mL) now for 1 drop(.05mL) @ 7 to equal our needed 25 uCi.
def concentration(mCinow, mCi):

	mLs = (0.05*mCinow)/mCi
	return round(mLs,2)


#24 hr per day - how many hours have passed so far = hr till midnight. then add 7 to get to 7 a.m. minus the minutes in the hour so far, rounded to 2 decimal places
timerange = round(24 - now.hour + 7 - (now.minute/60),2)
syringeactivity = float(input('how many mCi you have in syringe: '))
		
#QC with saline to reach the needed concentration for 1 drop to = mCi needed
QCto = concentration(float(syringeactivity),mCineeded(timerange))

print(f'There are {timerange} hours between now and 7 a.m. tomorrow \n You will need to QC your dose to {QCto} mLs')
