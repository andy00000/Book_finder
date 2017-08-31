from os import path
import xml.etree.ElementTree as etree

class Book:
    def __init__(self, file):
        if not path.isfile(file):
            return(False)
        else:
            self.file = file
    def author(self):
        tree = etree.parse(self.file)
        root = tree.getroot()
        att = root.findall('.//{http://www.gribuser.ru/xml/fictionbook/2.0}title-info')
        ret = []
        sec = att[0].findall('.//{http://www.gribuser.ru/xml/fictionbook/2.0}author')
        for s in sec:
            if s[0].text == None and s[1].text == None:
                fn = ''
                ln = ''
            elif s[0].text == None:
                ln = s[1].text
            elif s[1].text == None:
                fn = s[0].text
            else:
                fn = s[0].text
                ln = s[1].text
            aname = fn + ' ' + ln
            ret.append(aname)
        return(ret)
    def title(self):
        tree = etree.parse(self.file)
        root = tree.getroot()
        s = root.find('.//{http://www.gribuser.ru/xml/fictionbook/2.0}book-title')
        return(s.text)











if __name__ == '__main__':

    app = QApplication([])
    
    sys.exit(app.exec_())