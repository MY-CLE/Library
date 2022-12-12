
class Dict(dict):
    def __init__(self, *arg, **kw):
        super(Dict, self).__init__(*arg, **kw)


class BookMap():
    dict = Dict()

    # (Idee) durch datenbank-return value(object array) iterieren und in hashmap/dict als key(titel) value(Book-object) speichern
