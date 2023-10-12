// user_dashboard_update_script.js

function updateBookingInfo() {
    // Make an AJAX request to get the updated data
    fetch('/get-booking-info/')  // Adjust the URL if needed
        .then(response => response.json())
        .then(data => {
            // Update the buttons with real-time data
            updateButtons(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function updateButtons(data) {
    for (const areaId in data) {
        const buttonElement = document.querySelector(`[data-areaid="${areaId}"]`);
        if (buttonElement) {
            buttonElement.textContent = `${data[areaId]}/5`;
        }
    }
}

// Update booking information periodically (every 5 seconds in this example)
setInterval(updateBookingInfo, 5000);

window.onload = updateBookingInfo;
