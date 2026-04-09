const statusElement = document.getElementById("status");

async function loadWeather() {
  statusElement.textContent = "Loading weather data...";

  try {
    const response = await fetch("http://127.0.0.1:8000/weather");

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json();

    statusElement.innerHTML = `
      <p><strong>Location:</strong> ${data.location}</p>
      <p><strong>Current temperature:</strong> ${data.current.temperature}°C</p>
      <p><strong>Wind speed:</strong> ${data.current.wind_speed} km/h</p>
      <p><strong>Today's max:</strong> ${data.today.temperature_max}°C</p>
      <p><strong>Today's min:</strong> ${data.today.temperature_min}°C</p>
    `;
  } catch (error) {
    statusElement.textContent = "Could not load weather data";
    console.error("Failed to fetch weather data:", error);
  }
}

loadWeather();
