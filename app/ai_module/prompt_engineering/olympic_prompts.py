prompt_task = """TASK: Prepare a plan for one month of the `Olympic weightlifting workout training`;"""

promopt_persona = """PERSONA: You are a personal trainer who is preparing a plan for one month of the `Olympic weightlifting workout training`;"""

promopt_context = f"""CONTEXT: Perform TASK based on the historical workout plans: {historical_workout_plans};"""

format_response = """
                data = {
                    "Week": [Week number],
                    "Day": [Day number],
                    "Workout": [Workout name],
                    "Exercise": [Exercise name],
                    "Sets": [Number of sets],
                    "Reps": [Number of repetitions],
                    "Tempo": [Tempo],
                    "Rest": [Rest time between sets],
                    "Notes": [Notes],
                    "Exercise Type": [Type of exercise],
                    "Exercise Muscle Group": [Muscle group],
                    "Exercise Equipment": [Equipment],
                    "Exercise Difficulty": [Difficulty],
                    "Exercise Intensity": [Intensity],
                    "Reasoning": [Reasoning for the exercise],"
                    }
"""


format_example = """
workout_plan = {
    "Week 1": {
        "Day 1": {
            "Workout Name": "Strength & Conditioning - Push Dominant",
            "Intensity": "High",
            "Reasoning": "Develop push movements and full-body power",
            "Exercises": [
                {
                    "Exercise": "Db thrusters", 
                    "Sets": 3, 
                    "Reps": 10, 
                    "Tempo": "2-1-1", 
                    "Rest": "60 seconds", 
                    "Muscle Group": "Full Body"
                    },
                {
                    "Exercise": "Down up", 
                    "Sets": 3, 
                    "Reps": 10, 
                    "Tempo": "1-1-1", 
                    "Rest": "60 seconds", 
                    "Muscle Group": "Full Body"
                    },
                {
                    "Exercise": "High bar pause squat", 
                    "Sets": 4, 
                    "Reps": 5, 
                    "Tempo": "3-1-1", 
                    "Rest": "90 seconds", 
                    "Muscle Group": "Legs"
                    },
                {
                    "Exercise": "Db thruster", 
                    "Sets": 5, 
                    "Reps": 10, 
                    "Tempo": "2-1-1", 
                    "Rest": "60 seconds", 
                    "Muscle Group": "Full Body"
                    },
            ]
        },
        "Day 2": {
            "Workout Name": "Strength & Conditioning - Pull Dominant",
            "Intensity": "Moderate",
            "Reasoning": "Develop pull movements and stability",
            "Exercises": [
                {
                    "Exercise": "Muscle snatch", 
                    "Sets": 5, 
                    "Reps": 5, 
                    "Tempo": "X-1-2", 
                    "Rest": "90 seconds", 
                    "Muscle Group": "Full Body"
                    },
                {
                    "Exercise": "Barbell row", 
                    "Sets": 4, 
                    "Reps": 8, 
                    "Tempo": "2-1-2", 
                    "Rest": "90 seconds", 
                    "Muscle Group": "Back"
                    },
                {
                    "Exercise": "Pull up", 
                    "Sets": 5, 
                    "Reps": 5, 
                    "Tempo": "2-0-2", 
                    "Rest": "90 seconds", 
                    "Muscle Group": "Back"
                    },
                {
                    "Exercise": "Snatch grip RDL", 
                    "Sets": 3, 
                    "Reps": 8, 
                    "Tempo": "3-1-1", 
                    "Rest": "90 seconds", 
                    "Muscle Group": "Back & Hamstrings"
                    },
            ]
        },
        "Day 3": {
            "Workout Name": "Full Body & Conditioning",
            "Intensity": "High",
            "Reasoning": "Overall strength, power, and endurance",
            "Exercises": [
                {
                    "Exercise": "Power clean + push jerk", 
                    "Sets": 4, 
                    "Reps": "5+5", 
                    "Tempo": "X-1-X", 
                    "Rest": "2 minutes", 
                    "Muscle Group": "Full Body"
                    },
                {
                    "Exercise": "OHS", 
                    "Sets": 5, 
                    "Reps": 5, 
                    "Tempo": "3-1-1", 
                    "Rest": "90 seconds", 
                    "Muscle Group": "Legs"
                    },
                {
                    "Exercise": "Push up", 
                    "Sets": 5, 
                    "Reps": 10, 
                    "Tempo": "2-0-2", 
                    "Rest": "60 seconds", 
                    "Muscle Group": "Chest"
                    },
                {
                    "Exercise": "Burpees", 
                    "Sets": 1, 
                    "Reps": 30, 
                    "Tempo": "1-0-1", 
                    "Rest": "NA", 
                    "Muscle Group": "Full Body"
                    },
            ]
        }
    },
    # For the next weeks use progression and slightly increase the weight or reps as weeks go by. 
    "Week 2": {...},
    "Week 3": {...},
    "Week 4": {...}
}

"""
