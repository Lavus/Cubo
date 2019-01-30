#!/usr/bin/env python
# -*- coding: utf-8 -*-
def cria_cubo(x,y,z):
	cubo=[]
	for i in range (x):
		cubo.append([])
		for k in range (y):
			cubo[i].append([])
			for n in range (z):
				cubo[i][k].append(random.randint(0,1))
	return (cubo)

def face_1(cubo):
	print "face 1, face do primeiro conjunto de frente"	
	for i in range(len(cubo)):
		for k in range(len(cubo[0])):
			x = 0
			parar = 0
			for z in range(len(cubo[0][0])):
				if (cubo[i][z][k] == 1):
					print "T",x,
					parar = 1
				if parar == 1:
					break
				if x == (len(cubo[0])-1):
					print "A R",
				x = x+1
		print ""			

def face_2(cubo):
	print "face 2, face da primeira linha"	
	for i in range(len(cubo)):
		for k in range(len(cubo[0])):
			x = 0
			parar = 0
			for z in range(len(cubo[0][0])):
				if cubo[z][i][k] == 1:
					print "T",x,
					parar = 1
				if parar == 1:
					break
				if x == (len(cubo[0])-1):
					print "A R",
				x = x+1
		print ""

def face_3(cubo):
	print "face 3, face do ultima conjunto de frente"	
	for i in range(len(cubo)):
		for k in range(len(cubo[0])):
			x = 0
			parar = 0
			for z in range((len(cubo[0][0])-1),-1,-1):
				if cubo[i][z][k] == 1:
					print "T",x,
					parar = 1
				if parar == 1:
					break
				if x == (len(cubo[0])-1):
					print "A R",
				x = x+1
		print ""

def face_4(cubo):
	print "face 4, face da ultima linha"	
	for i in range(len(cubo)):
		for k in range(len(cubo[0])):
			x = 0
			parar = 0
			for z in range((len(cubo[0][0])-1),-1,-1):
				if cubo[z][i][k] == 1:
					print "T",x,
					parar = 1
				if parar == 1:
					break
				if x == (len(cubo[0])-1):
					print "A R",
				x = x+1
		print ""

def face_5(cubo):
	print "face 5, face da primeira coluna"
	for i in range(len(cubo)):
		for k in range(len(cubo[0])):
			x = 0
			parar = 0
			for z in range(len(cubo[0][0])):
				if cubo[i][k][z] == 1:
					print "T",x,
					parar = 1
				if parar == 1:
					break
				if x == (len(cubo[0][0])-1):
					print "A R",
				x = x+1
		print ""

def face_6(cubo):
	print "face 6, face da ultima coluna"	
	for i in range(len(cubo)):
		for k in range(len(cubo[0])):
			x = 0
			parar = 0
			for z in range((len(cubo[0][0])-1),-1,-1):
				if cubo[i][k][z] == 1:
					print "T",x,
					parar = 1
				if parar == 1:
					break
				if x == (len(cubo[0][0])-1):
					print "A R",
				x = x+1
		print ""

def main(args):
	cubo = cria_cubo(3,3,3)
	face_1(cubo)
	face_2(cubo)
	face_3(cubo)
	face_4(cubo)
	face_5(cubo)
	face_6(cubo)
	print "meio: ",cubo[1][1][1]
	print cubo[0]
	print cubo[1]
	print cubo[2]
	return 0

if __name__ == '__main__':
	import sys
	import random
	sys.exit(main(sys.argv))

