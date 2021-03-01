def div30by(dividirpor):
	try:
		return 42/dividirpor
	except ZeroDivisionError:
		print('dividiu por zero')

print(div30by(2))
print(div30by(0))