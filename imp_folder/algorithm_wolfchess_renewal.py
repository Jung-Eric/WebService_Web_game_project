
from algorithm_wolfchess_renewal_sub import *
from algorithm_wolfchess_renewal_move import *
#white 입장으로 회전시키지

#모든 수행명령은 [ dict_w, dict_r, num ] 이런 식으로 수행
#dict_w / dict_r를 반영한다. eval 값도 반영한다.


#모든 탐색명령은 [ dict1, dict2,
#p1 탐색명령 dict1,2 를 받아서 결과를 반영한다.
#depth_dest = 5

def Min_Max(dict_w, dict_r,depth, side):
    list_MinMax=[]
    list_order=[]

    win_check_imp = 0
    eval_check_imp = 0

    depth_new = depth - 1
    side_new - not(side)

    win_check_imp, eval_check_imp = eval(dict_w, dict_r)


    #eval이 확정이 되었을 때
    if ((win_check == 1) or (win_check == -1)):
        if side == True:
            win_check_imp = win_check_imp * (-1)
            eval_check_imp = eval_check_imp * (-1)
        return [ win_check_imp, eval_check_imp ]
    #미리 eval을 통해서 끝에 다달으면 return 한다.
    elif depth == 0:
        if side == True :
            win_check_imp = win_check_imp * (-1)
            eval_check_imp = eval_check_imp * (-1)
        return [ win_check_imp, eval_check_imp ]

    #white의 작업 턴
    #이제는 판을 바꾸는 방식으로 반복해서 활용한다.
    else :
        #최초의 설정을 제외하고는 계속 판을 회전시킨다. 최초도 False면 회전을 시켜줘야된다
        w_dict = {}
        r_dict = {}

        '''
        if not(side == True and depth == 0) :
            w_dict, r_dict = dict_transition(dict_w, dict_r)
        else :
            w_dict = dict_w.copy()
            r_dict = dict_r.copy()
        '''
        w_dict = dict_w.copy()
        r_dict = dict_r.copy()

        w_dict_all = list(w_dict.keys())

        for w_keys in w_dict_all:

            if w_keys == 'p1':
                imp_dictA_w, imp_dictA_r, imp_orders = p1_move(w_dict, r_dict)
                for i in range(len(imp_orders)):
                    imp_dict_w = imp_dictA_w[i]
                    imp_dict_r = imp_dictA_r[i]

                    list_MinMax.append(Min_Max(imp_dict_r, imp_dict_w,depth_new, side_new))
                    list_order.append()


    #p1 병정1 탐색 명령 / 수행 명령
    #p2 병정2 이동 명령
    #s1 방패병(좌) 이동 명령
    #s2는 존재만 한다.
    #d 이동명령
    #b 이동명령
    #c 곡예사 이동명령
    #f 화염구 이동명령
    #k 용기병 이동명령
    #q 여왕 이동명령


    #return d1의 배열 / d2의 배열 / 명령어의 배정
    result_val = [0,0]
    result_order = ''

    '''
    print('가능한 명령 종류')
    print(len(list_Order))
    '''

    #백색의 경우 최대의 값을 가져온다.
    if side == True:
        #우선 최초 등록
        try :
            result_val = list_MinMax[0]
        except:
            print('가능한 리스트 값 : ' + str(len(list_MinMax)))
        #1번 부터 탐색
        for i in range(1, len(list_MinMax)):
            #새로운 값이 더 크면 당연히 갱신한다.
            if list_MinMax[i][0] > result_val[0]:
                result_val = list_MinMax[i]
                result_order = list_Order[i]
            #새로운 값이 같으면 eval도 비교한다.
            elif list_MinMax[i][0] == result_val[0]:
                if list_MinMax[i][1] > result_val[1]:
                    result_val = list_MinMax[i]
                    result_order = list_Order[i]
            #그 외에는 변함이 없다.


    #적색의 경우 최소의 값을 선출한다.
    elif side == False:
        #우선 최초 등록
        try :
            result_val = list_MinMax[0]
        except:
            print('가능한 리스트 값 : ' + str(len(list_MinMax)))
        #1번 부터 탐색
        for i in range(1, len(list_MinMax)):
            #새로운 값이 더 작으면 당연히 갱신한다.
            if list_MinMax[i][0] < result_val[0]:
                result_val = list_MinMax[i]
                result_order = list_Order[i]
            #새로운 값이 같으면 eval도 비교한다.
            elif list_MinMax[i][0] == result_val[0]:
                if list_MinMax[i][1] < result_val[1]:
                    result_val = list_MinMax[i]
                    result_order = list_Order[i]
            #그 외에는 변함이 없다.

    #마지막일 겨우 추가적인 이동 정보를 제공한다.--------------------------------------------------------
    #그 외에는 win_check / eval_num도 제공한다.

    '''
    if depth == 0:
        return result_order
    else :
        return result_val
    '''

    #d1_arr / d2_arr / 명령어 배정 /

#print(pos_maker(5,1))
#print(pos_maker(3,2))

#dict1 = {'p1':12, 'q':20}
#dict2 = {'s1':11, 'd':10, 'f':14, 'q' : 22}
#print(dict1, dict2)
#print(eval(dict2,dict1))
