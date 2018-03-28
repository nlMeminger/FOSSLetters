$(document).ready(function(){
var selected = "";
$(".magicL").click(function() {
if(selected == $(this).prop("id")) {
    selected = "";
    $(".magicL .letterStroke").css("stroke", "black");
    $("#colorSelector").hide();
} else {
    selected = $(this).prop("id");
	$(".magicL .letterStroke").css("stroke", "black");
	$("#colorSelector").show();
  var colorText = $(this).find(".letterFill").css("fill");
  console.log(colorText);
  $('#cp1').colorpicker({format: "rgba"}).on('colorpickerChange colorpickerCreate', function (e) {
        colorText = e.color.toString(e.color.toRgbString);
        r = e.color.toRgb().r;
        g = e.color.toRgb().g;
        b = e.color.toRgb().b;
        $("#" + selected + " .letterFill").css("fill", colorText);

      });
        // potential outline TODO e.color.complement().toRgbString());
	//$("#" + selected + " .letterStroke").css("stroke", colorText);
  $(this).find(".letterStroke").css("stroke", colorText);
}
});
});

function letter_update(){
  $.ajax({
    url : "letter_update/",
    type : "POST",
    data: { the_post : $('#letter_update').val()},

    success: function(json) {
      $('letter-update').val('');
      console.log(json);
      console.log("success");
    },
    error : function(xhr,errmsg,err) {
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
  });
};
