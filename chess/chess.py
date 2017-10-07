from PIL import Image,ImageDraw


class ChessGame(object):
    '''
    шахматы
    TODO
    1. НАучиться рисовать шахматы
    2. Найти все фигуры
    3. Продумать логику(научиться рисовать поле и фигуры по ходам)
    '''
    def __init__(self):
        with Image.open('board.jpg') as self.board:
            self.draw = ImageDraw.Draw(self.board)
            self.width = self.board.size[0]
            self.height = self.board.size[1]
            self.pix = self.board.load()


    # под конец self.board.save('ans.jpg','JPEG')
    # del self.draw
