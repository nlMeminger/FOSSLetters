var colors = {M: "#eb2f2e", A: "#f49d26",G: "#2eb150", I: "#3a509f", C: "#7e4c9b"};

$(document).ready(function(){
  /*window.addEventListener("DOMContentLoaded", function () {
    $('.tiny button').click(function(){
      $("reset_button").addEventListener("click",function(){
        $("letter_reset").submit();
      });
    });
  });*/
  $('#letter_reset').on('click', function(event){
    event.preventDefault();
    $("#magicM .letterFill").css("fill", colors.M);
    $("#magicA .letterFill").css("fill", colors.A);
    $("#magicG .letterFill").css("fill", colors.G);
    $("#magicI .letterFill").css("fill", colors.I);
    $("#magicC .letterFill").css("fill", colors.C);
    $("#letter_reset").submit();
  });
var selected = "";
$(".magicL").click(function() {
if(selected == $(this).prop("id")) {
    selected = "";
    $(".magicL .letterStroke").css("stroke", "black");
    $("#colorSelector").hide();
} else {
    selected = $(this).prop("id");
    $('#id_letter').val(selected.substr(-1))
	$(".magicL .letterStroke").css("stroke", "black");
	$("#colorSelector").show();
  var colorText = $(this).find(".letterFill").css("fill");
  $('#cp1').colorpicker({
    inline:true,
    format: "rgba",
    useAlpha: false,
  }).on('colorpickerChange colorpickerCreate', function (e) {
        colorText = e.color.toString(e.color.toRgbString);
        r = e.color.toRgb().r;
        g = e.color.toRgb().g;
        b = e.color.toRgb().b;
        $("#" + selected + " .letterFill").css("fill", colorText);
        $('#id_cur_r').val(r);
        $('#id_cur_g').val(g);
        $('#id_cur_b').val(b);
        $('#id_letter').val(selected.substr(-1));
        $("#letter_update").submit();
      });

        // potential outline TODO e.color.complement().toRgbString());
	//$("#" + selected + " .letterStroke").css("stroke", colorText);
  $(this).find(".letterStroke").css("stroke", colorText);
}
});
});

function letter_update(){
  $.ajax({
    url : "letter_update",
    type : "POST",
    data: { the_post : $('#letter_update').val()},

    success: function(json) {
      $('letter_update').val('');
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

function letter_reset(){
  $.ajax({
    url : "letter_reset",
    type : "get",
    // data: { the_reset : $('#letter_reset').val()},

    success: function(json) {
      alert(data);
      // $('letter_reset').val('');
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
