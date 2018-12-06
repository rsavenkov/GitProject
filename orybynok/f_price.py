def fprice(pizza,sise,weight) -> object:
    if pizza == 'Маргарита':
        if sise == 26:
            if weight == 'normal':
                return("220 рублей")
            else:
                return("180 рублей")
        elif sise == 32:
            if weight == 'normal':
                return("230 рублей")
            else:
                return("190 рублей")
        else:
            sise == 40
            if weight == 'normal':
                return("250 рублей")
            else:
                return("210 рублей")
    elif pizza == 'Паперони':
        if sise == 26:
            if weight == 'normal':
                return("220 рублей")
            else:
                return("180 рублей")
        elif sise == 32:
            if weight == 'normal':
                return("230 рублей")
            else:
                return("190 рублей")
        else:
            sise == 40
            if weight == 'normal':
                return("250 рублей")
            else:
                return("220 рублей")
    else:
        pizza == 'Гавайская'
        if sise == 26:
            if weight == 'normal':
                return("230 рублей")
            else:
                return("200 рублей")
        elif sise == 32:
            if weight == 'normal':
                return("250 рублей")
            else:
                return("210 рублей")
        else:
            sise == 40
            if weight == 'normal':
                return("280 рублей")
            else:
                return("230 рублей")
