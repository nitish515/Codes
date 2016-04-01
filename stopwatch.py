import simplegui
max_time=6000
msg='0:00.0'
count=0
score=0
trail=0
def format(text):
    global msg
    m_sec=text%10
    sec=((text-m_sec)/10)%60
    mit=((text-m_sec)/10)/60
    if sec>=10:
        msg = str(mit)+':'+str(sec)+'.'+str(m_sec)
    else:
        msg = str(mit)+':0'+str(sec)+'.'+str(m_sec)
def tick():
    global count
    count = count+1
    format(count)
    if count ==max_time :
        time.stop()
def watch(canvas):
    global msg
    canvas.draw_text(msg, (90,110), 50,'White')
    canvas.draw_text(str(score)+'/'+str(trail), (270,20), 20,'Red')
def handle_1():
    time.start()
def handle_2():
    global score, trail
    time.stop()
    if count%10==0:
        score=score+1
    else:
        trail=trail+1
def handle_3():
    global msg,count,score,trail
    score=0
    trail=0
    msg = '0:00.0'
    count = 0
    

time = simplegui.create_timer(100, tick)
fun = simplegui.create_frame('Stopwatch', 300, 200)
fun.set_draw_handler(watch)
fun.add_button('start', handle_1, 100)
fun.add_button('stop', handle_2, 100)
fun.add_button('reset', handle_3, 100)
fun.start()
