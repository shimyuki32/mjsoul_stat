#calculate shanten in json format
from mahjong.tile import TilesConverter

from mahjong.shanten import Shanten

def calc_shanten(tehai):
    tehai.sort()
    man = ''
    pin = ''
    sou = ''
    honors = ''
    for hai in tehai:
        hais = str(hai)
        if hais[0] == '1':
            man += hais[1]
        if hais[0] == '2':
            pin += hais[1]
        if hais[0] == '3':
            sou += hais[1]
        if hais[0] == '4':
            honors += hais[1]
        if hais == '51':
            man += '5'
        if hais == '52':
            pin += '5'
        if hais == '53':
            sou += '5'

    tiles = TilesConverter.string_to_34_array(man=man, pin=pin, sou=sou, honors=honors)
    shanten = Shanten()
    result = shanten.calculate_shanten(tiles)
    return result
    
#sample
if __name__ == '__main__':
    tehai_sample = [16, 17, 17, 22, 23, 52, 26, 28, 32, 33, 34, 53, 37]
    shanten_s = calc_shanten(tehai_sample)
    print(shanten_s)