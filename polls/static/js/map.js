
        
        function updateAvailability(buttonElement) {
            const availability = parseInt(buttonElement.getAttribute("data-availability"));
            const totalSeats = parseInt(buttonElement.getAttribute("data-total"));
        
            if (availability < totalSeats) {
                return availability + 1;
            } else {
                return availability;
            }
        }
        
        function handleSeatButtonClick(buttonElement) {
            const availability = parseInt(buttonElement.getAttribute("data-availability"));
            const totalSeats = parseInt(buttonElement.getAttribute("data-total"));
        
            if (availability >= totalSeats) {
                if (totalSeats === 6) {
                    alert("You can only book a maximum of 6 seats in this area.");
                } else if (totalSeats === 24) {
                    alert("You can only book a maximum of 24 seats in this area.");
                }
                return;
            }
        
            showMessage('ARE YOU SURE YOU WANT TO BOOK THIS AREA?', buttonElement);
        }
        
        
        

        
        function handleYesButtonClick(buttonElement) {
            const availability = updateAvailability(buttonElement);
            buttonElement.setAttribute("data-availability", availability);
            buttonElement.textContent = `${availability}/${maxSeats}`;
            buttonElement.classList.toggle("button-red", availability === maxSeats);
            
            
            hideMessage();
        }

        
        const seatButtons = document.querySelectorAll(".seat");
        seatButtons.forEach(button => {
            button.addEventListener("click", () => handleSeatButtonClick(button));
        });
        function updateBookingInfo() {
            fetch('/get-booking-info/')  
                .then(response => response.json())
                .then(data => {
                    for (const areaId in data) {
                        const buttonElement = document.querySelector(`[data-areaid="${areaId}"]`);
                        if (buttonElement) {
                            buttonElement.setAttribute('data-availability', data[areaId]);
                            buttonElement.textContent = `${data[areaId]}/${totalSeats}`;
        
                            
                            if (data[areaId] === 6) {
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
        function showMessage(message, button) {
            var areaId = button ? button.getAttribute('data-areaid') : null;
            selectedAreaId = areaId;
            var popupMessage = document.getElementById('popupMessage');
            var popupText = document.getElementById('popupText');
            var buttonContainer = document.getElementById('buttonContainer');
            var referenceContainer = document.getElementById('referenceContainer');
            popupText.innerHTML = message;
            buttonContainer.style.display = 'block';
            referenceContainer.style.display = 'none';
            popupMessage.style.display = 'block';
        }
        function hideMessage() {
            var popupMessage = document.getElementById('popupMessage');
            popupMessage.style.display = 'none';
        }
        
        function areaButtonClick(areaId) {
            fetch('/area_button_click/?area_id=' + areaId)
                .then(response => response.json())
                .then(data => {
                    if (data.reference_number) {
                        showReferenceNumber(areaId, data.reference_number);
                        insertIntoDatabase(areaId, data.reference_number);
                    }
                })
                .catch(error => {
                    console.log('Error:', error);
                });
        }
        
        function insertIntoDatabase(areaId, referenceNumber) {
            fetch('/insert_into_database/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    area_id: areaId,
                    reference_number: referenceNumber,
                }),
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Data inserted into the database:', data);
                })
                .catch(error => {
                    console.log('Error:', error);
                });
        }
        
        function showReferenceNumber(areaId, referenceNumber) {
            var referenceContainer = document.getElementById('referenceContainer');
            var referenceText = areaId + referenceNumber.substring(2);
            referenceContainer.textContent = referenceText;
            referenceContainer.style.display = 'block';
            showMessage('WALK-IN REFERENCE #: ' + referenceText);
        }
        
        function handleYesButtonClick() {
            var referenceContainer = document.getElementById('referenceContainer');
            var referenceNumber = generateReferenceNumber(selectedAreaId);
            var areaId = referenceNumber.substring(0, 2);
        
            if (selectedAreaId === areaId) {
                var buttonContainer = document.getElementById('buttonContainer');
                buttonContainer.style.display = 'none';
                var yesButton = document.querySelector('#popupMessage .popup-button:nth-child(1)');
                var noButton = document.querySelector('#popupMessage .popup-button:nth-child(2)');
                yesButton.style.display = 'none';
                noButton.style.display = 'none';
                referenceContainer.style.display = 'block';
                referenceContainer.textContent = referenceNumber;
                showMessage('WALK-IN REFERENCE #: ' + referenceNumber);
            }
        }
        
        function generateReferenceNumber(areaId) {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '/area_button_click/?area_id=' + areaId, false);
            xhr.send();
        
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                return response.reference_number;
            } else {
                console.error('Error:', xhr.status);
                return '';
            }
        }
        
        
        
        setInterval(updateBookingInfo, 3000);
        
        window.onload = updateBookingInfo;
    