import datetime
dt = datetime.datetime
now = dt.now()


def mCineeded(time):
	mCi = 0.025/(2**(-time/6))
	return mCi


def concentration(mCinow, mCi):

	mLs = (0.05*mCinow)/mCi
	return round(mLs,2)


if now.minute <= 20:
	minutes = 0
elif 21 <= now.minute <= 39:
	minutes = 0.5
else:
	minutes = 1

timerange = 24 - now.hour + 7 + minutes
syringeactivity = int(input('how many mCi you have in syringe: '))

#converting mCi to uCi
thismany = int(mCineeded(timerange)*1000)
		
#QC with saline to reach the needed concentration for 1 drop to = mCi needed
QCto = concentration(int(syringeactivity),mCineeded(timerange))
		
print(f'There are {timerange} hours between now and 7 a.m. tomorrow \n You will need to QC your dose to {QCto} mLs')