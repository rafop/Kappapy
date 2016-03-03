from random import randint

s = randint(10, 99)
xd = []
w = s

for n in range(5):
	xd.append(randint(1,4))

	
def wgen(g,h): 
	result = h
	for i in range(len(g)):
		if g[i] == 1:
			result = result + h		
		if g[i] == 2:
			result = result - h
		if g[i] == 3:
			result = result * h		
		if g[i] == 4:
			result = result / h
		
	return result

w = wgen(xd,s)

gucci = False

while (gucci == False):
	if w == 0 or w == s or w == s * s or w == 1 or w == s + s:
		for n in range(5):
			xd.append(randint(1,4))
		w = wgen(xd,s)
	else:
		gucci = True
		
print(s)
print(w)
print("Napisz +, -, * lub /, aby wykonac dzialanie")
op = 0

for kappa in range(20): 
	an = str(raw_input(""))
	if an == '+':
		op = op + s
		print(op)
	if an == '-':
		op = op - s
		print(op)
	if an == '*':
		op = op * s
		print(op)
	if an == '/':
		op = op / s
		print(op)
	if an == 'reset':
		op = 0
	if op == w:
		print('gz')
		break
	