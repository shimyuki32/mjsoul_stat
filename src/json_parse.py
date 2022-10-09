#convert json_data to time series format
from copy import deepcopy

def log_parse(log):
    log_parse_list = []
    loop_count = -1
    while True:
        loop_count += 1
        if 'who' in locals():
            pass
        else:
            who = log[0][0]
            next_tsumo = [log[i * 3 + 5][0] for i in range(4)]
            loop = [0, 0, 0, 0]
            tehai_all = [[log[i * 3 + 4], []] for i in range(4)]
        try:
            tsumo = log[who * 3 + 5].pop(0)
        except:
            break
        
        if type(tsumo) == str:
            if len(tsumo) == 7 and 'p' in tsumo:
                tehai_all[who][1].append(tsumo)
                for i in range(2):
                    tehai_all[who][0].remove(int(tsumo[-2:]))
            elif len(tsumo) == 7 and 'c' in tsumo:
                tehai_all[who][1].append(tsumo)
                tehai_all[who][0].remove(int(tsumo[-4:-2]))
                tehai_all[who][0].remove(int(tsumo[-2:]))
                
            elif len(tsumo) == 9:
                tehai_all[who][1].append(tsumo)
                for i in range(3):
                    tehai_all[who][0].remove(int(tsumo[-2:]))
        try:
            dahai = log[who * 3 + 6].pop(0)
        except:
            dahai = 0
            log_parse_list.append(deepcopy([who, tehai_all[who], tsumo, dahai]))
            break
        
        log_parse_list.append(deepcopy([who, tehai_all[who], tsumo, dahai]))
        try:
            next_tsumo[who] = log[who * 3 + 5][0]
        except:
            next_tsumo[who] = 0
            
        if type(dahai) == str and len(dahai) == 9:
            if 'a' in dahai:
                tehai_all[who][1].append(dahai)
                tehai_all[who][0].append(tsumo)
                for i in range(4):
                    tehai_all[who][0].remove(int(dahai[-2:]))
            if 'k' in dahai:
                dahai_num = dahai[-2:]
                tehai_all[who][0].append(int(dahai_num))
                tehai_all[who][0].remove(int(dahai_num))
                dahai_pon = dahai[:-2].replace('k', 'p')
                tehai_all[who][1] = [dahai if meld == dahai_pon else meld for meld in tehai_all[who][1]]
                
            print(log_parse_list[loop_count])
            continue
        
        if type(dahai) == str and len(dahai) == 3:
            dahai = int(dahai[1:])

        
        if type(tsumo) == str and len(tsumo) == 9:
            print(log_parse_list[loop_count])
            continue

        if not dahai == 60:
            tehai_all[who][0].remove(dahai)
            if not type(tsumo) == str:
                tehai_all[who][0].append(tsumo)
        
        loop[who] += 1
        
        if dahai == 60:
            dahai = tsumo
        print(log_parse_list[loop_count])
        if str in [type(x) for x in next_tsumo]:
            from_whom = []
            for j ,hai in enumerate(next_tsumo):
                if type(hai) == str:
                    if 'p' in hai:
                        indexi = hai.find('p')
                        before, after = [0, 2, 4], [-1, -2, -3]
                        print(after[before.index(indexi)])
                        from_whom.append((j + after[before.index(indexi)]) % 4)
                    elif 'm' in hai:
                        indexi = hai.find('m')
                        before, after = [0, 2, 6], [-1, -2, -3]
                        from_whom.append((j + after[before.index(indexi)]) % 4)
                    else:
                        from_whom.append(-1)
                else:
                    from_whom.append(-1)
            if who in from_whom:
                if next_tsumo[from_whom.index(who)][-2:] == str(dahai):
                    who = from_whom.index(who)
                    continue
            
        who =  (who + 1) % 4
    
    return log_parse_list

if __name__ == '__main__':
    sample_log = [ [ 1, 0, 0 ],
        [ 25000, 17000, 33000, 25000 ],
        [ 45 ],
        [ 31 ],
        [ 13, 13, 13, 16, 16, 18, 21, 32, 34, 37, 37, 46, 47 ],
        [ 19, 27, 45, 42, 24, 47, 27, 36, 19, 43, "19p1919", 42, "4747p47", 43, 34, 14, 17, "c151416" ],
        [ 21, 60, 60, 32, 60, 34, 60, 42, 36, 60, 37, 60, 37, 60, 60, 18, 60, 16 ],
        [ 11, 16, 17, 26, 26, 29, 29, 35, 38, 38, 39, 41, 42 ],
        [ 44, 25, 21, 34, 37, 39, 31, 11, 24, 29, 26, 17, 47, 12, 15, 23, 44, 13, 33 ],
        [ 42, 44, 11, 21, 38, 60, 60, 60, 26, 60, 60, 60, 60, 60, "r41", 60, 60, 60 ],
        [ 11, 14, 15, 17, 18, 18, 19, 22, 52, 27, 36, 36, 44 ],
        [ 28, 42, 33, 43, 16, 12, 51, 18, 38, 14, "c265227", "c171618", 34, 28, 31, 41 ],
        [ 44, 60, 11, 60, 22, 60, 15, 18, 18, 33, 19, 28, 60, 38, 60, 60 ],
        [ 22, 22, 23, 24, 24, 32, 53, 36, 41, 41, 44, 45, 47 ],
        [ 32, 19, 46, 45, 27, 11, 29, 22, 35, 12, 46, "c345336", "41p4141", 21, 23, 15 ],
        [ 44, 60, 45, 60, 47, 60, 27, 29, 60, 60, 32, 32, 24, 60, 60, 60 ],
        [ "和了", [ -1300, 4900, -1300, -1300 ],
        [ 1, 1, 1, "20符3飜1300点∀", "Fully Concealed Hand(1飜)", "Pinfu(1飜)", "Riichi(1飜)", "Ura Dora(0飜)" ] ] ]
    log_parse_sample = log_parse(sample_log)
    for s in log_parse_sample:
        print(s)