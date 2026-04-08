const statusElement = document.getElementById("status");

async function loadBackendStatus() {
  statusElement.textContent = "Loading...";

  try {
    const response = await fetch("http://127.0.0.1:8000/health");
    const data = await response.json();

    statusElement.textContent = `Backend is ${data.status}`;
  } catch (error) {
    statusElement.textContent = "Could not connect to backend";
    console.error("Failed to fetch backend status:", error);
  }
}

loadBackendStatus();