function getSelectedOption(sel) {
  var opt;
  for ( var i = 0, len = sel.options.length; i < len; i++ ) {
      opt = sel.options[i];
      if ( opt.selected === true ) {
          break;
      }
  }
  return opt;
}

// function setCollapsible(){

//   var ele1=document.getElementById('pd1');
//   var id = getSelectedOption(ele1).value;

//   document.getElementById(id.toString()).style.display = 'block';

// }

function dtoggle1(){
  var ub1=document.getElementById('urlbox1');
  if (ub1.style.display === "block") {
    ub1.style.display = "none";
  } 
  var dd1=document.getElementById('ddone');
  if (dd1.style.display === "block") {
    dd1.style.display = "none";
  } else {
    dd1.style.display = "block";
  }
  
}

function utoggle1(){
  var dd1=document.getElementById('ddone');
  if (dd1.style.display === "block") {
    dd1.style.display = "none";
  } 
  var ub1=document.getElementById('urlbox1');
  if (ub1.style.display === "block") {
    ub1.style.display = "none";
  } else {
    ub1.style.display = "block";
  }
  
}

function dtoggle2(){
  var ub2=document.getElementById('urlbox2');
  if (ub2.style.display === "block") {
    ub2.style.display = "none";
  } 
  var dd2=document.getElementById('ddtwo');
  if (dd2.style.display === "block") {
    dd2.style.display = "none";
  } else {
    dd2.style.display = "block";
  }
  
}

function utoggle2(){
  var dd2=document.getElementById('ddtwo');
  if (dd2.style.display === "block") {
    dd2.style.display = "none";
  } 
  var ub2=document.getElementById('urlbox2');
  if (ub2.style.display === "block") {
    ub2.style.display = "none";
  } else {
    ub2.style.display = "block";
  }
  
}

function confirm1(){
  var ele1=document.getElementById('pd1');
  var ele2=document.getElementById('url1');
  var div1=document.getElementById('ddone');
    
    if(div1.style.display == "block"){
      document.getElementById('dset1').value = getSelectedOption(ele1).innerText;
    }
    else{
      document.getElementById('dset1').value = ele2.value;
    }


}

function confirm2(){
  var ele1=document.getElementById('pd2');
  var ele2=document.getElementById('url2');
  var div1=document.getElementById('ddtwo');
    
  if(div1.style.display == "block"){
    document.getElementById('dset2').value = getSelectedOption(ele1).innerText;
  }
  else{
    document.getElementById('dset2').value = ele2.value;
  }
}

function actoggle1(){
  var acc=document.getElementById('ac1');
  acc.classList.toggle("active");
  var panel = document.getElementById('d1');

  if (panel.style.maxHeight) {
    panel.style.maxHeight = null;
  } else {
    panel.style.maxHeight = panel.scrollHeight + "px";
  }

}

function actoggle2(){

  var acc=document.getElementById('ac2');
  acc.classList.toggle("active");
  var panel = document.getElementById('d2');

  if (panel.style.maxHeight) {
    panel.style.maxHeight = null;
  } else {
    panel.style.maxHeight = panel.scrollHeight + "px";
  }

}