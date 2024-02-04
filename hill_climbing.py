#100sudoku 有81行， 每行都是一个 正常的数独游戏 ，for循环
#没用提供的字典，不是太熟悉，还是选择用二维数组

def from_file(filename, sep='\n'):
    "Parse a file into a list of strings, separated by sep."
    return open(filename).read().strip().split(sep)


def shuffled(seq):
    "Return a randomly shuffled copy of the input sequence."
    seq = list(seq)
    random.shuffle(seq)
    return seq


import time, random



#入参 二维数组
def initial(val):
    length = len(val)

    puzzle_arr =  val

    numbers = list(range(1,10))


    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            shuffled_numbers = shuffled(numbers)

            for k in range(3):
                for l in range(3):

                    if puzzle_arr[i + k][j + l] == 0:
                        for candidate in shuffled_numbers:

                            if candidate not in [puzzle_arr[i + m][j + n] for m in range(3) for n in range(3)]:
                                puzzle_arr[i + k][j + l] = candidate
                                shuffled_numbers.remove(candidate)
                                break

    return puzzle_arr


#just for test initial()
def print_care(sukudo):
    leng = len(sukudo)
    for i in range(0, 9):
        for j in range(0, 9):
            print(sukudo[i][j] , end=" ")
        print()



#用于检测初始化已经有的数字 不可以参与swap 入参 二维数组 出参：数组tuple
def detector(sudoku):


    unchanged_tuple = []

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):


            for k in range(3):
                for l in range(3):

                    if sudoku[i + k][j + l] != 0:
                        unchanged_tuple.append((i+k,j+l))

    return unchanged_tuple



# 找到一个宫里可进行交换的数字，初始化已经有数字的不能动
def find_all_possibilities(arr,pos1, pos2, li):
    swaps=[]
    for i in range(3):
        for j in range(3):
            if (i+pos1,j+pos2) not in li: #初始化已经存在的数字不能进行交换
                swaps.append((i,j))

    return best_swap(arr,swaps,pos1,pos2)



def best_swap(arr,swaps,pos1,pos2):
    origi = conflict_count(arr)
    min_conflicts = float('inf')
    best_swap_pair = None
    for i in range(len(swaps)):
        for j in range(i + 1, len(swaps)):
            swap1 = swaps[i] #example : (1,1)
            swap2 = swaps[j]

            # 转换为全局坐标
            global_swap1 = (swap1[0] + pos1, swap1[1] + pos2)
            global_swap2 = (swap2[0] + pos1, swap2[1] + pos2)

            # 模拟交换两个位置的值（使用全局坐标）
            arr[global_swap1[0]][global_swap1[1]], arr[global_swap2[0]][global_swap2[1]] = arr[global_swap2[0]][
                global_swap2[1]], arr[global_swap1[0]][global_swap1[1]]

            current_conflicts = conflict_count(arr)

            # 如果当前冲突数更少，更新最佳交换对
            if current_conflicts < min_conflicts:
                min_conflicts = current_conflicts
                best_swap_pair = (swap1, swap2)  # 保存局部坐标

            # 撤销交换
            arr[global_swap1[0]][global_swap1[1]], arr[global_swap2[0]][global_swap2[1]] = arr[global_swap2[0]][
                global_swap2[1]], arr[global_swap1[0]][global_swap1[1]]

    if min_conflicts > origi:
        return None


    if best_swap_pair:
        global_best_swap1 = (best_swap_pair[0][0] + pos1, best_swap_pair[0][1] + pos2)
        global_best_swap2 = (best_swap_pair[1][0] + pos1, best_swap_pair[1][1] + pos2)
        arr[global_best_swap1[0]][global_best_swap1[1]], arr[global_best_swap2[0]][global_best_swap2[1]] = \
        arr[global_best_swap2[0]][global_best_swap2[1]], arr[global_best_swap1[0]][global_best_swap1[1]]
        return best_swap_pair




#检测冲突（每行＋每列）
def conflict_count(arr):

    length = len(arr)
    total_conflict = 0
    for i in range (9):
        row_confilct = 9 - len(set(arr[i]))
        templist = []
        for j in range(length):
            templist.append(arr[j][i])

        col_confilct = 9 - len(set(templist))

        total_conflict = total_conflict + row_confilct + col_confilct

    return total_conflict


def hill_climbing(val,list):

    init = initial(val)

    conflict_nums = conflict_count(init)


    #print('coflict '+str(conflict_nums))

    attempts = 0 #没招了

    while conflict_nums > 0 :
        #attempts += 1
        #print('conflict now' + str(conflict_nums))
        random_num1 = random.choice([0, 3, 6])
        random_num2 = random.choice([0, 3, 6])
        best_pair = find_all_possibilities(init,random_num1, random_num2, list)

        if best_pair is not None:
            conflict_nums_after = conflict_count(init)
            if conflict_nums_after < conflict_nums:

                conflict_nums = conflict_nums_after
                #print(conflict_nums)

        else:
            # 理论上如果没有找到更好的交换
            print('No better swap found.')
            break  # 或者尝试其他策略

    return conflict_nums


#100sudoku 文件 由一行字符串改成 数组 二维的 9*9
def parse_file(one_row_in_file):
    sudoku_grid = []

    for i in range(0, 81, 9):
        l = []
        for j in range(9):
            digit = int(one_row_in_file[i + j])
            l.append(digit)
        sudoku_grid.append(l)

    return sudoku_grid

def solve_prob(grids):
    count = 0
    for gird in grids:
        start = time.time()
        arr = parse_file(gird)
        li = detector(arr)
        global_conflicts_number = hill_climbing(arr,li)
        t = time.time() - start
        count += 1
        print(f'puzzle {count} : {global_conflicts_number} conflicts done in {"%.2f" % t} seconds')


#execute：
solve_prob(from_file("100sudoku.txt"))





























    # init = initial()
# print_carre(init)
# num_before = conflict_count(init)
# print(num_before)
# print("--------------------------")
# swap(init,3,3)
# print_carre(init)
# num_after = conflict_count(init)
# print(num_after)



# puzzle = random_puzzle(17) # Assuming you have defined all necessary functions and variables from the original code
# print_puzzle(puzzle)
# print(puzzle)

