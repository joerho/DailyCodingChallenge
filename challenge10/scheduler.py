from time import sleep


def hello_world():
	print("hello world")

def scheduler(f,n):
	sleep(n/1000)
	f()

scheduler(hello_world, 1000)
hello_world()