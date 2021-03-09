function showresult() {
  window.open("result.html", "_blank");
}

function chose(){
  var ele=document.getElementById('dsName');
  var box=document.getElementById('urlbox1');
  box.style.display = 'none';
  document.getElementById('choosen').value = ele.innerText;
  
}

function chose2(){
  var ele=document.getElementById('dsName2');
  var box=document.getElementById('urlbox2');
  box.style.display = 'none';
  document.getElementById('choosen2').value = ele.innerText;
}

function confirm1(){
  var ele=document.getElementById('dsName');
  document.getElementById('dset1').value = ele.innerText;
}

function confirm2(){
  var ele=document.getElementById('dsName2');
  document.getElementById('dset2').value = ele.innerText;
}
