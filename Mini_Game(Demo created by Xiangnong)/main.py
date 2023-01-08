import pygame

pygame.init()

WIDTH, HEIGHT=1600, 1200
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman(French Revolution Edition)")
FPS=60

YELLOW=(255,255,0)
BLUE=(0,255,0)
BLACK=(0,0,0)
font = pygame.font.SysFont("arial", 50)

buttons=[]
hang_pic=[pygame.image.load("Pictures/1.png"),pygame.image.load("Pictures/2.png"),pygame.image.load("Pictures/3.png"),
          pygame.image.load("Pictures/4.png"),pygame.image.load("Pictures/5.png"),pygame.image.load("Pictures/6.png"),
          pygame.image.load("Pictures/7.png")]

word="Hello"
hang=0
guessed=[]

def check(guess):
    if(guess.upper() in word.upper()):
        return True
    return False

def getButton(x,y):
    global buttons
    for button in buttons:
        if x>=button[1]-50 and x<=button[1]+50:
            if y>=button[2]-50 and y<=button[2]+50:
                if button[4]:
                    return button[5]
    return None

def get_output():
    global word
    output=''
    for i in word:
        found=False
        for j in guessed:
            if i.upper()==j.upper():
                output+=i+' '
                found=True
        if not found:
            output+='_ '
    return output


def draw_window():
    WIN.fill(YELLOW)
    for button in buttons:
        if button[4]:
            pygame.draw.circle(WIN,BLUE,(button[1],button[2]),button[3])
            letter = font.render(chr(button[5]), 1, BLACK)
            WIN.blit(letter,(button[1]-letter.get_width()//2,button[2]-letter.get_height()//2))
    WIN.blit(hang_pic[hang],(450,300))
    output=font.render(get_output(),1, BLACK)
    output_width=output.get_width()
    WIN.blit(output,((WIDTH//2-output_width//2),900))
    pygame.display.update()

def end(win=False):
    #pygame.time.delay(2000)
    if win==True:
        text="You win!"
    else:
        text="You lose!"
    WIN.fill(YELLOW)
    win_text=font.render(text,1,BLACK)
    WIN.blit(win_text, (WIDTH//2-win_text.get_width()//2,HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.quit()

def main():
    global hang
    run=True
    clock=pygame.time.Clock()
    for i in range(26):
        x=1500//13*(i%13+1)
        y=100+i//13*110
        buttons.append([BLUE,x,y,50,True,65+i])
    while run:
        clock.tick(FPS)
        draw_window()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                if getButton(x,y)!=None:
                    i=getButton(x,y)
                    letter=chr(i)
                    i-=65
                    guessed.append(letter)
                    buttons[i][4] = False
                    if check(letter):
                        if get_output().count('_')==0:
                            end(True)
                    else:
                        if hang!=5:
                            hang+=1
                        else:
                            end()

    pygame.quit()

if __name__ == "__main__":
    main()
