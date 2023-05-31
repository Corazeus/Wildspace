
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
