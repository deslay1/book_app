/* function Market(evt, market) {
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(market).style.display = "block";
  evt.currentTarget.className += " active";
  sessionStorage.setItem("activeTabId", market);
} */

function activateTab(evt, tab) {
  //document.getElementById(tab).style.display = "block";
  console.log(tab);
  evt.currentTarget.className += " active";
  sessionStorage.setItem("activeTabId", tab);
}

var activeTabId = sessionStorage.getItem("activeTabId");
if (activeTabId == "buy") {
  document.getElementById("buy").style.color = "black";
  document.getElementById("buy").style.backgroundColor = "white";
} else {
  document.getElementById("sell").style.color = "black";
  document.getElementById("sell").style.backgroundColor = "white";
}
