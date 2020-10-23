def makeEquation(x,y,x2,y2):
	m=(x-x2)/(y-y2)
	b=y/(m*x)
	return [m,b]
def getPoints(r_q,c_q,n):
	points=[]
	if (r_q==1 and c_q==n):
		points.append([n,1])
		points.append([n,n])
		points.append([1,1])

	elif(r_q==n and c_q==1):
		points.append([1,n])
		points.append([1,1])
		points.append([n,n])

	elif(r_q==1 and c_q==1):
		points.append([n,n])
		points.append([n,1])
		points.append([1,n])

	elif(r_q==n and c_q==n):	
		points.append([1,1])
		points.append([1,n])
		points.append([n,1])

	else:
		if c_q!=1 and r_q!=n:
			

		points.append([r_q+1,c_q+1])
		points.append([r_q-1,c_q+1])

	return points


	
def function(n, k, r_q, c_q, obstacles):
	l0=0
	l1=0
	l2=0
	l3=0
	l4=0
	l5=0
	l6=0
	l7=0
	points=getPoints(r_q,c_q,n)
	# eqs=[] 
	# for p in points:
	# 	x2=p[0]
	# 	y2=p[1]
	# 	eqs.append(makeEquation(r_q,c_q,x2,y2))
	# for i in obstacles:
	# 	if i[0]==r_q:
	# 		if i[1]<c_q:
	# 			pass
	# 		else:
	# 			pass
	# 	elif i[1]==c_q:
	# 		if i[0]<r_q:
	# 			pass
	# 		else:
	# 			pass
	tmp_i=r_q
	tmp_y=c_q
	while tmp_i<n:
		tmp_i=tmp_i+1
		poi=[tmp_i,tmp_y]
		if poi in obstacles:
			l0=tmp_i-r_q-1
			# print(l0)
			break
		else:
			l0=tmp_i-r_q
		# print(l0)
	
	tmp_i=r_q
	tmp_y=c_q
	while tmp_i>1:
		tmp_i=tmp_i-1
		poi=[tmp_i,tmp_y]
		if poi in obstacles:
			l1=r_q-tmp_i-1
			# print(l0)
			break
		else:
			# print(tmp_i)
			l1=r_q-tmp_i
		# print(l1)
	
	tmp_i=r_q
	tmp_y=c_q
	while tmp_y<n:
		tmp_y=tmp_y+1
		poi=[tmp_i,tmp_y]
		if poi in obstacles:
			l2=tmp_y-c_q-1
			# print(l0)
			break
		else:
			l2=tmp_y-c_q
		# print(l2)
	tmp_i=r_q
	tmp_y=c_q
	while tmp_y>1:
		tmp_y=tmp_y-1
		poi = [tmp_i,tmp_y]
		if poi in obstacles:
			l3=c_q-tmp_y-1
			# print(l0)
			break
		else:
			l3=c_q-tmp_y
		# print(l3)
	
	tmp_i=r_q
	tmp_y=c_q
	while tmp_i <n and tmp_y<n:
		
		tmp_y=tmp_y+1
		tmp_i=tmp_i+1
		poi = [tmp_i,tmp_y]
		if poi in obstacles:
			l4=tmp_i-r_q-1
			break
		else:
			l4=tmp_i-r_q

	tmp_i=r_q
	tmp_y=c_q
	while tmp_i>1 and tmp_y>1:
		tmp_y=tmp_y-1
		tmp_i=tmp_i-1
		poi =[tmp_i,tmp_y]
		if poi in obstacles:
			l5=c_q - tmp_y - 1
			break
		else:
			l5=c_q-tmp_y
	
	tmp_i=r_q
	tmp_y=c_q
	while tmp_y<n and tmp_i>1:
		tmp_y=tmp_y+1
		tmp_i=tmp_i-1
		poi= [tmp_i,tmp_y]
		if poi in obstacles:
			l6=tmp_y-c_q-1
			break
		else:
			l6=tmp_y-c_q
	
	tmp_i=r_q
	tmp_y=c_q
	while tmp_y>1 and tmp_i<n:
		tmp_i=tmp_i+1
		tmp_y=tmp_y-1
		poi=[tmp_i,tmp_y]
		if poi in obstacles:
			l7 = tmp_i-r_q-1
			break
		else:
			l7=tmp_i-r_q
	return l0+l1+l2+l3+l4+l5+l6+l7

		


if __name__ == "__main__":
	# n=5
	# k=3
	# r_q=4
	# c_q = 3
	# obstacles=[ [5 ,5],[4, 2],[2, 3]]
	n=1
	k=0
	r_q=1
	c_q=1
	obstacles=[]
	print(function(n, k, r_q, c_q, obstacles))
