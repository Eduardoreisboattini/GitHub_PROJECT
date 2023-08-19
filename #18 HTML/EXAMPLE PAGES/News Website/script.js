// Get the date element
const dateElement = document.getElementById("date");

// Function to update the date
function updateDateAndCity() {
  const currentDate = new Date();
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  const formattedDate = currentDate.toLocaleDateString('en-US', options);
  
  // Replace 'Your City Name' with the actual name of your city
  const cityName = 'São José dos Campos';

  dateElement.textContent = `Today's Date in ${cityName}: ${formattedDate}`;
}

// Call the updateDateAndCity function on page load
updateDateAndCity();
