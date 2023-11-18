def createPoison(pocet: number):
    global piece_of_poison
    for index in range(pocet):
        piece_of_poison = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        piece_of_poison.set_position(randint(28, 228), randint(28, 228))
def createFood(pocet2: number):
    global piece_of_food
    for index2 in range(pocet2):
        piece_of_food = sprites.create(img("""
                . . 2 2 b b b b b . . . . . . . 
                            . 2 b 4 4 4 4 4 4 b . . . . . . 
                            2 2 4 4 4 4 d d 4 4 b . . . . . 
                            2 b 4 4 4 4 4 4 d 4 b . . . . . 
                            2 b 4 4 4 4 4 4 4 d 4 b . . . . 
                            2 b 4 4 4 4 4 4 4 4 4 b . . . . 
                            2 b 4 4 4 4 4 4 4 4 4 e . . . . 
                            2 2 b 4 4 4 4 4 4 4 b e . . . . 
                            . 2 b b b 4 4 4 b b b e . . . . 
                            . . e b b b b b b b e e . . . . 
                            . . . e e b 4 4 b e e e b . . . 
                            . . . . . e e e e e e b d b b . 
                            . . . . . . . . . . . b 1 1 1 b 
                            . . . . . . . . . . . c 1 d d b 
                            . . . . . . . . . . . c 1 b c . 
                            . . . . . . . . . . . . c c . .
            """),
            SpriteKind.food)
        piece_of_food.set_position(randint(28, 228), randint(28, 228))

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite)
    scene.camera_shake(4, 500)
    info.change_score_by(1)
    if info.score() == NUMBER_OF_FOOD:
        game.show_long_text("Time: " + str(game.runtime()), DialogLayout.TOP)
        game.game_over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

piece_of_food: Sprite = None
piece_of_poison: Sprite = None
NUMBER_OF_FOOD = 0
tiles.set_current_tilemap(tilemap("""
    level2
"""))
eater = sprites.create(assets.image("""
    Eater
"""), SpriteKind.player)
eater.set_position(25, 25)
controller.move_sprite(eater, 100, 100)
scene.camera_follow_sprite(eater)
NUMBER_OF_FOOD = 10
createFood(NUMBER_OF_FOOD)
createPoison(5)