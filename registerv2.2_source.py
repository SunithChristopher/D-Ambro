#Project D'Ambro

class colour:
	BOLD = '\033[1m' 
	END  = '\033[0m' 

print colour.BOLD + '\n\n\n\n				Dunkin\' Donuts \n' + colour.END

print '1. Bagel w/cc \n' '2. Coffee \n' '3. Donut \n' '4. Sandwich \n\n\n'

list1 = [1, 2, 3, 4];


print colour.BOLD + 'Choose from the above list of Products by entering below the number corresponding to the Product.' + colour.END

choice		= int(raw_input('\nEnter your choice 				:  '))


def bagel():
	price_bagel = 3.79
	print '\nName of the product 				:  Bagel w/cc'
	print '\nPrice of the product 				: ', u'$', price_bagel
	qty_bagel = float(input('\nQuantity of the product				:  ')) 
	subtotal 	= price_bagel*qty_bagel
	print '\nSub Total					: ', subtotal
	vat 		= subtotal*0.08
	print u'\nVAT @ 8% of the sub-total			: ', vat
	print '\nThe total amount to be paid is			: ', u'\u0024',subtotal+vat
	return

def coffee():
	price_coffee = 1.59
	print '\nName of the product 				:  Coffee'
	print '\nPrice of the product 				: ', u'$', price_coffee
	qty_coffee = float(input('\nQuantity of the product				:  ')) 
	subtotal 	= price_coffee*qty_coffee
	print '\nSub Total					: ', subtotal
	vat 		= subtotal*0.08
	print u'\nVAT @ 8% of the sub-total			: ', vat
	print '\nThe total amount to be paid is			: ', u'\u0024',subtotal+vat
	return

def donut():
	price_donut = 0.99
	print '\nName of the product 				:  Donut'
	print '\nPrice of the product 				: ', u'$', price_donut
	qty_donut = float(input('\nQuantity of the product				:  ')) 
	subtotal 	= price_donut*qty_donut
	print '\nSub Total					: ', subtotal
	vat 		= subtotal*0.08
	print u'\nVAT @ 8% of the sub-total			: ', vat
	print '\nThe total amount to be paid is			: ', u'\u0024',subtotal+vat
	return

def sandwich():
	price_sandwich = 3.69
	print '\nName of the product 				:  Sandwich'
	print '\nPrice of the product 				: ', u'$', price_sandwich
	qty_sandwich = float(input('\nQuantity of the product				:  ')) 
	subtotal 	= price_sandwich*qty_sandwich
	print '\nSub Total					: ', subtotal
	vat 		= subtotal*0.08
	print u'\nVAT @ 8% of the sub-total			: ', vat
	print '\nThe total amount to be paid is			: ', u'\u0024',subtotal+vat
	return

if choice==list1[0]:
	bagel()
elif choice==list1[1]:
	coffee()
elif choice==list1[2]:
	donut()
elif choice==list1[3]:
	sandwich()
else:
	print '\n Invalid Input, run the program again. You are blessed by Christ! \n'
	exit()


print colour.BOLD + u'\n\n\n	 This project is dedicated to Sarah D\'Ambro. ChrisSunith \u00a9 2016\n\n\n\n\n\n\n\n\n\n'.encode('utf-8') + colour.END



