import re

def parse_message(text):
	res = re.search('\w{1,}@\w{1,}[.]\w{1,4}', text);
	if  res is None:
		return False
	return True

def initial(messege):
	with open('data/orf_2.txt') as f:
		for st in f:
			if messege == st[0:len(messege)]:
				return st[len(messege):len(messege)+1]
		else:
			return 'Давай что-нибудь другое'