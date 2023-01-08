import pygame

pygame.init()

WIDTH, HEIGHT=1600, 1200
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman(French Revolution Edition)")
FPS=60

YELLOW=(255,255,0)
BLUE=(0,255,0)
BLACK=(0,0,0)
btn_font = pygame.font.SysFont("arial", 50)

buttons=[]
pic=pygame.image.load("Pictures/1.png")

word="Hello"
hang=1

def check(guess):
    if(guess.upper() in word.upper()):
        return True
    return False

def getButton(x,y):
    for button in buttons:
        if x>=button[1]-50 and x<=button[1]+50:
            if y>=button[2]-50 and y<=button[2]+50:
                return button[5]
    return None

def draw_window():
    WIN.fill(YELLOW)
    for button in buttons:
        pygame.draw.circle(WIN,BLUE,(button[1],button[2]),button[3])
        letter = btn_font.render(chr(button[5]), 1, BLACK)
        WIN.blit(letter,(button[1]-letter.get_width()//2,button[2]-letter.get_height()//2))
    WIN.blit(pic,(400,600))
    pygame.display.update()

def end(win=False):
    print(1)

def main():
    run=True
    clock=pygame.time.Clock()
    for i in range(26):
        x=1500//13*(i%13+1)
        y=100+i//13*110
        buttons.append([BLUE,x,y,50,True,65+i])
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                if getButton(x,y)!=None:
                    letter=getButton(x,y)-65
                    if buttons[letter][4]:
                        buttons[letter][4]=False
                        if check(letter):
                            print(1)
                            end(True)
                        else:
                            if hang!=7:
                                hang+=1
                            else:
                                end()



    pygame.quit()

if __name__ == "__main__":
    main()
