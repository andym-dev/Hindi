def tenses(verb, tense, subject):
    # Assuming the input verb is in the root form without any additional conjugations
    root_verb = verb[:-3]  # Remove the "-na" suffix

    # Define conjugation rules based on tense and subject
    conjugation_rules = {
        "present": {
            "I": "Taa Hoon",
            "He": "Taa Hai",
            "She": "Tee Hai",
            "They/We/You": "Tay Hain"
        },
        "past": {
            "I": "a tha",
            "He": "a tha",
            "She": "i thi",
            "They/We/You": "e the"
        },
        "future": {
            "I": "aunga",
            "He": "aayega",
            "She": "aayegi",
            "They/We/You": "ain gay"
        },
        "present_continuous": {
            "I": "raha hun",
            "He": "raha hai",
            "She": "rahi hai",
            "They/We/You": "rahe hain"
        },
        "past_continuous": {
            "I": "raha tha",
            "He": "raha tha",
            "She": "rahi thi",
            "They/We/You": "rahe the"
        }
        # Add more tenses and subjects as needed
    }

    # Check if the provided tense and subject are in the rules
    if tense in conjugation_rules and subject in conjugation_rules[tense]:
        conjugation = conjugation_rules[tense][subject]
        return root_verb + " " + conjugation
    else:
        return "Invalid input for tense or subject"

# Example usage
print(tenses("Kha-na", "present", "I"))
print(tenses("Kha-na", "present", "He"))
print(tenses("Kha-na", "present", "She"))
print(tenses("Kha-na", "present", "They/We/You"))
