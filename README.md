Isaac Gonzalez				              					          4/7/2024
Major Project Documentation
Learning Python
	My major project came about when a friend of mine from home told me about some challenge problems he was doing for personal development as a CS major.  As an engineering major myself I have had little to no experience with actual CS classes outside of some java in high school and barely any experience scratching the surface of C in a digital microsystems class. My friend and I have always been skillfully close and having each other to motivate one another on personal projects aids in maintaining a competitive focus. I chose Python as my initial language of choice due to a research prospect I have for next semester. The professor told me I would need to be more proficient in Python for it. While I am aware I still have much to learn these challenges offered interesting fundamental practice to which I expanded upon beyond the scope of the original task. 
 
Rock Paper Scissors at High Noon

The initial challenge proposed was to make the rock paper scissors bot. Admittedly this did not take as long as initially expected. A lot of my struggles with the project came from not being knowledgeable on commonly used statements that simplified the process. Out of the three games I made this one was by far the easiest. It provided a smooth introduction to taking user inputs, taking a randomized value from an array, and utilizing if statements to compare strings. One of the largest developments from this project for me was the .upper(), .strip(), and .lower() functions. These functions were useful in ensuring users could input answers without worrying about case sensitivity which in turn simplified the program. The strip function was useful for clearing unnecessary white space that users may have input as well.  Upon completing the initial challenge, I expanded on the task. I was aiming to improve upon my current understanding of nested loops, so I added streak counters for the number of consecutive ties, losses, or wins. At first, I was extremely puzzled by indenting. I didn’t understand how indenting was crucial for orderly code execution and only noticed after looking up information on nested loops. The ability to add a flare of personality to each of the scripts was rather entertaining to me too. Each program felt more personal with touches like that.

Hang Man Also at Noon

 I began to seek out other rudimentary programing challenges to further familiarize myself with simple python. I had started with the idea of tic tac toe but quickly found it to be more challenging than I was expecting. I had already been planning to do hang man, so I began on what felt simpler first. The most difficult part was getting the hangman to look right in an array. My initial plan to horizontally write out each phase utilizing “\n” to create a new line within a string proved to be confusing and unproductive. It only made the code extremely clustered, difficult to read, and difficult to adjust. I know I left a comment in the file, but I did end up ripping the set up for the hangman from a tutorial. I couldn’t manage to get things to properly align. Although the main focus of the project was checking a randomized string for specific letters a then gradually revealing said guesses. This challenge taught me about generating a blank string based upon the length of a randomly generated word by multiplying a single character by the length of the randomized string. When initially approaching the issue, I was under the assumption it would require a complicated loop, but I have found many simple solutions to problems I originally perceived to be difficult throughout this project. Using the .append() taught me how to add a variable string onto a pre-established array to create a list of attempted letters to check against for repeats. The .join() function worked similarly to update the array of used string variables. .isalpha() checked inputs to ensure they were letters of the alphabet. The enumerate() function was especially interesting to me. It allowed for the sequential indexing of letters in a string. This allowed the program to check the randomized word for repeated letters and filled them in appropriately upon the blank string. Indexing itself became another interesting tool. It was briefly used in the rock paper scissors project to check a short list but now I was learning to use indexing to check for individual letters in a word. My favorite part about this one was the ascii art skull you get for losing. Having creative control really personalized the experience of making these programs. 
 
Tic Tac Toe with a Wizard

Tic Tac Toe with a Wizard felt like my greatest challenge that required numerous revisions due to a lack of understanding of functions and arguments. My initial set up had different values of the tic tac toe grid assigned to variable names that were represented by “*” place holders. Whenever I tried to manipulate those variables through functions, I was only able to extract their string value of “*” instead of passing a value onto the variable name and changing the attached strings. This led to me taking a different approach that saw the creation of a larger array representing the board that could be easily called. I had been stuck on that aspect of the project for a significant portion of time unable to solve the problem until I ultimately had to take a different. This left me wondering if I had truly done something wrong or if I simply could not overcome this gap in my understanding.  This program felt like a crowning achievement. The opening allows for customization of difficulty and if the human or the script gets to play first as well as an explanation on how inputs are registered to the board. This script saw a lot heavier use of functions which I was able to use to varying degrees of success. The best feature is the randomized wizard phrases made before each attack that over dramatize such a simple script. On difficulty one the script will always attack at random and capture obligatory sectors. On difficulty two I attempted to have the program make decisions based upon the player’s previous input. If the script goes first on difficulty two it will always take the middle section to block off the player and then it will make the following moves based on where the first player input was made. Either +/- 1 sector depending on the available space. Not with the intention of beating the player, just the intention of forcing stalemates. I had originally planned to have the second difficulty pick a direction to attempt to make a loop in unless blocked but this task became far too confusing for me. The scoring portion is the most simplistic and crude. Each condition is cleared after every time a player makes a move until either the wizard or the human wins. This portion was challenging for the most unnecessary of reasons. My use of repetition in code made reading the portion rather difficult and disorienting. I continually missed multiple improper indents and had misplaced integers within my indexing causing the program to repeatedly hiccup to my confusion. This was a lesson in debugging and proof reading. Always checking for indents and proper use of “==” and “=”.  If anything, this project as a whole has reminded me of my fondness for coding and the joy of finally overcoming an issue that has you stumped for days.

The Big Kahuna & git pushing.

The big Kahuna was a file where I was able to compile the different games onto allowing for the ability to play all three from one terminal and with significantly less code appearing in the compiler. This was initially confusing as I was unsure of how to call of the main functions to one file. Thankfully I received help from Eden. Eden also helped me push the git hub to publish my files. I had never used git hub before and that was a deeply confusing task, so I am greatly appreciative of that. If anything, it reminded me of what a great resource CSH is for learning. There are so many people in the org far more experienced than me. I know this project may not seem like much to innovative prowess of the CS majors but after everything I’ve learned I am only field to continue my pursuit of knowledge in the field of computer science. Especially Linux. I know so little about it, but I see everyone using it all the time and it looks so intriguing and almost Hollywood esque. It seems so versatile and foundational to furthering my knowledge of CS. I hope to learn so much more on floor and continue growing as one of the stay engineering majors of CSH. 
Overall, I learned a significant amount about the basics of python through exploring coding challenges and building upon them to expand my knowledge. I had never used git hub before, I had never explored beyond even half of what I learned over the course of these challenges. I even outpaced my friend back home. It was so easy to become engrossed and see opportunities to add onto what was already being asked. The loops and streaks were easy enough to implement but the more adventurous aspects of the tic tac toe bot threw me towards the winds of learning. 