#gerekli importlar
import random
import turtle
import time

#board yapılanması
drawing_board = turtle.Screen()
drawing_board.title("Catch The Turtle If You Can")

#turtle yapılanması
t = turtle.Turtle()
t.shape("turtle")
t.shapesize(stretch_len=3,stretch_wid=3)
t.speed(0)
t.penup()

#score yazdırma çabaları, score = 0 ı yazdırır.
score = 0
c = t.clone()
c.penup()
c.hideturtle()
c.setposition(0, 280)
scorestring="score: %s" % score
c.write(scorestring, False, align="center", font=("arial", 14, "normal"))

#zamanı yazdırma
timeskip = turtle.Turtle()
timeskipping = 20
timeskip.penup()
timeskip.hideturtle()
timeskip.setposition(0, 300)

#fonksiyonlar

#score func
def tikla(x,y):
    c.undo()
    global score
    score += 1
    c.penup()
    c.hideturtle()
    c.setposition(0, 280)
    scorestring = "Score: %s" % score
    c.write(scorestring, False, align="center", font=("arial", 14, "normal"))

#baştan başlamak için girişim
# def bastan():
#     global timeskipping
#     timeskipping = 20

#ana oyunun fonksiyonu zaman ile aynı orantıda for range ile çalıştırdım
for i in range(timeskipping):
    k = 0
    t.hideturtle()
    #mouse tıkladığımız bölüm direk score u +1 arttırıp c ye yazdırıyor
    t.onclick(tikla, 1)
    #rastgele bir yerlere gitmesi
    t.goto((random.randint(-200,200)),(random.randint(-300,300)))
    scorestring2 = "Time: %s" % timeskipping
    timeskip.write(scorestring2, False, align="center", font=("arial", 14, "normal"))
    timeskipping -= 1
    time.sleep(1)
    #kaybolma süresi için geliştirdiğim formül şimdilik işe yarıyor
    #eğer ki k<var daki var ne kadar büyük olursa o kadar uzun süre görünür kalıyor
    while k < 20:
        t.showturtle()
        k += 1
    timeskip.clear()
    #zaman bittiğinde gerekli işlemleri yapar
    if timeskipping <= 0:
        t.hideturtle()
        c.hideturtle()
        timeskip.hideturtle()
        d = turtle.Turtle()
        d.penup()
        d.hideturtle()
        d.setposition(0, 260)
        d.write("GAME OVER", False, align="center", font=("arial", 16, "normal"))
        # drawing_board.onkey(bastan,"space")


turtle.listen()

drawing_board.mainloop()