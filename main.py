import story

def main():
    story.intro()
    
    current_stage = "stage_one"
    
    while current_stage != "end":
        if current_stage == "stage_one":
            current_stage = story.stage_one()
        elif current_stage == "stage_two":
            current_stage = story.stage_two()
        elif current_stage == "stage_three":
            current_stage = story.stage_three()
        else:
            current_stage = "end"
    
    print("\nThanks for playing, adventurer!")

if __name__ == "__main__":
    main()
