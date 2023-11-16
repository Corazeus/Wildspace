
        
        function updateAvailability(buttonElement) {
            const availability = parseInt(buttonElement.getAttribute("data-availability"));
            const totalSeats = parseInt(buttonElement.getAttribute("data-total"));
        
            if (availability < totalSeats) {
                return availability + 1;
            } else {
                return availability;
            }
        }

        
    
        function updateBookingInfo() {
            fetch('/get-booking-info/')
                .then(response => response.json())
                .then(data => {
                    for (const areaId in data) {
                        const buttonElement = document.querySelector(`[data-areaid="${areaId}"]`);
                        if (buttonElement) {
                            const totalSeats = parseInt(buttonElement.getAttribute("data-total"));
                            buttonElement.setAttribute('data-availability', data[areaId]);
                            buttonElement.textContent = `${data[areaId]}/${totalSeats}`;
        
                            if (data[areaId] === totalSeats) {
                                buttonElement.style.backgroundColor = 'red';
                                buttonElement.style.color = 'white';
                            } else {
                                buttonElement.style.backgroundColor = '';
                                buttonElement.style.color = '';
                            }
                        }
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
        
        setInterval(updateBookingInfo, 3000);
        window.onload = updateBookingInfo;
        
    

        
     

        
        