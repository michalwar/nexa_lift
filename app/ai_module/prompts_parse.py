def parse_workout_response(response):
    # Split the response into weeks
    weeks = response.split("- **Week")

    parsed_workout = {}

    for week in weeks[1:]:
        days = week.split("- **Day")
        week_number = days[0].split(":")[0].strip()
        parsed_workout[week_number] = {}

        for day in days[1:]:
            exercises = day.split("- **Exercise")
            day_details = exercises[0].split("- **")
            day_number = day_details[0].split(":")[0].strip()
            parsed_workout[week_number][day_number] = {
                detail.split(":")[0].strip(): detail.split(":")[1].strip() for detail in day_details[1:]
            }

            parsed_workout[week_number][day_number]["exercises"] = []
            for exercise in exercises[1:]:
                exercise_details = exercise.split("- **")
                exercise_data = {
                    detail.split(":")[0].strip(): detail.split(":")[1].strip() for detail in exercise_details[1:]
                }
                parsed_workout[week_number][day_number]["exercises"].append(exercise_data)

    return parsed_workout
