def get_birthstone(date):
    print('model date', date)
    year, month, day = date.split('-')
    
    month = int(month)
    day = int(day) 

    if month == 12:
        stone = 'topaz' if (day < 22) else 'ruby'
    elif month == 1:
        stone = 'ruby' if (day < 20) else 'garnet'
    elif month == 2:
        stone = 'garnet' if (day < 19) else 'amethyst'
    elif month == 3:
        stone = 'amethyst' if (day < 21) else 'bloodstone'
    elif month == 4:
        stone = 'bloodstone' if (day < 20) else 'sapphire'
    elif month == 5:
        stone = 'sapphire' if (day < 21) else 'agate'
    elif month == 6:
        stone = 'agate' if (day < 21) else 'emerald'
    elif month == 7:
        stone = 'emerald' if (day < 23) else 'onyx'
    elif month == 8:
        stone = 'onyx' if (day < 23) else 'carnelian'
    elif month == 9:
        stone = 'carnelian' if (day < 23) else 'chrysolite'
    elif month == 10:
        stone = 'chrysolite' if (day < 23) else 'beryl'
    elif month == 11:
        stone = 'beryl' if (day < 22) else 'topaz'
  
    return stone
