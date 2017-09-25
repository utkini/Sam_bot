class ChooseWork(object):

    def __init__(self):
        self.action_dict = {'balda': False,
                            'news': False
                            }

    def balda_on(self):
        # action_dict_flase
        self.all_false()
        self.action_dict['balda'] = True

    def news_on(self):
        self.all_false()
        self.action_dict['news'] = True

    def all_false(self):
        for d in self.action_dict:
            self.action_dict[d] = False

    def get_all(self):
        for d in self.action_dict:
            print(d, self.action_dict[d])


if __name__ == '__main__':
    test = ChooseWork()
    test.balda_on()
    test.get_all()
    print("")
    test.news_on()
    test.get_all()
