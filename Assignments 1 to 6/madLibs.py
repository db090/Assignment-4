import random

def main():
    adjective = input("Please enter an adjective (e.g., big, happy, scary): ")
    noun = input("Please enter a noun (e.g., cat, dragon, robot): ")
    verb = input("Please enter a verb (e.g., run, jump, dance): ")


    themes = [
        "One day, a(n) [adjective] [noun] decided to [verb] through the enchanted forest!",
        "The [adjective] [noun] suddenly started to [verb] at the speed of light!",
        "I saw a [adjective] [noun] trying to [verb] on a skateboard!"
    ]

   
    story = random.choice(themes)
    story = story.replace("[adjective]", adjective).replace("[noun]", noun).replace("[verb]", verb)

    print(story)

if __name__ == "__main__":
    main()

