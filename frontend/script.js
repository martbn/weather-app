const statusElement = document.getElementById("status");
const cityInputElement = document.getElementById("city-input");
const loadWeatherButtonElement = document.getElementById("load-weather-button");

async function loadWeather() {
  const city = cityInputElement.value.trim();

  if (!city) {
    statusElement.textContent = "Please enter a city";
    return;
  }

  statusElement.textContent = "Loading weather data...";

  try {
    const response = await fetch(
      `${window.APP_CONFIG.apiBaseUrl}/weather?city=${encodeURIComponent(city)}`,
    );

    if (!response.ok) {
      if (response.status === 404) {
        statusElement.textContent = `City "${city}" was not found`;
        return;
      }

      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json();

    statusElement.innerHTML = `
      <p><strong>Location:</strong> ${data.location}</p>
      <p><strong>Current temperature:</strong> ${data.current.temperature}°C</p>
      <p><strong>Wind speed:</strong> ${data.current.wind_speed} km/h</p>
      <p><strong>Today's max:</strong> ${data.today.temperature_max}°C</p>
      <p><strong>Today's min:</strong> ${data.today.temperature_min}°C</p>
      <p><strong>Today's mean humidity:</strong> ${data.today.humidity_mean}%</p>
    `;
  } catch (error) {
    statusElement.textContent = "Could not load weather data";
    console.error("Failed to fetch weather data:", error);
  }
}

loadWeatherButtonElement.addEventListener("click", loadWeather);

loadWeather();
