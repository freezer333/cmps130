import time

LEFT = 1
ABOVE = 2
DIAG = 0

across = open('nras_human.txt').read()#"Saturday";
down = open('nras_cow.txt').read()#"Sunday";
across.replace('\n', "")
down.replace('\n', "")

rows = len(down)+1
cols = len(across) + 1

start = time.time()
D =  [[0 for x in range(cols)] for x in range(rows)] 
E =  [[0 for x in range(cols)] for x in range(rows)] 

for r in range(rows):
	D[r][0] = r
for c in range(cols):
	D[0][c] = c

for r in range(1, rows):
	for c in range(1, cols):
		if across[c-1] == down[r-1]:
			D[r][c] = D[r-1][c-1]
			E[r][c] = DIAG
		else:
			def oracle(above, left, diagonal):
				if above <= left and above <= diagonal:
					return (above+1, ABOVE)
				elif left <= above and left <= diagonal:
					return (left+1, LEFT)
				else:
					return (diagonal+1, DIAG)
			
			D[r][c], E[r][c] = oracle(D[r-1][c], D[r][c-1], D[r-1][c-1])

elapsed = time.time()-start
across_result = ""
down_result = ""
r, c = rows-1, cols-1
while r > 0 and c > 0:
	if E[r][c] == DIAG:
		across_result += across[c-1]
		c-= 1
		down_result += down[r-1]
		r-= 1
	elif E[r][c] == LEFT:
		across_result += across[c-1]
		c-= 1
		down_result += '-'
	else:
		down_result += down[r-1]
		r-= 1
		across_result += '-'
	
while r > 0:
	down_result += down[r-1]
	r-=1
	
while c > 0:
	across_result += across[c-1]
	c-=1;

print("Input Sequences");
print("----------------------------");
print(across);
print(down);
print("----------------------------");

print("Aligned Sequences");
print("----------------------------");
print(across_result[::-1])
print(down_result[::-1])
print("----------------------------");

print("The minimum edit distance is", D[rows-1][cols-1]);
print ("Completed in", str(elapsed), "seconds.")
