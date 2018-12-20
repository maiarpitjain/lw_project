#retrive data from database
def auth(user,passwd):
	if passwd=='redhat' and user=="root":
		return True
	else:
		return False
		



