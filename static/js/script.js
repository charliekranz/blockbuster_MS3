
var minNumber = 1;
var maxNumber = 20;

function randomNumberFromRange(min,max) {
return  Math.floor(Math.random()*(max-min+1)+min); 


}

function clickme() {
    $("#setting_name")[0].selectedIndex = randomNumberFromRange(minNumber, maxNumber);
    $("#resolution_name")[0].selectedIndex = randomNumberFromRange(minNumber, maxNumber);
    $("#plot_name")[0].selectedIndex = randomNumberFromRange(minNumber, maxNumber);
    $("#character_name")[0].selectedIndex = randomNumberFromRange(minNumber, maxNumber);

}

/* Limit Cast to 3 using code found here - http://jsfiddle.net/vVxM2/ and syntax tweaked with assistance of 
Ronan to target cast-checkbox correctly and call modal */


/*var min = 1;
$('.cast-checkbox').on('change', function(evt) {
   if($('.cast-checkbox:checked').length < min) {
       $('#minModal').modal("show")
       this.checked = false;
   }
});*/


/* Using code and adapting to show modal if no cast chosen  https://www.sitepoint.com/jquery-check-checkbox-checked/ */

var el = document.getElementById("checkcast");
if ($('input[name=cast-checkbox]').attr('checked') != true) {
    document.getElementById("form").submit();  
    }
else {
    $('#minModal').modal("show");  
    }
}


var limit = 3;
$('.cast-checkbox').on('change', function(evt) {
   if($('.cast-checkbox:checked').length > limit) {
       $('#limitModal').modal("show")
       this.checked = false;
   }
});

/* Modal from Bootstrap */

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
});

/* $(function() {
  $('#Alpha').on("submit", function() {
    if ($('input[name=cast-checkbox]').attr('checked') != false) {
	$('#minModal').modal("show");
      return false;
    } else {
      submit;
      return true;
    }
  });
}); */
