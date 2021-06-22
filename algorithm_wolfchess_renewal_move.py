from algorithm_wolfchess_renewal_sub import *

#p1 수행명령 dict1,2 를 받아서 결과를 반영한다.
#모든 결과들을 반영한다.
def p1_move(dict_w, dict_r):
    #dict_w2 = dict_w.copy()
    #dict_r2 = dict_r.copy()
    imp_p = dict_w["p1"]

    dict_w_arr = []
    dict_r_arr = []
    orders = []
    imp_order = ''

    imp_vals_r = list(dict_r.values())
    imp_keys_r = list(dict_r.keys())

    for i in range(3):
        if i == 0 or i == 2:
            dict_w2 = dict_w.copy()
            dict_r2 = dict_r.copy()

            imp_pos = pos_maker(imp_p, i, dict_w)

            if imp_pos != -1:
                #적 탐사
                #적 있는 경우에만 수행된다.
                if imp_pos in imp_vals_r:
                    imp_index = imp_vals_r.index(imp_pos)
                    imp_char = imp_keys_r[imp_index]

                    if imp_char != 's1' and imp_char != 's2':

                        imp_pop = dict_r2.pop(imp_char)
                        dict_w2['p1'] = imp_pop

                        dict_w_arr.append(dict_w2)
                        dict_r_arr.append(dict_r2)
                        orders.append('p1'+str(i))

        elif i == 1:
            dict_w2 = dict_w.copy()
            dict_r2 = dict_r.copy()

            imp_pos = pos_maker(imp_p, i, dict_w)

            if imp_pos != -1:
                #적 탐사
                #적 있는 경우에만 수행된다.
                if imp_pos in imp_vals_r:
                    imp_index = imp_vals_r.index(imp_pos)
                    imp_char = imp_keys_r[imp_index]

                    if imp_char != 's1' and imp_char != 's2':

                        imp_pop = dict_r2.pop(imp_char)
                        dict_w2['p1'] = imp_pop

                        dict_w_arr.append(dict_w2)
                        dict_r_arr.append(dict_r2)
                        orders.append('p1'+str(i))
                else :
                    dict_w2['p1'] = imp_pos + 4

                    dict_w_arr.append(dict_w2)
                    dict_r_arr.append(dict_r2)
                    orders.append('p1'+str(i))

    #실패하면
    return dict_w_arr, dict_r_arr, orders


#p2 수행명령
def p2_move(dict_w, dict_r):
    #dict_w2 = dict_w.copy()
    #dict_r2 = dict_r.copy()
    imp_p = dict_w["p2"]

    dict_w_arr = []
    dict_r_arr = []
    orders = []
    imp_order = ''

    imp_vals_r = list(dict_r.values())
    imp_keys_r = list(dict_r.keys())

    for i in range(3):
        if i == 0 or i == 2:
            dict_w2 = dict_w.copy()
            dict_r2 = dict_r.copy()

            imp_pos = pos_maker(imp_p, i, dict_w)

            if imp_pos != -1:
                #적 탐사
                #적 있는 경우에만 수행된다.
                if imp_pos in imp_vals_r:
                    imp_index = imp_vals_r.index(imp_pos)
                    imp_char = imp_keys_r[imp_index]

                    if imp_char != 's1' and imp_char != 's2':

                        imp_pop = dict_r2.pop(imp_char)
                        dict_w2['p2'] = imp_pop

                        dict_w_arr.append(dict_w2)
                        dict_r_arr.append(dict_r2)
                        orders.append('p2'+str(i))

        elif i == 1:
            dict_w2 = dict_w.copy()
            dict_r2 = dict_r.copy()

            imp_pos = pos_maker(imp_p, i, dict_w)

            if imp_pos != -1:
                #적 탐사
                #적 있는 경우에만 수행된다.
                if imp_pos in imp_vals_r:
                    imp_index = imp_vals_r.index(imp_pos)
                    imp_char = imp_keys_r[imp_index]

                    if imp_char != 's1' and imp_char != 's2':

                        imp_pop = dict_r2.pop(imp_char)
                        dict_w2['p2'] = imp_pop

                        dict_w_arr.append(dict_w2)
                        dict_r_arr.append(dict_r2)
                        orders.append('p2'+str(i))
                else :
                    dict_w2['p2'] = imp_pos + 4

                    dict_w_arr.append(dict_w2)
                    dict_r_arr.append(dict_r2)
                    orders.append('p2'+str(i))

    return dict_w_arr, dict_r_arr, orders

#s 수행명령
def s1_move(dict_w, dict_r):
    #dict_w2 = dict_w.copy()
    #dict_r2 = dict_r.copy()
    imp_p = dict_w["s1"]

    dict_w_arr = []
    dict_r_arr = []
    orders = []
    imp_order = ''

    imp_vals_r = list(dict_r.values())
    imp_keys_r = list(dict_r.keys())

    dict_w2 = dict_w.copy()
    dict_r2 = dict_r.copy()

    imp_pos = pos_maker(imp_p, 1, dict_w)
    imp_pos2 = pos_maker(imp_p, 2, dict_w)

    #확인 용도
    imp_check = pos_maker(imp_p, 1, dict_r)
    imp_check2 = pos_maker(imp_p, 2, dict_r)

    if ((imp_pos != -1 ) and (imp_pos2 != -1)):
        if ((imp_check != -1) and (imp_check2 != -1)):
            dict_w2['s1'] = imp_pos + 4
            dict_w2['s2'] = imp_pos2 + 4
            dict_w_arr.append(dict_w2)
            dict_r_arr.append(dict_r2)
            orders.append('s1')

    return dict_w_arr, dict_r_arr, orders

#d 수행명령
def d_move(dict_w, dict_r):

    imp_p = dict_w["d"]

    dict_w_arr = []
    dict_r_arr = []
    orders = []
    imp_order = ''

    imp_vals_r = list(dict_r.values())
    imp_keys_r = list(dict_r.keys())

    imp_pos = [-1,-1]
    imp_pos[0] = pos_maker(imp_p, 1, dict_w)
    imp_pos[1] = pos_maker(imp_pos[0], 1, dict_w)

    #안에 있는 경우
    for i in range(2):

        if imp_pos[i] != -1:

            dict_w2 = dict_w.copy()
            dict_r2 = dict_r.copy()

            if imp_pos[i] in imp_vals_r:
                imp_index = imp_vals_r.index(imp_pos[i])
                imp_char = imp_keys_r[imp_index]

                if imp_char != 's1' and imp_char != 's2':
                    imp_pop = dict_r2.pop(imp_char)
                    dict_w2['d'] = imp_pop

                    dict_w_arr.append(dict_w2)
                    dict_r_arr.append(dict_r2)
                    orders.append('d'+str(i))
            else:
                dict_w2['d'] = imp_pos[i]

                dict_w_arr.append(dict_w2)
                dict_r_arr.append(dict_r2)
                orders.append('d'+str(i))

    return dict_w_arr, dict_r_arr, orders

#b 수행명령
def b_move(dict_w, dict_r):

    imp_p = dict_w["b"]

    dict_w_arr = []
    dict_r_arr = []
    orders = []
    imp_order = ''

    imp_vals_r = list(dict_r.values())
    imp_keys_r = list(dict_r.keys())

    for i in range(4):
        imp_counter = 0
        imp_sub = imp_p
        while True:
            imp_pos = pos_maker(imp_sub, 2*i+1, dict_w)
            imp_counter += 1

            dict_w2 = dict_w.copy()
            dict_r2 = dict_r.copy()

            if imp_pos == -1:
                break
            #적이 있는 경우
            elif imp_pos in imp_vals_r:
                imp_index = imp_vals_r.index(imp_pos)
                imp_char = imp_keys_r[imp_index]

                if imp_char != 's1' and imp_char != 's2':
                    imp_pop = dict_r2.pop(imp_char)
                    dict_w2['b'] = imp_pop

                    dict_w_arr.append(dict_w2)
                    dict_r_arr.append(dict_r2)
                    orders.append('b'+str(2*i+1)+str(imp_counter))
                break
            #적이 없는 경우
            else :
                dict_w2['b'] = imp_pos
                imp_sub = imp_pos

                dict_w_arr.append(dict_w2)
                dict_r_arr.append(dict_r2)
                orders.append('b'+str(2*i+1)+str(imp_counter))

    return dict_w_arr, dict_r_arr, orders

#c 수행명령
def c_move(dict_w, dict_r):

    imp_p = dict_w["c"]

    dict_w_arr = []
    dict_r_arr = []
    orders = []
    imp_order = ''

    imp_vals_r = list(dict_r.values())
    imp_keys_r = list(dict_r.keys())

    for i in range(8):
        #imp_counter = 0
        #imp_sub = imp_p

        imp_pos = pos_maker(imp_p, i, dict_w)
        imp_counter += 1

        dict_w2 = dict_w.copy()
        dict_r2 = dict_r.copy()

        move_success = False

        if imp_pos == -1:
            continue
        elif imp_pos in imp_vals_r:
            imp_index = imp_vals_r.index(imp_pos)
            imp_char = imp_keys_r[imp_index]

            if imp_char != 's1' and imp_char != 's2':
                imp_pop = dict_r2.pop(imp_char)
                dict_w2['c'] = imp_pop
                move_success = True

        else :
            dict_w2['c'] = imp_pos
            move_success = True

        if move_success == True:
            for i in range(8):
                imp_val_c = pos_maker(imp_pos, i, dict_w)
                if imp_val_c != -1:
                    if imp_val_c in imp_vals_r:
                        imp_index = imp_vals_r.index(imp_val_c)
                        imp_char = imp_keys_r[imp_index]
                        if imp_char != 's1' and imp_char != 's2':
                            dict_r2.pop(imp_char)

            dict_w_arr.append(dict_w2)
            dict_r_arr.append(dict_r2)
            orders.append('c'+str(i))
    return dict_w_arr, dict_r_arr, orders

#f 수행명령
def f_move(dict_w, dict_r):

    imp_p = dict_w["f"]

    dict_w_arr = []
    dict_r_arr = []
    orders = []
    imp_order = ''

    imp_vals_w = list(w_dict.values())
    imp_vals_r = list(dict_r.values())
    imp_keys_r = list(dict_r.keys())

    imp_set_w = []
    imp_set_r = []

    for i in range(len(imp_vals_w)):
        imp_set_w.append(imp_vals_w[i]>>2)
    for i in range(len(imp_vals_r)):
        imp_set_r.append(imp_vals_r[i]>>2)

    imp_set_w2 = set(imp_set_w)
    imp_set_r2 = set(imp_set_r)

    imp_list_all = list(imp_set_w2 & imp_set_r2)

    for i in imp_list_all:
        dict_w2 = dict_w.copy()
        dict_r2 = dict_r.copy()

        for j in imp_vals_r:
            if i == (j >> 2):
                imp_index = imp_vals_r.index(j)
                imp_char = imp_keys_r[imp_index]
                if imp_char != 's1' and imp_char != 's2':
                    dict_w2 = dict_w.copy()
                    dict_r2 = dict_r.copy()

                    dict_r2.pop(imp_char)
                    dict_w2.pop('f')

                    dict_w_arr.append(dict_w2)
                    dict_r_arr.append(dict_r2)
                    orders.append('f'+str(i))

    return dict_w_arr, dict_r_arr, orders

#k 수행명령
def k_move(dict_w, dict_r):

    imp_p = dict_w["k"]

    dict_w_arr = []
    dict_r_arr = []
    orders = []
    imp_order = ''

    imp_vals_r = list(dict_r.values())
    imp_keys_r = list(dict_r.keys())

    for i in range(4):

        #최초 한 칸 이동
        imp_pos = pos_maker(imp_sub, 2*i+1, dict_w)

        imp_num = 2*i+2
        if imp_num>=8:
            imp_num = imp_num - 8

        imp_pos2 = []

        imp_pos2[0] = pos_maker(imp_pos, 2*i, dict_w)
        imp_pos2[1] = pos_maker(imp_pos, imp_num, dict_w)

        for i in range(2):
            if imp_pos2[i] != -1:
                dict_w2 = dict_w.copy()
                dict_r2 = dict_r.copy()

                move_success = False

                if imp_pos2[i] in imp_vals_r:
                    imp_index = imp_vals_r.index(imp_pos2[i])
                    imp_char = imp_keys_r[imp_index]

                    #지나가면서 때리기
                    if imp_char != 's1' and imp_char != 's2':
                        imp_pop = dict_r2.pop(imp_char)
                        dict_w2['k'] = imp_pop
                        move_success = True
                else :
                    dict_w2['k'] = imp_pos2[i]
                    move_success = True


                if move_success == True:
                    #이단 경로 제거
                    if imp_pos in imp_vals_r:
                        imp_index = imp_vals_r.index(imp_pos)
                        imp_char = imp_keys_r[imp_index]

                        if imp_char != 's1' and imp_char != 's2':
                            imp_pop = dict_r2.pop(imp_char)

                    dict_w_arr.append(dict_w2)
                    dict_r_arr.append(dict_r2)
                    orders.append('k'+str(2*i+1)+str(imp_num))

    return dict_w_arr, dict_r_arr, orders

#q 수행명령
def q_move(dict_w, dict_r):

    imp_p = dict_w["q"]

    dict_w_arr = []
    dict_r_arr = []
    orders = []
    imp_order = ''

    imp_vals_r = list(dict_r.values())
    imp_keys_r = list(dict_r.keys())

    for i in range(8):
        imp_counter = 0
        imp_sub = imp_p
        while True:
            imp_pos = pos_maker(imp_sub, i, dict_w)
            imp_counter += 1

            dict_w2 = dict_w.copy()
            dict_r2 = dict_r.copy()

            if imp_pos == -1:
                break
            #적이 있는 경우
            elif imp_pos in imp_vals_r:
                imp_index = imp_vals_r.index(imp_pos)
                imp_char = imp_keys_r[imp_index]

                imp_pop = dict_r2.pop(imp_char)
                dict_w2['q'] = imp_pop

                dict_w_arr.append(dict_w2)
                dict_r_arr.append(dict_r2)
                orders.append('q'+str(i)+str(imp_counter))

                break
            #적이 없는 경우
            else :
                dict_w2['q'] = imp_pos
                imp_sub = imp_pos

                dict_w_arr.append(dict_w2)
                dict_r_arr.append(dict_r2)
                orders.append('q'+str(i)+str(imp_counter))

    return dict_w_arr, dict_r_arr, orders
