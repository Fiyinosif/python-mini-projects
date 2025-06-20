# Modules:
import random
# Variables:
maths_correct_choice = 0
biology_correct_choice = 0
maths_count = 0
bio_count = 0 
math_result = None
bio_result = None

print()
print("Simple Quiz App")
print("""Welcome!
      Instructions : 
      1. Press 1 for Maths Quiz / to continue Maths Quiz.
      2. press 2 for Biology Quiz / to continue Biology Quiz.
      3. Pick a letter from the option A - C
      4. Press 4 to get results
      5. Press 5 to quit program
      """)

math_questions = [
    "What is 5 + 3?\n A. 6\n B. 8\n C. 10",
    "What is 9 - 4?\n A. 5\n B. 6\n C. 4",
    "What is 6 x 2?\n A. 12\n B. 8\n C. 10",
    "What is 15 ÷ 3?\n A. 5\n B. 6\n C. 4",
    "What is the square of 4?\n A. 16\n B. 8\n C. 12",
    "What is 10 % 3?\n A. 1\n B. 2\n C. 3",
    "What is 2 + 2 x 2?\n A. 8\n B. 6\n C. 4",
    "What is the value of π (pi) approximately?\n A. 2.14\n B. 3.14\n C. 4.14",
    "What is 12 - (2 + 3)?\n A. 7\n B. 10\n C. 5",
    "What is 100 ÷ 10?\n A. 10\n B. 20\n C. 5",
    "What is 7 x 5?\n A. 30\n B. 35\n C. 25",
    "What is 81 ÷ 9?\n A. 7\n B. 8\n C. 9",
    "What is 6 squared?\n A. 36\n B. 12\n C. 18",
    "What is 3³?\n A. 6\n B. 9\n C. 27",
    "What is the smallest prime number?\n A. 1\n B. 2\n C. 3",
    "What is 0 divided by any number (except 0)?\n A. 0\n B. 1\n C. Undefined",
    "What is the perimeter of a square with side length 4?\n A. 12\n B. 16\n C. 8",
    "What is the area of a rectangle 5 x 3?\n A. 8\n B. 15\n C. 12",
    "What is 1/2 + 1/4?\n A. 3/4\n B. 1/2\n C. 2/4",
    "What is 10²?\n A. 20\n B. 100\n C. 10"
]

biology_questions = [
    "What is the basic unit of life?\n A. Atom\n B. Cell\n C. Tissue",
    "What organ pumps blood throughout the body?\n A. Brain\n B. Kidney\n C. Heart",
    "What gas do plants absorb from the atmosphere?\n A. Oxygen\n B. Carbon Dioxide\n C. Nitrogen",
    "What part of the cell contains DNA?\n A. Cytoplasm\n B. Nucleus\n C. Ribosome",
    "Which organ is responsible for breathing?\n A. Lungs\n B. Liver\n C. Intestine",
    "What do we call animals that eat only plants?\n A. Carnivores\n B. Omnivores\n C. Herbivores",
    "What is the powerhouse of the cell?\n A. Mitochondria\n B. Nucleus\n C. Chloroplast",
    "Which human organ filters blood?\n A. Kidney\n B. Stomach\n C. Heart",
    "What type of blood cells fight infection?\n A. Red\n B. White\n C. Platelets",
    "What is the largest organ in the human body?\n A. Liver\n B. Skin\n C. Brain",
    "Which part of the plant makes food?\n A. Roots\n B. Leaves\n C. Stem",
    "What is the process by which plants make food?\n A. Respiration\n B. Photosynthesis\n C. Digestion",
    "Which body part helps us to hear?\n A. Nose\n B. Ears\n C. Eyes",
    "Which body system controls movement and balance?\n A. Nervous\n B. Circulatory\n C. Digestive",
    "What do you call animals that live both in water and on land?\n A. Amphibians\n B. Mammals\n C. Reptiles",
    "What is the liquid part of blood called?\n A. Platelets\n B. Plasma\n C. Lymph",
    "Which organ helps digest food using acid?\n A. Stomach\n B. Pancreas\n C. Liver",
    "What body system includes bones?\n A. Nervous system\n B. Skeletal system\n C. Muscular system",
    "How many chambers does the human heart have?\n A. 2\n B. 3\n C. 4",
    "Which sense organ helps us smell?\n A. Eyes\n B. Tongue\n C. Nose"
]

math_answers = [
    "B",  # 8
    "A",  # 5
    "A",  # 12
    "A",  # 5
    "A",  # 16
    "B",  # 1
    "B",  # 2 + (2x2) = 6
    "B",  # 3.14
    "A",  # 12 - 5 = 7
    "A",  # 10
    "B",  # 35
    "C",  # 9
    "A",  # 36
    "C",  # 27
    "B",  # 2
    "A",  # 0
    "B",  # 16
    "B",  # 15
    "A",  # 3/4
    "B"   # 100
]

biology_answers = [
    "B",  # Cell
    "C",  # Heart
    "B",  # Carbon Dioxide
    "B",  # Nucleus
    "A",  # Lungs
    "C",  # Herbivores
    "A",  # Mitochondria
    "A",  # Kidney
    "B",  # White
    "B",  # Skin
    "B",  # Leaves
    "B",  # Photosynthesis
    "B",  # Ears
    "A",  # Nervous
    "A",  # Amphibians
    "B",  # Plasma
    "A",  # Stomach
    "B",  # Skeletal system
    "C",  # 4
    "C"   # Nose
]


while True:
    try:
        response = int(input("Pick an option: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue
    print()

    match response :
        case 1 :
            maths_count+=1
            num = random.randint(0,20)
            random_maths_question = input(f"Math Quiz\n{math_questions[num]} \nAnswer:  ").capitalize() 

            if random_maths_question == math_answers[num]:
                print("Correct.")
                maths_correct_choice += 1
                print()
            else:
                print("Wrong.")   
                print()

            math_result = f"{maths_correct_choice} correct out of {maths_count} question(s)."    

        case 2 :
            bio_count+=1
            num = random.randint(0,20)
            random_biology_question = input(f"Biology Quiz\n{biology_questions[num]} \nAnswer:  ").capitalize() 

            if random_biology_question == biology_answers[num]:
                print("Correct.")
                biology_correct_choice += 1
                print()
            else:
                print("Wrong.") 
                print() 

            bio_result = f"{biology_correct_choice} correct out of {bio_count} question(s)."    

        case 4 : 
            user_option = int(input("Press 1 for Maths result.\nPress 2 for Biology result.\nOption : "))
            if user_option == 1:
                if math_result is None:
                    print("No Math result yet. Take the quiz first.\n")   
                else : 
                    print(f"For the Maths quiz , you got {math_result}\n") 
            elif user_option == 2: 
                if bio_result is None:  
                    print("No Biology result yet. Take the quiz first.\n")     
                else:
                    print(f"For the Biology quiz , you got {bio_result}\n") 
            else:
                print("Invalid option, Go back to the main menu and select valid option.\n")            

           
        case 5 :
            print("Program ended sucessfully. Goodbye!")
            break        

        case _:
            print("Please choose a valid option from 1 - 5 (Excluding 3)") 



