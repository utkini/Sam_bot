import re

def parse_message(text):
	res = re.search('\w{1,}@\w{1,}[.]\w{1,4}', text);
	if  res is None:
		return False
	return True
