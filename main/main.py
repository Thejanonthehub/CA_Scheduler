#main execution file
import fe_tr2
import date_booking

print("Welcome...")
a=int(input('Enter 1 to continue: '))
if a==1:
    print('Sample mysql table after all users filled their online forms ',"\n")
    print(fe_tr2.df0)
    print('\n','After scheduling','\n')
    date_booking.dt_chk()
else:
    print('Sorry, something went wrong try again...')
