board_ = [[".","8","7","6","5","4","3","2","1"],
          ["2",".",".",".",".",".",".",".","."],
          ["3",".",".",".",".",".",".",".","."],
          ["4",".",".",".",".",".",".",".","."],
          ["5",".",".",".",".",".",".",".","."],
          ["6",".",".",".",".",".",".",".","."],
          ["7",".",".",".",".",".",".",".","."],
          ["8",".",".",".",".",".",".",".","."],
          ["9",".",".",".",".",".",".",".","."]]
def board(board):
    dicio = {}
    c = 0
    x = 3
    lista_3x3 = []
    for line in range(len(board)):
        lista = []
        for value in range(len(board[line])):
            if value < x and line < x:
                lista_3x3.append(board[line][value])

            else:
                if len(lista_3x3) != len(set(lista_3x3)):
                    print(value, line, board[line][value], x)
                    print(lista_3x3, set(lista_3x3))
                    return False
                x+=3
                lista_3x3 = []

            if board[line][value] == ".":
                continue
            
            elif value == c:
                dicio[(line)] = board[line][value]
            
            lista.append(board[line][value])

        set_lista =  set(board[line])
        set_lista.remove('.')

        if len(lista) != len(set_lista):
            return False
        
    if len(set(dicio.values()))!=len(list(dicio.values())):
        return False
    
    return True
result = board(board_)
