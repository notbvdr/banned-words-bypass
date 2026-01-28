
#i'm just beginner and i found this idea so i start coding for fun and learning new stuff :)
#DISCORD : notbvdr
#Twiter : https://x.com/notbvdr
#---------------------------------------------------------#
def seofriendly(seo):
  wordseo=""
  wordseo=lghdar+seo+lghdar
  return wordseo
def eye(notseo):
    notfriend=""
    for twila in notseo:
        notfriend+=twila+lghdar
    return notfriend
def save(saveword):
  
  with open('word.txt', 'a+', encoding="utf-8") as f:
    f.write(saveword+ "\n")
  print("Done !! Check file word.txt")
def start():

  level=input('''1- Low Level Bypass (Seo Friendly)
2- High Level Bypass (not friendly for seo)
Enter Number :''')
  return level   

lghdar="󠀡󠀡"
check=start()

if check == "1":
  save(seofriendly(input("Enter Your Word Or Enter 0 To stop:")))
elif check == "2":
  save(eye(input("Enter Your Word:")))
 
else:
  print("ONLY 1 And 2 Availble For now")
  exit()



    

    

