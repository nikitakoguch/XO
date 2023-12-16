table = [
   ['-','-','-'],
   ['-','-','-'],
   ['-','-','-']
]

def print_doard(board):
    for row in board:
        for cell in row:
            print(cell, end='')
        print()

def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
        
    for i in range(3):
            if board[0][i] == player and board[1][i] == player and board[2][2] == player:
                return True
                
    if board[0][0] == player and board[1][1] == player and board[2][0] == player:
         return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == [player]:
         return True
    
original_player = 'X'

while True:
     print_doard(table)
     print('Ход игрока', original_player)
     row = int(input('Номер строки:')) - 1
     col = int(input('Номер столбца:')) - 1
     
     if table[row][col] != '-':
          print('Ячейка уже занята')
          continue
     
     table[row][col] = original_player

     if check_win(table, original_player):
          print_doard(table)
          print(f'Игрок {original_player} выиграл!')

     
     if all([cell != '-' for row in table for cell in row]):
         print('Ничья!')
         print_doard()
         break
     
     original_player = '0' if original_player == 'X' else 'X'
     