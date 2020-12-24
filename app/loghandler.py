import os
from logging.handlers import RotatingFileHandler

# Кастомное логгирование, обнуляющее файл логов при
# достижении определенного размера
class FileHandler(RotatingFileHandler):
    def __init__(self, filename, mode="a", maxBytes=0, encoding=None, delay=0):
        super(FileHandler, self).__init__(filename, mode, maxBytes, 0, encoding, delay)

    # Если файл достиг максимального размера
    def doRollover(self):
        if self.stream:
            self.stream.close()
        if os.path.exists(self.baseFilename):
            os.remove(self.baseFilename)
        self.mode = "a"
        self.stream = self._open()