text= open("pass.txt","w")
for x in range(10):
	for y in range(10):
		for p in range(10):
			for q in range(10):
				count=str(x)+str(y)+str(p)+str(q)
				text.write(count)
				text.write("\n")