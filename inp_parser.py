import codecs

def inp_readln(file):
    book_list = []
    rfdl = codecs.open(file, 'r', 'utf_8_sig')
    for i in rfdl:
        stri = rfdl.readline().split(chr(4))
        book_list.append(stri)
    return book_list

def par_blist(book_list):
    for i in book_list:
        a_name = i[0].split(',')
        #for russian full names
        if len(a_name) == 3:
            author = a_name[0]+' '+a_name[1]+' '+a_name[2][:-1]
        #for other names
        else:
            author = ' '.join(a_name)
            author = author.split(':')
            author = ' '.join(author)
    return author



