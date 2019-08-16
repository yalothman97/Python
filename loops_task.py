print("\nCASHIER HELPER 9000 🧾")
print("The Coded Electronics Store")

items=[]
while True:
	name=input('\nInsert product name (enter "done" when finished): ')
	if name=='done':
		break
	price=float(input("Insert price: "))
	quantity=int(input("Insert quantity: "))
	items.append({'name':name,'price':price,'quantity':quantity})

print('-'*14+'\n RECEIPT\n'+'-'*14)

total_price=0
for item in items:
	total_price+=item['price']*item['quantity']
	print('%d %s %.3fKD'%(item['quantity'],item['name'],item['price']))

print('-'*14)
print('TOTAL: %.3fKD'%(total_price))