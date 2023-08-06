# Game starts here
label start:

#...

scene bg example with fade
play music "bg.mp3" 
show idle_image with dissolve

$ result = renpy.imagemap("idle_image.png", "hovered_image.png", [
(0, 232, 381, 909, "choice 1"), 
# You can find image coordinates in developer menu (Shift + D) and take first and second value + first and second value on the line below
# But you need to select the area strictly starting from the upper left corner to the lower right!!!
(377, 266, 821, 900, "choice 2"),
(814, 247, 1208, 889, "choice 3")
], focus="imagemap")
if result == "choice 1":
    jump choice 1
if result == "choice 2":
    jump choice 2
if result == "choice 3":
    jump choice 3

label choice 1:
"You are the best!"
jump next

label choice 2:
"You are cool!"
jump next

label choice 3:
"I hope this method helped you in your project"
jump next

label next:
"It's over"

return
