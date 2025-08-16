def sorting_hat():
    slytherin = 0
    hufflepuff = 0      
    ravenclaw = 0
    gryffindor = 0
    
    #Questions 1
    print("Q1: When I die, I want people to remember me as:")
    print("A. The Good")
    print("B. The Great")   
    print("C. The Wise")
    print("D. The Bold")
    answer = input("Enter your answer: ")
    if answer =="A or a":
        hufflepuff += 1
    elif answer =="B":
        slytherin += 1
    elif answer =="C":
        ravenclaw += 1
    elif answer =="D":
        gryffindor += 1
    else:
        print("Invalid Input: ")
        
    #Questions 2
    print("Do you prefer Dawn or Dusk?")
    print("A. Dawn")
    print("B. Dusk")
    answer = input("Enter your answer: ")
    if answer =="A":
        gryffindor += 1
        ravenclaw += 1
    elif answer =="B":
        hufflepuff += 1
        slytherin += 1
    else:
        print("Invalid Input: ")
    
    #Questions 3
    print("Q3: Whhich kind of instruemnt most pleases your ear?")
    print("A. The violin")
    print("B. The trumpet")
    print("C. The piano")
    print("D. The drum")
    
# Print the scores
    print("\nFinal Scores:")
    print(f"Slytherin: {slytherin}")
    print(f"Hufflepuff: {hufflepuff}")
    print(f"Ravenclaw: {ravenclaw}")
    print(f"Gryffindor: {gryffindor}")

    # Determine the house with the most points
    scores = {
        "Slytherin": slytherin,
        "Hufflepuff": hufflepuff,
        "Ravenclaw": ravenclaw,
        "Gryffindor": gryffindor
    }
    max_score = max(scores.values())
    winning_houses = [house for house, score in scores.items() if score == max_score]

    if len(winning_houses) > 1:
        print(f"\nIt's a tie between: {', '.join(winning_houses)}!")
    else:
        print(f"\nThe house with the most points is: {winning_houses[0]}!")

# Run the quiz
if __name__ == "__main__":
    sorting_hat()