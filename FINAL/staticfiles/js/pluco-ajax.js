$(document).ready(function() {

$("#aumentar").click(function() {
      var fontSize = parseInt($("body").css("font-size"));
      fontSize = fontSize + 1 + "px";
      $("body").css({'font-size':fontSize});
});


$("#btnOuch").click( function() {
alert ("Ouch! That hurt.");
});

/**Fuentes y tamaño letras**/
var tamOriginal = $(html).css(font-size);
alert(tamOriginal);
$(.reiFuente).click(function(){
  $(html).css(font-size, tamOriginal);
});

// Incrementar el tamaño de la fuente
$(.aumFuente).click(function(){
  var tamActual = $(html).css(font-size);
  alert(tamActual);
  var tamActualNum = parseFloat(tamActual, 10);
  var nuevaFuente = tamActualNum*1.2;
  $(html).css(font-size, nuevaFuente);
  return false;
});

// Disminuir el tamaño de la fuente
$(.disFuente).click(function(){
  var tamActual = $(html).css(font-size);
  var tamActualNum = parseFloat(tamActual , 10);
  var nuevaFuente = tamActualNum*0.8;
  $(html).css(font-size, nuevaFuente);
  return false;
});

}); //Fin document ready
