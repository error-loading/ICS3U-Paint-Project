from pygame import *
from glob import *

class Text:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self, mx, my, size, col):
        comicFont = font.SysFont("Comic Sans MS", size)

        txt = self.getName(mx, my)
        txtPic = comicFont.render(txt, True, (255,0,0))

        self.screen.blit(txtPic,(mx,my))



    def getName(self, mx, my):
        ans = ""                    # final answer will be built one letter at a time.
        arialFont = font.SysFont("Times New Roman", 16)
        back = self.screen.copy()        # copy screen so we can replace it when done
        textArea = Rect(mx,my,200,25) # make changes here.


        cursorShow = 0
        myclock = time.Clock()
        typing = True
        while typing:
            cursorShow += 1
            for e in event.get():
                if e.type == QUIT:
                    event.post(e)   # puts QUIT back in event list so main quits
                    return ""
                if e.type == KEYDOWN:
                    if e.key == K_BACKSPACE:    # remove last letter
                        if len(ans)>0:
                            ans = ans[:-1]
                    elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                        typing = False
                    elif e.key < 256:
                        ans += e.unicode       # add character to ans
                        
            txtPic = arialFont.render(ans, True, (0,0,0))   #
            draw.rect(self.screen,(220,255,220),textArea)        # draw the text window and the text.
            draw.rect(self.screen,(0,0,0),textArea,2)            
            self.screen.blit(txtPic,(textArea.x+3,textArea.y+2))
            if cursorShow // 50 % 2 == 1:
                cx = textArea.x+txtPic.get_width()+3
                cy = textArea.y+3
                draw.rect(self.screen,(255,0,0),(cx,cy,2,textArea.height-6))
            myclock.tick(100)
            display.flip()
            
        self.screen.blit(back,(0,0))
        return ans