def pos_maker_dict(pos,dir,dict_imp):
    #혹시라도 실패를 받으면 그냥 실패 반환
    if pos == -1:
        return -1

    pos_x = pos & 3
    pos_y = pos >> 2

    imp_index_pos = list(dict_imp.values())

    #좌상
    if dir == 0:
        if pos_x > 0 and pos_y < 5 :
            pos_x = pos_x-1
            pos_y = pos_y+1
            ret = (pos_y << 2) + pos_x
            if ret in imp_index_pos:
                return -1
            else :
                return ret
    elif dir == 1:
        if pos_y < 5:
            pos_y = pos_y +1
            ret = (pos_y << 2) + pos_x
            if ret in imp_index_pos:
                return -1
            else :
                return ret
        else:
            return -1

    elif dir == 2:
        if pos_x < 3 and pos_y < 5 :
            pos_x = pos_x+1
            pos_y = pos_y+1
            ret = (pos_y << 2) + pos_x
            if ret in imp_index_pos:
                return -1
            else :
                return ret

    elif dir == 3:
        if pos_x < 3 :
            pos_x = pos_x+1
            ret = (pos_y << 2) + pos_x
            if ret in imp_index_pos:
                return -1
            else :
                return ret

    elif dir == 4:
        if pos_x < 3 and pos_y > 0 :
            pos_x = pos_x+1
            pos_y = pos_y-1
            ret = (pos_y << 2) + pos_x
            if ret in imp_index_pos:
                return -1
            else :
                return ret

    elif dir == 5:
        if pos_y > 0 :
            pos_y = pos_y-1
            ret = (pos_y << 2) + pos_x
            if ret in imp_index_pos:
                return -1
            else :
                return ret

    elif dir == 6:
        if pos_x > 0 and pos_y > 0 :
            pos_x = pos_x-1
            pos_y = pos_y-1
            ret = (pos_y << 2) + pos_x
            if ret in imp_index_pos:
                return -1
            else :
                return ret

    elif dir == 7:
        if pos_x > 0 :
            pos_x = pos_x-1
            ret = (pos_y << 2) + pos_x
            if ret in imp_index_pos:
                return -1
            else :
                return ret
    else :
        return -1
    return -1

#--------------------------------------------------------------------------------------
def pos_maker(pos,dir):
    #혹시라도 실패를 받으면 그냥 실패 반환
    if pos == -1:
        return -1

    pos_x = pos & 3
    pos_y = pos >> 2


    #좌상
    if dir == 0:
        if pos_x > 0 and pos_y < 5 :
            pos_x = pos_x-1
            pos_y = pos_y+1
            return (pos_y << 2) + pos_x
        else:
            return -1

    elif dir == 1:
        if pos_y < 5:
            pos_y = pos_y +1
            return (pos_y << 2) + pos_x
        else:
            return -1

    elif dir == 2:
        if pos_x < 3 and pos_y < 5 :
            pos_x = pos_x+1
            pos_y = pos_y+1
            return (pos_y << 2) + pos_x
        else:
            return -1

    elif dir == 3:
        if pos_x < 3 :
            pos_x = pos_x+1
            return (pos_y << 2) + pos_x
        else:
            return -1

    elif dir == 4:
        if pos_x < 3 and pos_y > 0 :
            pos_x = pos_x+1
            pos_y = pos_y-1
            return (pos_y << 2) + pos_x
        else:
            return -1

    elif dir == 5:
        if pos_y > 0 :
            pos_y = pos_y-1
            return (pos_y << 2) + pos_x
        else:
            return -1

    elif dir == 6:
        if pos_x > 0 and pos_y > 0 :
            pos_x = pos_x-1
            pos_y = pos_y-1
            return (pos_y << 2) + pos_x
        else:
            return -1

    elif dir == 7:
        if pos_x > 0 :
            pos_x = pos_x-1
            return (pos_y << 2) + pos_x
        else:
            return -1

    return -1


def pos_maker_d(dir):
    if dir == 0:
        return 3
    elif dir == 1:
        return 4
    elif dir == 2:
        return 5
    elif dir == 3:
        return 1
    elif dir == 4:
        return -3
    elif dir == 5:
        return -4
    elif dir == 6:
        return -5
    elif dir == 7:
        return -1


def dict_transition(dict_1, dict_2):
    dict_2_imp = dict_1.copy()
    dict_1_imp = dict_2.copy()

    for imp_key, imp_val in dict_1_imp.items():
        dict_1_imp[imp_key] = 23 - imp_val

    for imp_key, imp_val in dict_2_imp.items():
        dict_2_imp[imp_key] = 23 - imp_val

    return dict_1_imp, dict_2_imp


def eval(w_dict, r_dict):
    eval_num_w = 0
    eval_num_r = 0

    #1 백 승리 / -1 적 승리 / 0 승리 미정
    win_check = 0
    eval_num_cal = 0

    w_key_list = list(w_dict.keys())
    r_key_list = list(r_dict.keys())

    table_keys = ['p1', 'p2','s1','d','b','c','f','k','q']
    table_vals = [5, 5, 10,10,10,10,10,10,50]

    for eval_num in range(len(table_keys)):
        if table_keys[eval_num] in w_key_list:
            eval_num_w += table_vals[eval_num]
        if table_keys[eval_num] in r_key_list:
            eval_num_r += table_vals[eval_num]


    if eval_num_w <= 50:
        if eval_num_r < eval_num_w :
            win_check = 1
        elif eval_num_r == eval_num_w:
            win_check = -1
        else :
            win_check = -1
    elif eval_num_r <= 50:
        if eval_num_w < eval_num_r:
            win_check = -1
        elif eval_num_r == eval_num_w:
            win_check = -1
        else :
            win_check = 1
    else :
        win_check = 0

    eval_num_cal = eval_num_w - eval_num_r

    return win_check, eval_num_cal
