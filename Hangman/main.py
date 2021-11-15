def draw_hang_loser():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|        /|\   \n")
    print("|        / \   \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head_body_legs_la():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |\   \n")
    print("|        / \   \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head_body_legs():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |    \n")
    print("|        / \   \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head_body_ll():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |    \n")
    print("|          \   \n")
    print("|              \n")
    print("|              \n")   

def draw_hang_head_body():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |    \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")

def draw_hang_scaffold():
    print(" _________     \n")
    print("|         |    \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")

def draw_hangman(state):
    if state == 0:
        draw_hang_scaffold()
    elif state == 1:
        draw_hang_head()
    elif state == 2:
        draw_hang_head_body()
    elif state == 3:
        draw_hang_head_body_ll()
    elif state == 4:
        draw_hang_head_body_legs()
    elif state == 5:
       draw_hang_head_body_legs_la()
    elif state == 6:
        draw_hang_loser()
        
        
def blanks_gone(s):
  # You must implement this
  # Look up the find() function for strings
  return False

def replace_all(orig, working, ch):
  done = False
  count = 0
  while not done:
    idx = orig.find(ch)
    if idx != -1:
      count = count + 1
      orig = orig[:idx] + "_" + orig[idx+1:]
      working = working[:idx] + ch + working[idx+1:]
    else:
      done = True
  return count != 0, orig, working 
  
def main():
  # You must implement this
    
main()

    
