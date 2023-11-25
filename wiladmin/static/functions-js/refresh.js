const a1 = document.getElementById('a1');
const a2 = document.getElementById('a2');
const a3 = document.getElementById('a3');
const a4 = document.getElementById('a4');
const a5 = document.getElementById('a5');
const a6 = document.getElementById('a6');
const a7 = document.getElementById('a7');
const a8 = document.getElementById('a8');
const a9 = document.getElementById('a9');

setInterval(() => {
    $.ajax({
        type: 'GET',
        url:'/wiladmin/updateworkspaces',
        success: function(response){
            console.log('success', response);
            a1.value=JSON.stringify(response.area_count.countA1) + "/5";
            a2.value=JSON.stringify(response.area_count.countA2) + "/5";
            a3.value=JSON.stringify(response.area_count.countA3) + "/6";
            a4.value=JSON.stringify(response.area_count.countA4) + "/6";
            a5.value=JSON.stringify(response.area_count.countA5) + "/6";
            a6.value=JSON.stringify(response.area_count.countA6) + "/6";
            a7.value=JSON.stringify(response.area_count.countA7) + "/24";
            a8.value=JSON.stringify(response.area_count.countA8) + "/5";
            a9.value=JSON.stringify(response.area_count.countA9) + "/5";
        },
        error: function(error){
            console.log('error', error);
        }
    })

}, 2000);