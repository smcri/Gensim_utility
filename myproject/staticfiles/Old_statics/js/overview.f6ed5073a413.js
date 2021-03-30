document.querySelectorAll('.clickable').addEventListener('click', function(){
    var new_div = $('<div>START</div>').addClass('d');    
  
    new_div.insertAfter('#carousel-example-generic');  
});