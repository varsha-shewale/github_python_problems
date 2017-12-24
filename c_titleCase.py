def title_case(title, minor_words = ''):
    title_li = [x.lower() for x in title.split(' ')]
    out = []
    out1 =''
    out.append(title_li[0].capitalize())
    if minor_words != '':
        minor_words = [x.lower() for x in minor_words.split(' ')]
    else:
        minor_words = []

    for ind in range(1, len(title_li)):
        if minor_words!= [] and title_li[ind] in minor_words:
            out.append(title_li[ind])
        else:
            out.append(title_li[ind].capitalize())

    out1 = ' '.join(out)
    return out1

print title_case('First a of in','an often into')
