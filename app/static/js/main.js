document.getElementById('workoutForm').addEventListener('submit', function(e) {
    e.preventDefault();  // prevent form from actually submitting

    const workoutQuery = document.querySelector("input[name='workout_query']").value;

    // Clear the workoutResponse content
    document.getElementById('workoutResponse').innerHTML = '';

    // Show spinner when starting the request
    document.getElementById('loadingSpinner').style.display = 'block';

    fetch("/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `workout_query=${workoutQuery}`
    })
    //.then(response => response.json())  // Assuming server returns JSON
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();})
    .then(data => {
        displayWorkoutData2(data);
        document.getElementById('workoutResponse').scrollIntoView({ behavior: 'smooth' });

        // Hide spinner once data is displayed
        document.getElementById('loadingSpinner').style.display = 'none';
    })
    .catch(error => {
        console.error('Error:', error);
        
        // Hide spinner if an error occurs
        document.getElementById('loadingSpinner').style.display = 'none';
        //document.getElementById('workoutResponse').innerText = 'An error occurred. Please try again later.';

    });
});


function displayWorkoutData(data) {
    const workoutResponse = document.getElementById('workoutResponse');

    for (const week in data) {
        const weekDiv = document.createElement('div');
        const weekTitle = document.createElement('h3');
        weekTitle.innerText = week;
        weekDiv.appendChild(weekTitle);

        const daysData = data[week];
        for (const day in daysData) {
            const dayDiv = document.createElement('div');
            const dayTitle = document.createElement('h4');
            dayTitle.innerText = day;
            dayDiv.appendChild(dayTitle);

            const workout = daysData[day];
            for (const key in workout) {
                if (key === "Exercises") {
                    const exercisesList = document.createElement('ul');
                    workout[key].forEach(exercise => {
                        const exerciseItem = document.createElement('li');
                        exerciseItem.innerText = exercise["Exercise"];
                        const detailsList = document.createElement('ul');
            
                        // Adjusted the loop to iterate through the exercise object's keys directly.
                        for (const detailKey in exercise) {
                            if (detailKey !== "Exercise") {  // Skip the "Exercise" key since it's already displayed.
                                const detailItem = document.createElement('li');
                                detailItem.innerText = `${detailKey}: ${exercise[detailKey]}`;
                                detailsList.appendChild(detailItem);
                            }
                        }
            
                        exerciseItem.appendChild(detailsList);
                        exercisesList.appendChild(exerciseItem);
                    });
                    dayDiv.appendChild(exercisesList);
                } else {
                    const workoutDetail = document.createElement('p');
                    workoutDetail.innerText = `${key}: ${workout[key]}`;
                    dayDiv.appendChild(workoutDetail);
                }
            }

            weekDiv.appendChild(dayDiv);
        }
        
        workoutResponse.appendChild(weekDiv);
    }
}

function displayWorkoutData2(data) {
    const workoutResponse = document.getElementById('workoutResponse');
    
    // Convert the JSON object to a readable string
    const dataString = JSON.stringify(data, null, 2); // The '2' here adds indentation for readability

    // Display the string in a preformatted text block
    workoutResponse.innerHTML = `<pre>${dataString}</pre>`;
}
