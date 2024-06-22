with open ('Scores.txt','r') as f1:
    print(f1.read)


#####################################################################################################

#Quiz Program

import time
print('Computer Science Summer Holiday Homework- 2020-21')
time.sleep(1)

print('Project By- Dhruva Parashar')
time.sleep(1)
print('Class & Sec- XII-D')
time.sleep(1)
print('Roll No.- 10')
time.sleep(1)
print('Topic: QUIZ')
time.sleep(1)
print()
print("WELCOME TO QUIZANIA!!!!!!")
time.sleep(1)
print()
a=input('Would You Like to Play the Most Fascinating QUIZ???  (Yes/No):')
if a=='Yes' or a=='yes':
    print('So Good!!! Let us proceed then!')
    time.sleep(1)
    b=input('Enter Your Name: ')
    print()
    print('First read the Rules Thoroughly.')
    time.sleep(1)
    print('1. There are 10 MCQs in the Quiz.\n 2. Each Question carries 5 Points.\n 3. ZERO marks will be awarded in the Question if it is wrongly attempted.\n 4. There are No Hints Available and DO NOT CHEAT in the Quiz!!!!.\n 5. WRITE ONLY THE OPTION NUMBER IN THE SPACE.')
    time.sleep(10)
    print()
    print('You are now ready to start the Quiz. All The Best!!!')
    time.sleep(1)
    print()
    print()
    print('Q1. Which was the First Indigeniously built Fighter Aircraft of India? (Write Correct Option No.)')
    time.sleep(1)
    print(' (1). HAL LCA Tejas\n (2). Dassault Rafael\n (3). HAL HF-24 Marut\n (4). HAL Ajeet')
    c=input('Answer Here: ')
    if c=='3':
        print('Good',b,'!!!, Correct Answer')
        print(' (3). HAL HF-24 Marut which was built in 1961 by Kurt Tank.')
    else:
        print('Sorry',b,',Wrong Answer')
        time.sleep(1)
        print('The Correct Answer is (3). HAL HF-24 Marut which was built in 1961 by Kurt Tank.')
    time.sleep(3)
    print()
    print('Next Question.')
    time.sleep(1)
    print()
    print('Q2. Which was the first SUPER-COMPUTER of India? ')
    time.sleep(1)
    print(' (1). ARYABHATT 2000\n (2). PARAM Ishan\n (3). Sahasrat (CRAY XC40)\n (4). PARAM 8000')
    d=input('Answer Here: ')
    if d=='4':
        print('Woahhh!!!',b,'Right Answer.')
        print(' (4). PARAM 8000 was built in 1991 by C-DAC.')
    else:
        print('Ohhh!!! You were close',b,'. But Wrong Answer.')
        time.sleep(1)
        print('The Correct Answer is (4). PARAM 8000 was built in 1991 by C-DAC.')
    time.sleep(3)
    print()
    print('Next Question.')
    time.sleep(1)
    print()
    print("Q3. The Motto of Indian Air Force 'Nabhah Sparsham Deeptam' is taken from which Ancient Literature? ")
    time.sleep(1)
    print(' (1). Rig Veda\n (2). Bhagvad Gita\n (3). Hitopdesh\n (4). Anandmath')
    e=input('Answer Here: ')
    if e=='2':
        print('So Gooood',b,'. Keep Going!!!')
        print(" (2). 'Nabhah Sparsham Deeptam' is a hymn from Bhagvad Gita.")
    else:
        print('Wrong Answer',b,'.')
        time.sleep(1)
        print('The Correct Answer is (2). Bhagvad Gita.')
    time.sleep(3)
    print()
    print('Next Question.')
    time.sleep(1)
    print()
    print("Q4. 'Kalinga Cup' is related to which Sport?")
    time.sleep(1)
    print(' (1). Cricket\n (2). Hockey\n (3). Football\n (4). Badminton')
    f=input('Answer Here: ')
    if f=='3':
        print('Corrrrrrect',b,'!!!')
        print(" (3). 'Kalinga Cup' is related to Football.")
    else:
        print('Wrong Answer',b,'.')
        time.sleep(1)
        print(' The Correct Answer is (3). Football.')
    time.sleep(3)
    print()
    print('Next Question.')
    time.sleep(1)
    print()
    print("Q5. What is the Minimum Age required to be eligible for the Post of 'President of India'?")
    time.sleep(1)
    print(' (1). 35 yrs.\n (2). 40 yrs.\n (3). 21 yrs.\n (4). 18 yrs.')
    g=input('Answer Here: ')
    if g=='1':
        print('Right Answer',b,'!!!')
        print(" (1). 35 yrs. is the Min. Age to be eligible for the Post of 'President of India'.")
    else:
        print('Ohhoo..... Wrong Answer',b,'.')
        time.sleep(1)
        print('The Correct is (1). 35 yrs.')
    time.sleep(3)
    print()
    print('Next Question.')
    print()
    print("Q6. The foundation stone for a missile park called 'Agneeprastha' has been laid in which among the following naval ship?")
    time.sleep(1)
    print(" (1). INS Kalinga\n (2). INS Vikrant\n (3). INS Tarkash\n (4). INS Shivalik")
    h=input('Answer Here: ')
    if h=='1':
        print('Right Answer',b,'!!!')
        print('(1). INS Kalinga')
    else:
        print('Wrong Answer',b)
        time.sleep(1)
        print('The Correct answer is (1). INS Kalinga.')
    time.sleep(3)
    print()
    print('Next Question.')
    print()
    print("Q7. What was the Name of the First Satellite Launched by India?")
    time.sleep(1)
    print(" (1). BHASKARA-1\n (2). ARYABHATT\n (3). CHANDRAYAAN-1\n (4). ROHINI")
    i=input('Answer Here: ')
    if i=='2':
        print('Corrrrrrect Answerrrrr',b,'!!!')
        print('(2). ARYABHATT was the First Satellite Launched by India in 1975 from Soviet Union and aboard a Soviet Launcher.')
    else:
        print('Wrong Answer',b)
        time.sleep(1)
        print('The Correct Answer is (2). ARYABHAT')
    time.sleep(2)
    print()
    print('Next Question.')
    print()
    print("Q8. Who is the First Lieutenant Governor of the newly formed Union Territory of Ladakh?")
    time.sleep(1)
    print(" (1). Satyapal Malik\n (2). Girish Chandra Murmu\n (3). B.D. Mishra\n (4). Radha Krishna Mathur")
    j=input('Answer Here: ')
    if j=='4':
        print('Woahhh.....Right Answer',b)
        print('(4). R.K. Mathur was appointed as the First L.G. of Ladakh on 31st October 2019.')
    else:
        print('Ohhh.... Wrong Answer',b)
        time.sleep(1)
        print('The Correct Answer is (4). Radha Krishna Mathur.')
    time.sleep(2)
    print()
    print('Next Question.')
    print()
    print("Q9. Which countries hosted the World Environment Day-2020?")
    print(" (1). Thailand-Vietnam\n (2). Colombia-Thailand\n (3). Colombia-Germany\n (4). Germany-Vietnam")
    k=input('Answer Here: ')
    if k=='3':
        print('Great',b,'!!! Right Answer')
        print('(3). Colombia hosted the World Environment Day-2020 in partnership with Germany.')
    else:
        print('Wrong Answer',b)
        time.sleep(1)
        print('The Correct Answer is (3). Colombia-Germany.')
    time.sleep(2)
    print()
    print('Last Question.')
    print()
    print("Q10. When is Indian Armed Forces Flag Day Celebrated?")
    print(" (1). 7 December\n (2). 15 January\n (3). 25 May\n (4). 8 November")
    l=input('Answer Here: ')
    if l=='1':
        print('Wowww!!! Correct',b)
        print('(1). The Indian Armed Forces Flag Day is Celebrated on 7th December.')
    else:
        print('Wrong Answer',b)
        time.sleep(1)
        print('The Correct Answer is (1). 7 December.')
    time.sleep(3)
    print()
    print('The QUIZ is over. I hope you enjoyed it and learnt something new.')
    time.sleep(4)
    print('Thank You for your Participation.')
elif a=='No' or a=='no':
    print('Okay User. Play the Quiz whenever you are free. You will learn something really interesting from this QUIZ.')
print()    
time.sleep(1)

#####################################################################################################

if a=='Yes' or a=='yes':

    with open ('Scores.txt','a') as f2:
        user=b
        s=int(input('How many did you attempt correctly???'))
        l1=str([user, s])
        f2.write(l1)

    
#####################################################################################################
    
import mysql.connector as m
con=m.connect(user='root', host='localhost', passwd='dhruva13', database='QUIZ')
cur=con.cursor()
#cur.execute('CREATE TABLE scores (Name varchar(20), Score int(5))')
if a=='Yes' or a=='yes':
    t=(b,s)
    cur.execute(f'INSERT INTO scores VALUES{t};')
    con.commit()
    con.close()
