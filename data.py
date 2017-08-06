"""HI"""
# picture = 'http://cliparting.com/wp-content/uploads/2016/06/Smiley-thumbs-up-clipart-clipart.jpeg'
#
# audio = open('/home/ihgorek/Documents/PyCharm/photo_sender/data/NO.mp3', 'rb')
#
# hello = 'Hi!'
#
# helper = 'Please entered your email and i checked him'
#
# check = 'end'
def initial(messege):
    with open('data/orf_2.txt') as f:
        for st in f:
            if messege == st[0:len(messege)]:
                return st[0:len(messege)+1]
        else:
            return 'Давай что-нибудь другое'