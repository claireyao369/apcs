import time
import random

# Introduction of the rules of the game
# print("Welcome, Detective Casey! I am your personal AI assistant! Here are some quick rules and some things worth knowing during your work:\n1. \033[33mYellow texts\033[0m indicates a collectable item that will be stored in your inventory\n2. \033\033[31mRed texts\033[0m indicates a NPC\n3. \033[34mBlue texts\033[0m indicates interactive items\n4. \033[32mGreen texts\033[0m indicates narration/hints\n5. ALWAYS input the EXACT input indicated, or else the program will not run properly\nGood luck, and I will always be available when you need a hint!\n\n")

# Start of the game (background information)
# print("===================================")

# NOTES FROM LAST NIGHT:
# 1. Add a anti-stupid code for every chat message
# 2. Add comments
print("You opened your mailbox, there is \033[33ma letter\033[0m inside...")
print(" --------------------------------------------------------------\n|                                                              |")
print("|  Dear Detective Casey,                                       |")
print("|  Greetings, and I hope this letter finds you in good health  |")
print("|  . Check apartment 123, you will find Lucas Blackwood's      |")
print("|  body there. I am not playing a game, and you should get in- |")
print("|  to work ASAP. I heard Ray Kensington, his best friend,      |")
print("|  has not been sighted recently, if I were you, I would       |")
print("|  contact him. Here is his number: 251-433-0608. I warn you   |")
print("|  it is more complicated than you thought...                  |")
print("|                                                              |")
print("|  Best regards,                                               |")
print("|  A friend                                                    |")
print("|                                                              |")
print(" -------------------------------------------------------------- ")
print("\nWhen you searched around Lucas's apartment, you found \033[34mLucas's Journal\033[0m covered in blood, but you don't have the password to open it")
print("\nYou felt chill on your back. Your \033[34mvirtual phone\033[0m lit up...")
print("\033[32mHint: Use 'Messages' to contact Ray Kensington\033[0m")

# Initial constant variables
contacts = {
    "Ray Kensington": "251-433-0608",
    "Stella Fredman": "888-498-1778",
    "Felix Rogers": "770-555-5948"
}

# Initialize all variables
gameEnd = False

ray_messages = {
  "detective_intro" : [
    "Woa ok, well i didnt do nothing bad, how can i help you tho?",
    "Oh ur that person that goes around and ask random questions huh, whats this time about?",
    "Ok wow, first time in my life i ever get questioned by a detective lol, what can i do for Mr. Sherlock?"
  ],
  "apartment_confront_about_lucas": [
    "Oh yea i heard... i never knew until a few days ago cuz i havent talk to him for a long time, he is too busy chatting with Stella Fredman",
    "So ur coming for that... well its a shame isnt it, now lover boys gone whos gonna flirt with Stella Fredman",
    "Ok thats a sad topic... I bet Stella Fredman was crying her heart out those days"
  ],
  "ask_about_stella" : [
    "Just one of Lucas's girls, she has nothing to do with the case i knew for a fact, she is with me that night",
    "Oh, Lucas's 'everthing' lol, shes with me that night fyi, so she cant have anything to do with the case",
    "Ur suspecting her?? Shes with me when Lucas died just so you know, she cant possibilly do anything..."
  ],
  "ask_about_ray_stella" : [
    "Idk if i should say it...or if she wants me to say it...Its nothing about Lucas's death i swear!",
    "I swear its nothing about Lucas's death! But i dont really want to say it...",
    "Oh nonono its nothing to do with Lucas's death i swear! I just dont really want ppl to know"
  ]
}

unstable_ray_messages = {
  "detective_intro" : [
    "Hi..? Y are u back? I thought it was over",
    "Hi... im sorry idk why ur back, i thought it is all over now right"
  ],
  "lucas_accuse" : [
    "Lucas...Lucas... Hes gone isnt he?? Im not the one that made it happened, u know that right??",
    "Im so sorry im sorry Lucas, but hes gone isnt he? I didnt do anything!!",
    "PLS! Tell me u know its not me! I already tried to provide u with info, u know its not me right?!"
  ],
  "truth_about_felix" : [
    "Wait wut??? Did u say Dr. Rogers was trying to manipulate me??",
    "NO...Ur definitely lying, Dr. Rogers will never...",
    "But he could never! Dr. Rogers is not that kind of person!"
  ],
  "truth_in_journal" : [
    "U...u read it!? Then u know! U KNOW he was trying to ruin everything!!",
    "Wait u read it!? Then u KNOW he was leaving me behind for her!",
    "No! Ur lying, Lucas is lying, everyones lying!"
  ]
}

stella_messages = {
  "detective_intro" : [
    "Oh hi! But why I dont understand...I am not even there...",
    "Hi detective, why are you contacting me? I wasnt even there when it happened...",
    "Hi detective! I am not even there during the crime, how am I a suspect.."
  ],
  "about_ray_alibi" : [
    "Oh...yes, he is with me...But we are not doing anything wrong! We were just chatting about something's wrong with Lucas...",
    "Yes...I was with Ray, but we were just talking about something about Lucas, and thats all!",
    "Oh... me and Ray were together, but we were just talking about Lucas, we didnt do anything!"
  ],
  "about_lucas" : [
    "I dont know why you asked but I have almost nothing to do with him. I am friends with Ray, thats how I know Lucas",
    "Im sorry I cannot help you. I dont know Lucas that well. I know Ray and Ray knows him, thats all",
    "Sorry, I dont really know him"
  ],
  "confess_about_lucas" : [
    "Oh...I mean if you already knew...ok, I mean I have feelings for him and he likes me too, we are kind of secretly dating...",
    "Wait he told you?? Ok...I admit that me and Lucas is secretly kinda dating if you wanna call it that way...",
    "Wait he did?? Well...ok, we are secretly dating..."
  ],
  "about_ray_lucas" : [
    "I mean now I told you my secrets now... Ray is kinda obsessed with Lucas, Idk why",
    "Ok... so what know, Ray is kinda obsessed with Lucas. He wants to know everything about him, and he follows him around...",
    "Ray is really obsessed with Lucas, idk why but its kinda creepy"
  ],
  "about_conversation" : [
  "Ray said Lucas doesnt seem like a good guy, he suspect that Lucas want to do smth bad to his friends...",
  "Ray told me about how he suspect Lucas is up to something really bad...",
  "Ray said Lucas doesnt seem like a good person to be around with..."
  ],
  # Ray said his therapist Dr. Felix Rogers suggest him to not go around Lucas...
  "therapist_contact" : [
    "Ok..Here is Felix Rogers's contact, name: Felix Rogers, number: 770-555-5948...",
    "Fine, here is his contact, name: Felix Rogers, number: 770-555-5948",
    "Ok, here is his contact, name: Felix Rogers, number: 770-555-5948"
  ]
  # She has to go, but warns the player about the danger
}

urgent_stella_messages = {
  "find_ray" : [
    "Wait what!? I saw him a few hours ago and he seems fine! What happened?",
    "Oh what!? At his apartment?"
  ],
  "rogers_danger" : [
    "I knew that therapist was off! It was him all along!",
    "I knew it! Ray said Rogers had a key to his place for emergencies, but I knew it wasn't just that!"
  ],
  "save_ray" : [
    "I am already on my way, Bring whatever you can, if Rogers is there, we don't have much time, detective! See you there",
    "I am already out the door. I won't let anything happen to him! Be careful, detective! See you there"
  ]
}

felix_messages = {
  "detective_intro" : [
    "Hi Detective, always glad to help, so you are contacting me for?",
    "Greetings Detective, glad to provide a few details",
    "Hi Detective, would love to collaborate"
  ],
  "about_lucas_case" : [
    "Oh yes... It's always a tragedy when a young life is lost",
    "Oh definitely... It is such a huge tragedy, and it brough huge impact to the community..."
  ], 
  "about_ray" : [
    "Yes, Ray has been under my care for quite some times, very nice young man but just a bit unstable. He needs to learn to control his relationships",
    "Oh yes, I have been taking care of him, very complicated young man, always have his own thoughts...",
    "Yes, Ray is instead a nice person to be around with, but he gets sensitive sometimes..."
  ],
  "about_ray_lucas" : [
    "They were best buds, but I'm afraid people like Lucas is too impulsive, not the best one to be around",
    "Yes I heard, they were really close. Even though I told Ray multiple times, but I believe Lucas is not the best influence for someone like Ray who struggles with emotional regulations",
    "Yes. I'm afraid Ray is far too close with Lucas, which he formed unhealthy attatchments with, and I don't think that is good for someone like Ray..."
  ],
  "about_ray_mental" : [
    "I know Ray quite well. He can get unstable sometimes, but I will say he is just sensative. I always warn him to not go to the bars with Lucas all night and drown himself in those \033[32mWhiskey\033[0m bottles, but he never listen...",
    "He is quite a nice young guy, spontaneous, but sometimes get mentally unstable... partially due to his all-night \033[32mWhiskey\033[0m drinking with Lucas at the bars...",
    "Ray is a guy with nice heart but has an unstable mentality. It takes quite some tries to get him out of the bars and \033[32mWhiskey\033[32m with Lucas, but he doesn't listen to me"
  ],
  "about_ray_violence" : [
    "Oh no Ray could never. Even though people like him always act sensative and spontaneous, but never dangerous to others",
    "Emotions like jealousy and fear are often uncontrollable for people like Ray, but violence? No, I never sense that"
  ]
}
currentView = "home"
game_state = "Act 1"
ray_online = True
stella_online = True
felix_online = True
contact_names = []
contact_numbers = []
# 1. 📩 Messages  
# 2. ☎️ Contacts  
# 3. 📁 Evidence  
# 4. 🌐 Browser  
# 5. 🧩 Puzzles (Locked)

# Views
def homescreenView():
  print(" =========[\N{mobile phone} VIRTUAL PHONE HOME SCREEN]=========")
  print("")
  print("1. 📩 Messages")
  print("2. 📖 Lucas's Journal")
  print(" ========================================= ")
  choice = input("Select an option (1/2): ")
  if choice == "1":
    return "messages"
  elif choice == "2":
    return "journal"
  else:
    print("Invalid choice")
    return "home"

def messageView():
  global game_state
  global ray_online
  global stella_online
  
  def chatWithRay(gameState):
    global ray_online
    global game_state
    if ray_online == False:
      print("\033[31mRay Kensington\033[0m appears offline...")
      input("Press enter to return to the home screen.")
      return "home"
    if gameState == "Act 1":
      print("------CHAT WITH \033[31mRAY KENSINGTON\033[0m------")
      # detective_intro
      ray_online = True
      print("\033[31mRay\033[0m: Hello, um who r u?")
      print("\033[32mHint: Tell him your name\033[0m")
      uinput1 = input("You: ").lower()
      time.sleep(1)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      if "detective" in uinput1 or "casey" in uinput1:
        print("\033[31mRay\033[0m: " + random.choice(ray_messages["detective_intro"]))
      else:
        print("\033[31mRay\033[0m: I dont know what u r talking about, sorry I cant help")
        print("\033[32mChat ended, you can restart in messages\033[0m")
        return "messages"
      # apartment_confront_about_lucas
      print("\033[32mHint: Ask about Lucas Blackwood\033[0m")
      uinput2 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      if "lucas" in uinput2:
        print("\033[31mRay\033[0m: " + random.choice(ray_messages["apartment_confront_about_lucas"]))
      # ask_about_stella
      print("\033[32mHint: Ask about Stella\033[0m")
      uinput3 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      if "stella" in uinput3:
        print("\033[31mRay\033[0m: " + random.choice(ray_messages["ask_about_stella"]))
      else:
        print("\033[31mRay\033[0m: Ok i dont really have time for your questions, i gotta meet with Stella")
      # ask_about_ray_stella
      print("\033[32mHint: Ask why Ray is with Stella\033[0m")
      uinput4 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      if "what did" in uinput4 or "you and stella" in uinput4 or "night" in uinput4 or "stella and you" in uinput4 or "you guys" in uinput4 or "with you" in uinput4 or "with her" in uinput4 or "with stella" in uinput4:
        print("\033[31mRay\033[0m: " + random.choice(ray_messages["ask_about_ray_stella"]))
      time.sleep(2)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      print("\033[31mRay\033[0m: I gotta go, but here is Stella's contact 888-498-1778, ask her if u want...")
      ray_online = False
      print("\033[31mRay Kensington\033[0m appears offline...")
      print("\033[32mHint: Now go back and contact Stella Fredman\033[0m")
      input("Press enter to return to the home screen.")
      game_state = "Act 2"
      return "home"
    elif gameState == "Act 5":
      print("------CHAT WITH \033[31mRAY KENSINGTON\033[0m------")
      # detective_intro
      ray_online = True
      print("\033[31mRay\033[0m: " + random.choice(unstable_ray_messages["detective_intro"]))
      # lucas_accuse
      print("\033[32mHint: Say this is about Lucas\033[0m")
      uinput1 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      if "lucas" in uinput1:
        print("\033[31mRay\033[0m: " + random.choice(unstable_ray_messages["lucas_accuse"]))
      # truth_about_felix
      print("\033[32mHint: Calm Ray down and talk about the truth about Dr. Rogers\033[0m")
      uinput2 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      if "rogers" in uinput2 or "felix" in uinput2 or "truth" in uinput2:
        print("\033[31mRay\033[0m: " + random.choice(unstable_ray_messages["truth_about_felix"]))
      # truth_in_journal
      print("\033[32mHint: Tell him you looked at the journal\033[0m")
      uinput3 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      if "lucas" in uinput3 or "journal" in uinput3 or "lucas's journal" in uinput3:
        print("\033[31mRay\033[0m: " + random.choice(unstable_ray_messages["truth_in_journal"]))
      # After conversation
      time.sleep(2)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      print("\033[31mRay\033[0m: Hes here... Hes here! I think i have to go! Dr. Rogers is here")
      time.sleep(3)
      print("You: Ray! What's happening!? Are you safe right now? Where are you?")
      time.sleep(2)
      print("\033[31mRay\033[0m is typing...")
      time.sleep(2)
      print("\033[31mRay\033[0m: NO hes here! I really have to go im sorry! Im so sorry for Lucas!")
      time.sleep(2)
      print("You: No, NO! RAY!? Don't leave! Try to stay in contact and stay calm!")
      time.sleep(2)
      print("\033[31mRay Kensington\033[0m appears offline...")
      print("\033[32mOh no...Ray is now in serious danger... You have to grap Stella ASAP to go to Ray's apartment to check him out. Move quick!\033[0m")
      game_state = "Act 6"
      input("Press enter to return to the home screen.")
      return "home"
  def chatWithStella(gameState):
    global game_state
    global stella_online
    global gameEnd
    if stella_online == False:
      print("\033[31mStella Fredman\033[0m appears offline...")
      input("Press enter to return to the home screen.")
      return "home"
    if gameState == "Act 2":
      print("------CHAT WITH \033[31mSTELLA FREDMAN\033[0m------")
      # detective_intro
      stella_online = True
      print("\033[31mStella\033[0m: Hi! How can I help you!")
      print("\033[32mHint: Tell him your name\033[0m")
      uinput1 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      if "detective" in uinput1 or "casey" in uinput1 or "lucas" in uinput1:
        print("\033[31mStella\033[0m: " + random.choice(stella_messages["detective_intro"]))
      # about_ray_alibi
      print("\033[32mHint: Ask about her and Ray\033[0m")
      uinput2 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      if "ray" in uinput2 or "with ray" in uinput2 or "with" in uinput2:
        print("\033[31mStella\033[0m: " + random.choice(stella_messages["about_ray_alibi"]))
      # about_lucas
      print("\033[32mHint: Ask about her relationship with Lucas Blackwood\033[0m")
      uinput3 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      if "lucas" in uinput3:
        print("\033[31mStella\033[0m: " + random.choice(stella_messages["about_lucas"]))
      # confess_about_lucas
      print("\033[32mHint: Lie that Ray already told you about everything, so she can confess\033[0m")
      uinput4 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      if "lucas" in uinput4 or "already" in uinput4 or "ray had" in uinput4 or "ray had" in uinput4 or "ray already" in uinput4:
        print("\033[31mStella\033[0m: " + random.choice(stella_messages["confess_about_lucas"]))
      # about_ray_lucas
      print("\033[32mHint: Now ask about Ray and Lucas\033[0m")
      uinput5 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      if "lucas" in uinput5 and "ray" in uinput5:
        print("\033[31mStella\033[0m: " + random.choice(stella_messages["about_ray_lucas"]))
      # about_conversation
      print("\033[32mHint: Ask about what did Stella and Ray talked about that night\033[0m")
      uinput6 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      if "you and ray" in uinput6 or "ray and you" in uinput6 or "you guys" in uinput6 or "you two" in uinput6 or "the night" in uinput6 or "talk about" in uinput6:
        print("\033[31mStella\033[0m: " + random.choice(stella_messages["about_conversation"]))
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      print("\033[31mStella\033[0m: Ray said his therapist Dr. Felix Rogers suggest him to not go around Lucas...")
      # therapist_contact
      print("\033[32mHint: Ask about Felix Rogers\033[0m")
      uinput7 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      if "felix" in uinput7 or "rogers" in uinput7 or "dr.felix rogers" in uinput7 or "dr. felix rogers" in uinput7 or "contact" in uinput7:
        print("\033[31mStella\033[0m: " + random.choice(stella_messages["therapist_contact"]))
      # After the conversation
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      print("\033[31mStella\033[0m: I have to go..Be careful though, you might not believe what you will find...")
      print("\033[31mStella Fredman\033[0m appears offline...")
      game_state = "Act 3"
      print("\033[32mHint: Now go back and contact Dr. Felix Rogers\033[0m")
    elif gameState == "Act 6":
      print("------CHAT WITH \033[31mSTELLA FREDMAN\033[0m------")
      # find_ray
      stella_online = True
      print("\033[32mHint: Tell Stella about Ray in danger, be quick and short!\033[0m")
      uinput1 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      print("\033[31mStella\033[0m: " + random.choice(urgent_stella_messages["find_ray"]))
      # rogers_danger
      print("\033[32mHint: Tell Stella about how Dr. Rogers is dangerous, be quick and short!\033[0m")
      uinput3 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      print("\033[31mStella\033[0m: " + random.choice(urgent_stella_messages["rogers_danger"]))
      # save_ray
      print("\033[32mHint: Tell Stella to meet at Ray's\033[0m")
      uinput3 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mStella\033[0m is typing...")
      time.sleep(2)
      print("\033[31mStella\033[0m: " + random.choice(urgent_stella_messages["save_ray"]))
      print("\033[31mStella Fredman\033[0m appears offline...")
      gameEnd = True
      
  def chatWithFelix(gameState):
    global felix_online
    global game_state
    if felix_online == False:
      print("\033[31mStella Fredman\033[0m appears offline...")
      input("Press enter to return to the home screen.")
      return "home"
    if game_state == "Act 3":
      print("------CHAT WITH \033[31mFELIX ROGERS\033[0m------")
      # detective_intro
      stella_online = True
      print("\033[31mFelix\033[0m: Hello, may I have your name?")
      print("\033[32mHint: Tell him your name\033[0m")
      uinput1 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mFelix\033[0m is typing...")
      time.sleep(2)
      if "detective" in uinput1 or "casey" in uinput1:
        print("\033[31mFelix\033[0m: " + random.choice(felix_messages["detective_intro"]))
      # about_lucas_case
      print("\033[32mHint: Now ask about Lucas's case\033[0m")
      uinput2 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mFelix\033[0m is typing...")
      time.sleep(2)
      if "lucas" in uinput2:
        print("\033[31mFelix\033[0m: " + random.choice(felix_messages["about_lucas_case"]))
      # about_ray
      print("\033[32mHint: Ask about Ray\033[0m")
      uinput3 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mFelix\033[0m is typing...")
      time.sleep(2)
      if "ray" in uinput3:
        print("\033[31mFelix\033[0m: " + random.choice(felix_messages["about_ray"]))
      # about_ray_lucas
      print("\033[32mHint: Now ask about Ray and Lucas\033[0m")
      uinput4 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mFelix\033[0m is typing...")
      time.sleep(2)
      if "lucas" in uinput4 and ("ray" in uinput4 or "him" in uinput4):
        print("\033[31mFelix\033[0m: " + random.choice(felix_messages["about_ray_lucas"]))
      # about_ray_mental
      print("\033[32mHint: Now ask about Ray's emotions\033[0m")
      uinput5 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mFelix\033[0m is typing...")
      time.sleep(2)
      if "ray" in uinput5 or "mental" in uinput5 or "emotion" in uinput5:
        print("\033[31mFelix\033[0m: " + random.choice(felix_messages["about_ray_mental"]))
      # about_ray_violence
      print("\033[32mHint: Now ask about Ray's potential violence act'\033[0m")
      uinput6 = input("You: ").lower()
      time.sleep(2)
      print("\033[31mFelix\033[0m is typing...")
      time.sleep(2)
      if "ray" in uinput6 or "violence" in uinput6 or "aggression" in uinput6 or "aggresive" in uinput6:
        print("\033[31mFelix\033[0m: " + random.choice(felix_messages["about_ray_violence"]))
      # After conversation
      time.sleep(2)
      print("\033[31mFelix\033[0m is typing...")
      time.sleep(2)
      print("\033[31mFelix\033[0m: So sorry but I have to leave you there, I have an important meeting with one of my patient. Hope I helped you even just a little")
      print("\033[31mFelix Rogers\033[0m appears offline...")
      game_state = "Act 4"
      print("\033[32mHint: Now you have the hint to the password, go back and read Lucas's journal\033[0m")
    
  print(" =========[📨 VIRTUAL PHONE MESSAGES]========")

  if len(contact_names) > 0:
    print("\033[32mYour Current Contacts\033[0m:")
    for i in range(len(contact_names)):
      print(f"{i + 1}. {contact_names[i]} ({contact_numbers[i]})")
  else:
    print("\033[32mYou don't have any contacts yet...\033[0m")
  print("\nWhat would you like to do?")
  print("1. Add a new contact")
  print("2. Start a chat with an existing contact")
  print("Type 'exit' to return to the home screen.")

  choice = input("Enter your choice(1/2/exit): ")

  if choice == '1':
    if game_state == "Act 1":
      name = input("Enter the contact's name (format: Ray Kensington): ")
      number = input("Enter the contact's number (format: 251-433-0608): ")
    elif game_state == "Act 2":
      name = input("Enter the contact's name (format: Stella Fredman): ")
      number = input("Enter the contact's number (format: 888-498-1778): ")
    elif game_state == "Act 3":
      name = input("Enter the contact's name (format: Felix Rogers): ")
      number = input("Enter the contact's number (format: 770-555-5948): ")
    elif game_state == "Act 5":
      ray_online = True
      name = input("Enter the contact's name (format: Ray Kensington): ")
      number = input("Enter the contact's number (format: 251-433-0608): ")
    elif game_state == "Act 6":
      stella_online = True
      name = input("Enter the contact's name (format: Stella Fredman): ")
      number = input("Enter the contact's number (format: 888-498-1778): ")
    if number == "" or name == "":
      print("Information incomplete")
    if contacts[name] != number:
      print("⚠️ Contact not found")
    contact_names.append(name)
    contact_numbers.append(number)
    print(f"\n✅ Contact '{name}' added.")
    input("Press enter to return to the home screen.")
    print(" =========================================")
    return "home"
  elif choice == '2':
    if game_state == "Act 1":
      search = input("Enter a name to chat with (format: Ray Kensington): ")
    elif game_state == "Act 2":
      search = input("Enter a name to chat with (format: Stella Fredman): ")
    elif game_state == "Act 3":
      search = input("Enter a name to chat with (format: Felix Rogers): ")
    elif game_state == "Act 5":
      search = input("Enter a name to chat with (format: Ray Kensington): ")
    elif game_state == "Act 6":
      search = input("Enter a name to chat with (format: Stella Fredman): ")
    
    found = False
    for i in range(len(contact_names)):
      if search.lower() == contact_names[i].lower() or search == contact_numbers[i]:
        if contact_names[i] == "Ray Kensington":
          chatWithRay(game_state)
        elif contact_names[i] == "Stella Fredman":
          chatWithStella(game_state)
        elif contact_names[i] == "Felix Rogers":
          chatWithFelix(game_state)
        found = True
        break
    if not found:
      print("\n⚠️ Contact not found.")
      input("Press enter to return to the home screen.")
      return "home"
      
def journalView():
  global game_state
  print(" =========[\N{mobile phone} LUCAS'S JOURNAL]=========")
  print("The journal seems to be covered in blood...")
  print("\033[32mPassword Hint: Lucas and Ray's favorite drink\033[0m")
  upassword = input("Please enter the password(7 letter word): ").lower()
  if "whiskey" in upassword:
    print("\033[32mCORRECT!\033[0m")
    print(" --------------------------------------------------------------\n|                                                              |")
    print("|                   PAGE 1 (4 Days Ago)                        |")
    print("|  I never believed love at first sight, until I met her...    |")
    print("|  She is so perfect and my eyes drop everytime I see her      |")
    print("|  walking around that door... and even her name, Stella, is   |")
    print("|  such an artistic and poetic name. I want to ask her out     |")
    print("|  some day, maybe soon, who knows...                          |")
    print("|                                                              |")
    print(" -------------------------------------------------------------- ")
    print(" --------------------------------------------------------------\n|                                                              |")
    print("|                   PAGE 2 (3 Days Ago)                        |")
    print("|  Ray is acting a bit weird these days... I can see him       |")
    print("|  sta ring at me from the swings in the park. He doesn't      |")
    print("|  seem that talky when we go to the club anymore, which is    |")
    print("|  just so weird... I really do hope he is ok though...        |")
    print("|                                                              |")
    print(" -------------------------------------------------------------- ")
    print(" --------------------------------------------------------------\n|                                                              |")
    print("|                   PAGE 3 (2 Days Ago)                        |")
    print("|  I confessed to Stella, and she surprisingly accepted me!    |")
    print("|  I should be happy, but then I heard that Stella already     |")
    print("|  told Ray about me and her, and Ray doesn't seem happy...    |")
    print("|  Even though we are best friends, I still feel uncomfortable |")
    print("|  about Ray's reaction. But anyways, Stella is with me now, so|")
    print("|  I cannot let anyone take her, not even Ray.                 |")
    print("|                                                              |")
    print(" -------------------------------------------------------------- ")
    print(" --------------------------------------------------------------\n|                                                              |")
    print("|                   PAGE 4 (1 Days Ago)                        |")
    print("|  I might have found the darkest secret about a person today, |")
    print("|  it is so dark and horrible, my heart dropped...             |")
    print("|  That psychologist, Dr. Felix Rogers, I swear he is insane,  |")
    print("|  when I waited around his desk to pick up Ray's med, I saw   |")
    print("|  some of his secret files he forgot to put away... and then, |")
    print("|  I saw him doing inhuman cruel psychology experiments with   |")
    print("|  his patients, eventually causing their mental states to get |")
    print("|  extremely bad, and eventually gone insane or die!!! I       |")
    print("|  confronted this monster, and he denied it... I have to tell |")
    print("|  Ray ASAP!!! I cannot let my best friend die in the hands of |")
    print("|  a devil!!!                                                  |")
    print("|                                                              |")
    print(" -------------------------------------------------------------- ")
    print(" --------------------------------------------------------------\n|                                                              |")
    print("|                   PAGE 5 (0 Days Ago)                        |")
    print("|  I saw Dr. Rogers, that monster, going to Ray's house again, |")
    print("|  I have to stop him                                          |")
    print("|                                                              |")
    print(" -------------------------------------------------------------- ")
    print("\033[32mHint: Now quick! Talk to Ray about your discovery!\033[0m")
    game_state = "Act 5"
    input("Press enter to return to the home screen.")
    return "home"
  else:
    print("\033[31mINCORRECT\033[0m")
    input("Press enter to return to the home screen.")
    return "home"
# View changer
if currentView == "home":
  currentView = homescreenView()
elif currentView == "messages":
  currentView = messageView()
elif currentView == "evidence":
  currentView = evidenceView()
else:
  print("Unrecognized option. Returning to home screen.")
  time.sleep(1)
  currentView = "home"

# While Loop for the entire game
while not gameEnd:
  if currentView == "home":
    currentView = homescreenView()
  elif currentView == "messages":
    currentView = messageView()
  elif currentView == "journal":
    currentView = journalView()
  else:
    currentView = "home"

# Grand Ending
print("==============\033[31mAT RAY's APARTMENT\033[0m================")
time.sleep(1)
print("\033[32mYou\033[0m kicks open Ray's door")
time.sleep(1)
print("\033[31mDr. Rogers\033[0m stands over Ray with a knife raised in his hand. Ray is bleeding on the ground")
time.sleep(2)
print("\033[32mYou\033[0m: FREEZE! DROP IT ")
time.sleep(2)
print("\033[31mDr. Rogers\033[0m: He is already broken! I am doing this to save MORE PEOPLE!")
time.sleep(2)
print("\033[33mStella\033[0m: RAY! Hang on! We're here!!!")
time.sleep(1.8)
print("\033[33mRay\033[0m: P-please... don't let him.")
time.sleep(2)
print("\033[32mYou\033[0m: You destroy lives for your sick and cruel games, You will pay for this *sirens sound outside and the police kicks the door as they walk in")
time.sleep(3)

# Cliff-hanger
print("Later that night, you returned home from the Rogers case. You opened your mailbox, there is \033[33ma letter\033[0m inside...")
print(" --------------------------------------------------------------\n|                                                              |")
print("|  Dear Detective Casey,                                       |")
print("|  You were quite a detective this time... Didn't think you    |")
print("|  would solve it this fast, which is so impressive!           |")
print("|                                                              |")
print("|                                                              |")
print("|  Shall we play again sometime?                               |")
print("|                                                              |")
print("|  This is fun :)                                              |")
print("|                                                              |")
print("|  Wish to see you soon                                        |")
print("|  A friend                                                    |")
print("|                                                              |")
print(" -------------------------------------------------------------- ")
print("===========================\033[34mTHE END\033[0m===========================")
