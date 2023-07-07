import pygame

pygame.init()

Width = 1100
Height = 800
screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption('Two Player game chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 45)
clock = pygame.time.Clock()
fps = 60

#game varible and images

white_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations =[(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), 
                 (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1) ]

black_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations =[(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), 
                 (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6) ]

captured_pieces_white = []
captured_pieces_black = []
 
#0_whites turn no selection: 1_whites turn piece selected: 2_blacks turn no selection: 3_blacks turn piece selected
turn_step = 0
selection = 100
valid_moves = []

#load in game piece images (qeen,king,knight,bishhop,rook,pawn) x 2
# white pieces
white_queen = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/white_queen.png')
white_queen = pygame.transform.scale(white_queen, (70,70))
white_queen_small = pygame.transform.scale(white_queen, (32,32))

white_king = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/white_king.png')
white_king = pygame.transform.scale(white_king, (70,70))
white_king_small = pygame.transform.scale(white_king, (32,32))

white_bishop = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/white_bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (70,70))
white_bishop_small = pygame.transform.scale(white_bishop, (32,32))

white_knight = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/white_knight.png')
white_knight = pygame.transform.scale(white_knight, (70,70))
white_knight_small = pygame.transform.scale(white_knight, (32,32))

white_pawn = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (55,55))
white_pawn_small = pygame.transform.scale(white_pawn, (32,32))

white_rook = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/white_rook.png')
white_rook = pygame.transform.scale(white_rook, (70,70))
white_rook_small = pygame.transform.scale(white_rook, (32,32))

# black pieces

black_queen = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/black_queen.png')
black_queen = pygame.transform.scale(black_queen, (70,70))
black_queen_small = pygame.transform.scale(black_queen, (32,32))

black_king = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/black_king.png')
black_king = pygame.transform.scale(black_king, (70,70))
black_king_small = pygame.transform.scale(black_king, (32,32))

black_bishop = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/black_bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (70,70))
black_bishop_small = pygame.transform.scale(black_bishop, (32,32))

black_knight = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/black_knight.png')
black_knight = pygame.transform.scale(black_knight, (70,70))
black_knight_small = pygame.transform.scale(black_knight, (32,32))

black_pawn = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (55,55))
black_pawn_small = pygame.transform.scale(black_pawn, (32,32))

black_rook = pygame.image.load('pygameChess-main/pygameChess-main/assets/images/black_rook.png')
black_rook = pygame.transform.scale(black_rook, (70,70))
black_rook_small = pygame.transform.scale(black_rook, (32,32))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_king_small, white_queen_small, white_rook_small, white_knight_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king,black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_king_small, black_queen_small, black_rook_small, black_knight_small, black_bishop_small]

piece_list= ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
#check varibles and flashing counter
counter = 0
winner = ''
game_over = False


#draw main game board
def draw_board():
    for i in range (32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray',[540- (column * 180), row * 90, 90, 90])
        else:
         pygame.draw.rect(screen, 'light gray',[630 - (column * 180), row * 90, 90, 90])
        
        pygame.draw.rect(screen, 'gray',[0, 717, Width, 84])  
        pygame.draw.rect(screen, 'pink',[0, 717, Width, 84], 5)
        pygame.draw.rect(screen, 'pink',[720, 0, 380, 800], 5)
        
        status_text = ['White: select a piece to move' , 'white: select destination!',
                      'Black: select a piece to move' , 'Black: select destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'purple'), (10, 730))
        for i in range(8):
            pygame.draw.line(screen, 'black', (0, 90 * i), (717, 90 * i), 2)
            pygame.draw.line(screen, 'black', ( 90 * i, 0), (90 * i, 717), 2)
        screen.blit(big_font.render('FORFEIT', True, 'black'), (730, 730))

# draw pieces onto board
def draw_pieces():
    for i in range (len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] *90 + 22, white_locations[i][1] * 90 +30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 90 + 10, white_locations[i][1] * 90 + 10))
       
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 90 + 1, white_locations[i][1] * 90 + 1, 90, 90], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn': 
              screen.blit(black_pawn, (black_locations[i][0] * 90 + 22, black_locations[i][1] * 90 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 90 + 10, black_locations[i][1] * 90 + 10))      
       
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 90 + 1, black_locations[i][1] * 90 + 1,
                                                  90, 90], 2)

#function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range ((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list
#check valid king
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friend_list = white_locations
    else:
        enemies_list = white_locations
        friend_list = black_locations
     #8 squares to check for king, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -2),(0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friend_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)


    return moves_list
    

#check valid queen
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

#check valid bishop
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friend_list = white_locations
    else:
        enemies_list = white_locations
        friend_list = black_locations
    for i in range(4): #up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x=1
            y=-1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x=1
            y=1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friend_list and 0 <= position[0] + (chain * x ) <=7 and  0 <= position[1] + (chain * y) <=7:
               moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
               if(position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                   path = False
               chain += 1 
            else:
                path = False

    return moves_list


#check valid rook moves
def check_rook(position, color):
    moves_list =[]
    if color == 'white':
        enemies_list = black_locations
        friend_list = white_locations
    else:
        enemies_list = white_locations
        friend_list = black_locations
    for i in range(4): #down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x=0
            y=1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x=1
            y=0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friend_list and 0 <= position[0] + (chain * x ) <=7 and  0 <= position[1] + (chain * y) <=7:
               moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
               if(position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                   path = False
               chain += 1 
            else:
                path = False

    return moves_list 

#check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if(position[0], position[1] + 1) not in white_locations and (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if(position[0], position[1] + 2) not in white_locations and (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if(position[0] + 1, position[1] + 1) in black_locations :
             moves_list.append((position[0] + 1, position[1] + 1))
        if(position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))

    else:
        if(position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if(position[0], position[1] - 2) not in white_locations and (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if(position[0] + 1, position[1] - 1) in white_locations :
             moves_list.append((position[0] + 1, position[1] - 1))
        if(position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

#check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friend_list = white_locations
    else:
        enemies_list = white_locations
        friend_list = black_locations
    #8 squares to check for knight, they can go two squares in one direction and one in aother
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2),(-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friend_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)

    return moves_list

#check valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options 

#draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range (len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 90 + 45, moves[i][1] * 90 + 45), 5)
#draw captured pieces on side of screen 
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50 * i))
#draw a flashing squre around king of in check
def draw_check():

    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 90 + 1, white_locations[king_index][1] * 90 + 1, 90, 90], 5)

    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 90 + 1, black_locations[king_index][1] * 90 + 1, 90, 90], 5)


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to restart', True, 'white'), (210, 240))                

#main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')

run = True
while run :
    clock.tick(fps)
    if counter < 30:
        counter+= 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)


    #event handiling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over: 
            x_coord = event.pos[0] // 90
            y_coord = event.pos[1] // 90
            click_coords = (x_coord, y_coord) 
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                           winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options( black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

        if turn_step > 1 :
            if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
            if click_coords in black_locations:
                selection = black_locations.index(click_coords)
                if turn_step == 0:
                    turn_step = 1
            if click_coords in valid_moves and selection != 100:
                black_locations[selection] = click_coords
                if click_coords in white_locations:
                    white_piece = white_locations.index(click_coords)
                    captured_pieces_black.append(white_pieces[white_piece])
                    if white_pieces[white_piece] == 'king':
                           winner = 'black'
                    white_pieces.pop(white_piece)
                    white_locations.pop(white_piece)
                black_options = check_options( black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
                turn_step = 0
                selection = 100
                valid_moves = []

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                            'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
                white_locations =[(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), 
                            (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1) ]

                black_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                            'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
                black_locations =[(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), 
                            (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6) ]

                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
    
    if winner != '': 
            game_over = True
            draw_game_over()    

    pygame.display.flip()
pygame.quit()
