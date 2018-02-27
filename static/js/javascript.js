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
	var colorArr = colorText.substr(4, colorText.length - 5).split(", ");
	var hslArr = rgb2hsl(colorArr);
	$("#sliderH").val(hslArr[0]);
	$("#sliderS").val(hslArr[1]);
	$("#sliderL").val(hslArr[2]);
	colorText = "rgb("+(255-colorArr[0])+", "+(255-colorArr[1])+", "+(255-colorArr[2])+")";
	$(this).find(".letterStroke").css("stroke", colorText);
}
});
$("#colorSelector input").change(function() {
    changeColor();
});
function changeColor() {
    var hslArr = [0, 0, 0];
	hslArr[0] = $("#sliderH").val();
	hslArr[1] = $("#sliderS").val();
	hslArr[2] = $("#sliderL").val();
	colorArr = hsl2rgb(hslArr);
	colorText = "rgb("+colorArr[0]+", "+colorArr[1]+", "+colorArr[2]+")";
	$("#" + selected + " .letterFill").css("fill", colorText);
	colorText = "rgb("+(255-colorArr[0])+", "+(255-colorArr[1])+", "+(255-colorArr[2])+")";
	$("#" + selected + " .letterStroke").css("stroke", colorText);
}
		
// Used/modified under the MIT license
// from https://github.com/JuhQ/rgb-to-hsl/blob/master/index.js
function rgb2hsl(rgbArr) {
	var r = rgbArr[0], b = rgbArr[1], g = rgbArr[2];
	var d, h, l, max, min, s;
	r /= 255;
	g /= 255;
	b /= 255;
	max = Math.max(r, g, b);
	min = Math.min(r, g, b);
	h = 0;
	s = 0;
	l = (max + min) / 2;
    if (max === min) {
	   h = s = 0;
    } else {
        d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
		switch (max) {
		  case r:
		  h = (g - b) / d + (g < b ? 6 : 0);
		  break;
		case g:
		  h = (b - r) / d + 2;
		  break;
        case b:
			h = (r - g) / d + 4;
		}
        h /= 6;
    }
	h = h * 360;
    // Using H&L in decimal percents, so skip
	//s = (s * 100);
	//l = (l * 100);
	return [h, s, l];
}
		
		// Used/modified under the ISC license (as specified in package.json)
		// from https://github.com/kayellpeee/hsl_rgb_converter/blob/master/converter.js
		// expected hue range: [0, 360)
		// expected saturation range: [0, 1]
		// expected lightness range: [0, 1]
function hsl2rgb(hslArr){
	var hue = hslArr[0], saturation = hslArr[1], lightness = hslArr[2];
    // based on algorithm from http://en.wikipedia.org/wiki/HSL_and_HSV#Converting_to_RGB
    if( hue == undefined ){
        return [0, 0, 0];
    }

    var chroma = (1 - Math.abs((2 * lightness) - 1)) * saturation;
    var huePrime = hue / 60;
    var secondComponent = chroma * (1 - Math.abs((huePrime % 2) - 1));

    huePrime = Math.floor(huePrime);
    var red;
    var green;
    var blue;

    if( huePrime === 0 ){
        red = chroma;
        green = secondComponent;
        blue = 0;
    }else if( huePrime === 1 ){
        red = secondComponent;
        green = chroma;
        blue = 0;
    }else if( huePrime === 2 ){
        red = 0;
        green = chroma;
        blue = secondComponent;
    }else if( huePrime === 3 ){
        red = 0;
        green = secondComponent;
        blue = chroma;
    }else if( huePrime === 4 ){
        red = secondComponent;
        green = 0;
        blue = chroma;
    }else if( huePrime === 5 ){
        red = chroma;
        green = 0;
        blue = secondComponent;
    }

    var lightnessAdjustment = lightness - (chroma / 2);
    red += lightnessAdjustment;
    green += lightnessAdjustment;
    blue += lightnessAdjustment;

    return [Math.round(red * 255), Math.round(green * 255), Math.round(blue * 255)];
}
});