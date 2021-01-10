def pattern1(n):
	
	for i in range(1,n+1):
		s = ' '.join(['*']*i)
		print(s)		
		
def pattern2(n):
	
	for i in range(1,n+1):
		s = ' '.join(['*']*i)
		w = n*2
		s = s.center(w,' ')
		print(s)
		
def pattern3(n):
	
	for i in range(1,n+1):
		s = ' '.join(['*']*i)
		w = n*2
		s = s.rjust(w,' ')
		print(s)
		
def pattern4(n):
	
	for i in range(1,n+1):
		s = ' '.join(list(map(str,list(range(1,i)))))
		print(s)
		
def pattern5(n):
	
	num = 1
	for i in range(1,n+1):
		lst = list(range(num,num+i))
		num = lst[-1] + 1
		s = ' '.join(list(map(str,lst)))
		print(s)