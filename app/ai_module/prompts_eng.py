
#prompt_task = """TASK: Prepare a plan for one month of the `Olympic weightlifting workout training`;"""

#promopt_persona = """PERSONA: You are a personal trainer who is preparing a plan for one month of the `Olympic weightlifting workout training`;"""

#promopt_context = f"""CONTEXT: Perform TASK based on the historical workout plans: {historical_workout};"""

_format_response = """
**Response Template for Workout Plan**

- **Week #[number]**:
    - **Day #[number]**:
        - **Workout Name**: [Workout Name or Description]
        - **Intensity**: [Intensity Level e.g. High/Moderate/Low]
        - **Reasoning**: [Brief reasoning behind the workout's purpose]
        - **Exercises**:
            - **Exercise**: [Exercise Name]
            - **Sets**: [Number of Sets]
            - **Reps**: [Number of Repetitions]
            - **Tempo**: [Tempo, e.g., 2-1-1]
            - **Rest**: [Rest Period]
            - **Muscle Group**: [Targeted Muscle Group]

Please fill in the [brackets] with the appropriate information.
"""

format_response = """
Please fill in the [brackets] with the appropriate information:
    "Week #[number]": {
        "Day #[number]": {
            "Workout Name": "[Workout Name or Description]",
            "Intensity": "[Intensity Level e.g. High/Moderate/Low]",
            "Reasoning": "[Brief reasoning behind the workout's purpose]",
            "Exercises": [
                {
                    "Exercise": "[Exercise Name]", 
                    "Sets": [Number of Sets], 
                    "Reps": [Number of Repetitions], 
                    "Tempo": "[Tempo, e.g., 2-1-1]", 
                    "Rest": "[Rest Period]", 
                    "Muscle Group": "[Targeted Muscle Group]"
                    },
            ]
        },
    },
"""



historical_workout = """
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



olympic_main_prompt = f"""
Please adhere to the following guidelines for your response:

`CONTEXT`: My past workout plans: [( {historical_workout} )].
- Purpose: Offer information on what exercises, sets, reps, and weights I have used in the past. This will guide you in providing a progressive plan.

`TASK`: Create a one-month Olympic weightlifting workout plan.
- Purpose: Design a plan that continues from past workouts, ensuring progression and avoiding plateaus.

`PERSONA`: An experienced Olympic weightlifting coach.
- Purpose:  Ensure the plan is technically sound, safe, and tailored for Olympic weightlifting progression.

`RESPONSE STRUCTURE`: Weekly breakdown of the workout plan: [( {format_response} )].
- Purpose: Provide a day-by-day plan that's easy to follow and structured.

`RESPONSE FORMAT`: Organized list format with clear subheadings for each week.
- Purpose: Make the workout schedule easy to read and track by user.
"""