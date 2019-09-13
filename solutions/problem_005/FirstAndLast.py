def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def cdr(pair):
	def getLast(a,b):
		return b
	return pair(getLast)

def car(pair):
	def getFirst(a,b):
		return a
	return pair(getFirst)


#using lambda
def cdr(pair):
	f = lambda a,b: b
	return pair(f)

def car(pair):
	f = lambda a,b: a
	return pair(f)

assert car(cons(3,4)) == 3
assert cdr(cons(3,4)) == 4