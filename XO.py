import datetime # אחראי על הצגת זמן ותאריך 

 

# הכנסת ערכים מספריים לתוך הרשימה - על מנת לדעת מיקומים על לוח המשחק
theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }



board_keys = [] # מערך שבו יכנסו ערכי אינדקס




for key in theBoard:  # מעבר על הרשימה עם המיקומים - והכנסת כל ערך מ1-9 למערך
    board_keys.append(key) 

    

###################################################################################


# תפריט ראשי
def Menu(): 
    print("\n\t<<<<<<<<<<<<<<< Welcome to Tic Tac Toe Game >>>>>>>>>>>>>>>")
    print()

    option = input("""
                               Game Menu 
                       <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        1: Start to play
                        2: Rules Game
                        3: View player history
                        4: Exit/Quit
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n
                        Enter your option please:""")
    
    print("")

    if option == "1":
       for key in board_keys:
           theBoard[key] = " "    #אתחול לוח המשחק בכל פעם על מנת לשחק משחק חדש
       game()
    elif option == "2":
       Rules()
    elif option == "3":
       ReadFile()
    elif option == "4":
       Exit()
    else: 
      print("""
                        Unknown Option Selected! try again
                        ----------------------------------
                        """)
  
      Menu()
      

   
###################################################################################


def ReadFile():# הצגת היסטוריית השחקנים כאופציה בתפריט
    
    try:
        
       file = open(r"C:\Tic Tac Toe\XOXO.txt", "r")
       print(file)
       print(" ")
       print(file.read())
       BackToMenu()

    except FileNotFoundError:
        
           print('The file was not created, please start playing')
           BackToMenu()
           

##################################################################


# אפשרות המשתמש לבחור אם לחזור לתפריט או לא
def BackToMenu():
    back = input("Do you want to return to the main menu?(y/n)")
    if back == "y" or back == "Y": 
       Menu()
    elif back == "n" or back == "N":
       return
    else:
       print("Invalide input, please try again..")
       BackToMenu()



##################################################################

    
def Rules(): # הצגת חוקי המשחק 
    print("\n\t\t\tHow to Play Tic-Tac-Toe:")
    print("\t\t\t------------------------")
    print("Tic-tac-toe, noughts and crosses, is a paper-and-pencil game for two players,\nX and O, who take turns marking the spaces in a 3×3 grid.\nThe player who succeeds in placing three of their marks in a diagonal,\nhorizontal, or vertical row is the winner.\nIt is a solved game with a forced draw assuming best play from both players\n\n")
    BackToMenu()


################################################################

# פונקציה האחראית על מה שיופיע בקובץ כטקסט
def WriteFile(player1,player2,now,theBoard,turn):

    my_out_file = open(r"C:\Tic Tac Toe\XOXO.txt", "a") # --> "a" - Append - יתווסף לסוף הקובץ
    print("\n\n")
    my_out_file.write("\n\nPlayer History on date: " + now.strftime("%Y-%m-%d %H:%M:%S")+"\n\n")
    my_out_file.write("Name Player1 (X): " + player1 + "\n")
    my_out_file.write("Name Player2 (O): " + player2 + "\n\n")
    my_out_file.write("The WINNER is:\n\n" + turn + "\n\n")
    my_out_file.write("Result of the game:\n\n" + str(theBoard) + "\n==========================================================================================\n")
    
    print(" ")

    print("It's OK - the files were written\n")
    my_out_file.close() # אחראי לסגירת הקובץ אם הוא פתוח




################################################################

# פונקציה המאפשרת למשתמש לבחור אם לשחק שוב או לא בסוף המשחק
def PlayAgain():
    restart = input("Do you want to play Again?(y/n)")
    
    if restart == "y" or restart == "Y":  
        for key in board_keys: # אתחול לוח המשחק
            theBoard[key] = " "

        game() # במידה והמשתמש בוחר להמשיך לשחק המשחק יתחיל מחדש

    elif restart == "n" or restart == "N":
        Menu() # במידה ולא - חוזר לתפריט
    
    else:
        print("Invalide input, please try again..")
        PlayAgain()



##################################################################

# אפשרות יציאה
def Exit(): 
    print("BYE BYE DUDE!")
    return


##################################################################


# פונקציה המאפשרת הדפסה של לוח המשחק
# שימוש במערך שבו נכנסו כל המפתחות מהרשימה
def printBoard(board): 

    print(board['1'] + '   |  ' + board['2'] + ' | ' + board['3'])
    print('----+----+----')
    print(board['4'] + '   |  ' + board['5'] + ' |  ' + board['6'])
    print('----+----+----')
    print(board['7'] + '   |  ' + board['8'] + ' |  ' + board['9'])




  ################################################# GAME FUNCTION #############################################


# הפונקציה הראשית של המשחק שאחראית על כל תהליכי המשחק העיקריים
def game():

    turn = 'X'
    count = 0 # משתנה הסוכם את כמות סיבובי המשחק שהתבצעו
   
    print(' ')
    

   ###########################################################

         
    now = datetime.datetime.now() # משתנה להצגת זמן ותאריך 

   
    # קליטת שמות שחקנים
    print("Player 1")
    player1 = input("Enter your name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter your name : ")
    print("\n")

   

  ###########################################################


    while len(theBoard) != ' ':


        printBoard(theBoard) # הדפסת לוח המשחק



        # בדיקות עבור הצגת שם השחקן לפי איקס או עיגול
        if turn == 'X':
           print("\n"+ player1 +" you are "+ turn + ",choose a number between 1-9\n")
        else:
           print("\n"+ player2 +" you are "+ turn + ",choose a number between 1-9\n")



  ###########################################################
       
        
        # מתן עזרה לשחקן במהלך המשחק - כולל תפריט עזרה
        needHelp = input("Do you need some help? (y/n)")
        
        if needHelp == "y" or needHelp == "Y":
           print()

           option = input("""
                               Help Options
                       -------------------------------------
                        1: Displays the game board
                        2: View empty places are left on the board
                        3: I regret, let me go back to playing
                       -------------------------------------\n
                        Enter your option please:""")


           
           print("")

           
           if option == "1": # אופציית עזרה - הצגת לוח המשחק לפי מיקומים 
              print("\n\n\t\t\t\t Game Board: \n")
              print("\n------------------------------------------------------------------------------------------\n")
              print(theBoard)
              print("\n------------------------------------------------------------------------------------------\n")
              print("\n")
              continue


           elif option == "2": # אופציית עזרה 2 - הצגת מספר המקומות הריקים שנותרו על הלוח
               print("\n")
               empty = len(theBoard) - count
               print("Places are left in the game board: " + str(empty))
               print("\n\n")
               continue
            
            
           elif option == "3": 
               continue

            
           else:
              print("Unknown Option Selected! try again")
              continue



        # קליטת מיקום מהמשתמש        
        elif needHelp == "n" or needHelp == "N":
             print("\nSo which box do you choose?\n")
             move = input() 
             print("\n")

        else:
             print("Invalide input, please try again..")
             continue


        ###########################################################

          

        
        # טיפול בשגיאות
        if len(move) == 1 and move.isalpha() == False and move.isdigit(): # אם אורך הקלט 1,הקלט לא מכיל אותיות,והקלט הוא מספר

           if int(move) < 1 or int(move) > 9: # בדיקת טווחי מספרים תקינים לקליטה
              print("Invalide input, please try again..")
              continue

            
           else:
               
              if theBoard[move] == ' ': # אם המיקום בלוח ריק- ניתן להכניס בו איקס או עיגול ואז הכמות עולה ב1 כל פעם  
                 theBoard[move] = turn  # Insert a value into the board - הכנסת הערך לתוך הלוח
                 count += 1 

           
              else: # אחרת- המיקום בלוח תפוס
                 print("\nThat place is already filled.\n\nMove to which place?\n")
                 continue
                
            
        else: # אם התנאי הראשי שלמעלה לא מתקיים אז הפלט שגוי - הדפסת הודעה מתאימה
              print("Invalide input, please try again..")
              continue

            


################################################################################
            

        
        # כעת בודקים אם יש מנצח אחרי 5 סיבובים או יותר במשחק
        # יש מספר סטים אפשריים שבהם יכול אחד מהשחקנים לנצח (סטים של 3)
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # למעלה
                printBoard(theBoard)
                print("\nGame Over.\n")
                if turn == 'O':
                   print(" **** " +player2 + "(" + turn + ")" + " won ****")
                elif turn == 'X':
                   print(" **** " +player1 + "(" + turn + ")" + " won ****")
                WriteFile(player1,player2,now,theBoard,turn) #sent data to Write File - they need to be written in the file.
                PlayAgain()
                break
            
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # באמצע
                printBoard(theBoard)
                print("\nGame Over.\n")
                if turn == 'O':
                   print(" **** " +player2 + "(" + turn + ")" + " won ****")
                elif turn == 'X':
                   print(" **** " +player1 + "(" + turn + ")" + " won ****")
                WriteFile(player1,player2,now,theBoard,turn)
                PlayAgain()
                break
            
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # למטה
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if turn == 'O':
                   print(" **** " +player2 + "(" + turn + ")" + " won ****")
                elif turn == 'X':
                   print(" **** " +player1 + "(" + turn + ")" + " won ****")
                WriteFile(player1,player2,now,theBoard,turn)
                PlayAgain()
                break
            
            elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ': # מלמטה למעלה בצד שמאל
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if turn == 'O':
                   print(" **** " +player2 + "(" + turn + ")" + " won ****")
                elif turn == 'X':
                   print(" **** " +player1 + "(" + turn + ")" + " won ****")
                WriteFile(player1,player2,now,theBoard,turn)
                PlayAgain()
                break
            
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ': # מלמטה למעלה באמצע
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if turn == 'O':
                   print(" **** " +player2 + "(" + turn + ")" + " won ****")
                elif turn == 'X':
                   print(" **** " +player1 + "(" + turn + ")" + " won ****")
                WriteFile(player1,player2,now,theBoard,turn)
                PlayAgain()
                break
            
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ': # מלמטה למעלה בצד ימין
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if turn == 'O':
                   print(" **** " +player2 + "(" + turn + ")" + " won ****")
                elif turn == 'X':
                   print(" **** " +player1 + "(" + turn + ")" + " won ****")
                WriteFile(player1,player2,now,theBoard,turn)
                PlayAgain()
                break
            
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # אלכסוני
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if turn == 'O':
                   print(" **** " +player2 + "(" + turn + ")" + " won ****")
                elif turn == 'X':
                   print(" **** " +player1 + "(" + turn + ")" + " won ****")
                WriteFile(player1,player2,now,theBoard,turn)
                PlayAgain()
                break
            
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # אלכסוני
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if turn == 'O':
                   print(" **** " +player2 + "(" + turn + ")" + " won ****")
                elif turn == 'X':
                   print(" **** " +player1 + "(" + turn + ")" + " won ****")
                WriteFile(player1,player2,now,theBoard,turn)
                PlayAgain()
                break 





       # כאשר כל הלוח מלא כבר ואין זוכה אז זה תיקו
        if count == 9:
         print("\nGame Over.\n")                
         print("It's a Tie!!")
         PlayAgain()




        

        
        # שינוי ממשתמש איקס לעיגול וההפך בכל תור
        if turn =='X':
           turn = 'O' 
           
        else:
           turn = 'X'



        
        
    

###################################################################################
        
        
def main():
    main()

if __name__ == "__main__":

    Menu()
    
  
