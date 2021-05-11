
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


/* check that at lease one checkbox is checked before submitting form */
/* Ronan helped me by finding the e.prevent method and suggested naming form to avoid issue later */
/* e.prevent found at ttps://stackoverflow.com/questions/35552813/call-function-with-bootstrap-submit-button */

$(".story-form").on('submit', function(e) {
    if($('.cast-checkbox:checked').length < 1){
        //show modal and stop standard submit
        e.preventDefault();
        $('#minModal').modal("show");
    }
});

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



var limit = 3;
$('.cast-checkbox').on('change', function(evt) {
   if($('.cast-checkbox:checked').length > limit) {
       $('#limitModal').modal("show");
       this.checked = false;
   }
});

/* Modal from Bootstrap */

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus');
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
