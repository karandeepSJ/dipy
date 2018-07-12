import ui
import window
from pdb import set_trace

cube=ui.Cuboid(size=(10,10,10))
rect1=ui.Rectangle2D(size=(2,2),color=(1,0,0))
rect2=ui.Rectangle2D(size=(2,2),color=(0,1,0))
rect3=ui.Rectangle2D(size=(2,2),color=(0,0,1))
text1 = ui.TextFollower(text='AAAAAA',color=(1,0,0),scale=(1,1,1))
text2 = ui.TextFollower(text='BBBBBB',color=(0,1,0),scale=(1,1,1))
text3 = ui.TextFollower(text='CCCCCC',color=(0,0,1),scale=(1,1,1))
text4 = ui.TextFollower(text='DDDDDD',color=(0,1,1),scale=(1,1,1))
text5 = ui.TextFollower(text='EEEEEE',color=(1,1,0),scale=(2,2,2))
text6 = ui.TextFollower(text='FFFFFF',color=(1,0,1),scale=(1,1,1))
text7 = ui.TextFollower(text='GGGGGG',color=(230/255,92/255,0),scale=(1,1,1))
text8 = ui.TextFollower(text='HHHHHH',color=(1,0,0),scale=(1,1,1))
text9 = ui.TextFollower(text='IIIIII',color=(0,1,0),scale=(2,2,1))
text10 = ui.TextFollower(text='JJJJJJ',color=(0,0,1),scale=(1,1,1))
text11 = ui.TextFollower(text='KKKKKK',color=(0,1,1),scale=(1,1,1))
text12 = ui.TextFollower(text='LLLLLL',color=(1,1,0),scale=(1,1,1))
text13 = ui.TextFollower(text='MMMMMM',color=(1,0,1),scale=(1,1,1))
text14 = ui.TextFollower(text='NNNNNN',color=(230/255,92/255,0),scale=(2,2,1))
text15 = ui.TextFollower(text='OOOOOO',color=(1,0,0),scale=(1,1,1))
text16 = ui.TextFollower(text='PPPPPP',color=(0,1,0),scale=(1,1,1))
text17 = ui.TextFollower(text='QQQQQQ',color=(0,0,1),scale=(2,2,1))
text18 = ui.TextFollower(text='RRRRRR',color=(0,1,1),scale=(1,1,1))
text19 = ui.TextFollower(text='SSSSSS',color=(1,1,0),scale=(1,1,1))
text20 = ui.TextFollower(text='TTTTTT',color=(1,0,1),scale=(2,2,1))
text21 = ui.TextFollower(text='UUUUUU',color=(230/255,92/255,0),scale=(1,1,1))
text22 = ui.TextFollower(text='VVVVVV',color=(1,0,0),scale=(1,1,1))
text23 = ui.TextFollower(text='WWWWWW',color=(0,1,0),scale=(1,1,1))
text24 = ui.TextFollower(text='XXXXXX',color=(0,0,1),scale=(1,1,1))
text25 = ui.TextFollower(text='YYYYYY',color=(0,1,1),scale=(2,2,1))
text26 = ui.TextFollower(text='ZZZZZZ',color=(1,1,0),scale=(1,1,1))

def toggle(i_ren, obj, follower):
	menu.set_visibility(not menu.visibility)
	menu.visibility = not menu.visibility
	i_ren.force_render()
cube.add_callback(cube.actor, "RightButtonPressEvent", toggle)

renderer = window.ren()
current_size = [600, 600]
showm = window.ShowManager(renderer, size=current_size, title="Sci-Fi UI")

# menu=ui.FollowerMenu((0,0,0),5*1.741,renderer.GetActiveCamera(),[rect1,rect2,rect3])
menu=ui.FollowerMenu((0,0,0),5*1.741,renderer.GetActiveCamera(),[text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20,text21,text22,text23,text24,text25,text26])

showm.ren.add(cube)
showm.ren.add(menu)
showm.start()