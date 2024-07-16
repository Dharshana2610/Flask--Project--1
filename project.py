#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def Moral_Story  ():
    return "<div style='background:cyan'><center><h1>The Farmer and the Snake</center></h1><br><p>Once upon a time, a farmer was walking through his fields on a bitterly cold winter's morning. He noticed something strange on the ground – a snake, stiff and frozen from the cold. Taking pity on the creature, the farmer picked it up, tucked it inside his coat to warm it, and hurried home.Once home, the farmer laid the snake by the hearth, where it slowly began to thaw. As the snake revived, it bit the farmer, delivering a lethal dose of venom. Feeling the poison course through his veins, the farmer exclaimed, I saved your life, and in return, you kill me!,The snake looked at the farmer and hissed, You knew I was a snake when you picked me up.<br><br><hr><br><br>Moral:<br> Kindness should not be given blindly. Beware of who you help, for not everyone will return kindness with kindness.<br><br></hr></p></div>"
if __name__=='__main__':
   app.run(debug=True)    