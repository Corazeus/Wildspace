function getUpdates(){
    fetch('area_count')
    .then(response => response.json())
    
}

setInterval(() => {
    $("#facility-map").load(" #facility-map > *");
}, 2000);