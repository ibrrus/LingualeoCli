

def show_translate_variant(translates):
    for t in range(1, len(translates)):
        element = translates[t-1]
        print('[' + str(t) + '] ' + element["value"])

