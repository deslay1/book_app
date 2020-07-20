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

// save active tab to storage
function activateTab(evt, tab) {
  //document.getElementById(tab).style.display = "block";
  evt.currentTarget.className += " active";
  sessionStorage.setItem("activeTabId", tab);
}

// read from storage and style correct tab
const activeTabId = sessionStorage.getItem("activeTabId");
let buyTab = document.getElementById("buy");
let sellTab = document.getElementById("sell");
if (activeTabId == "buy" && buyTab) {
  document.getElementById("buy").style.color = "black";
  document.getElementById("buy").style.backgroundColor = "white";
}
if (activeTabId == "sell" && sellTab) {
  document.getElementById("sell").style.color = "black";
  document.getElementById("sell").style.backgroundColor = "white";
}

function viewComments(name) {
  let commentsDiv = document.getElementById(name);
  if (commentsDiv) {
    if (commentsDiv.style.visibility == "visible") {
      commentsDiv.style.visibility = "hidden";
    } else {
      commentsDiv.style.visibility = "visible";
    }
  }
}

// Clear filters in home
function clearFilters() {
  $("input[name=condition]").attr("checked", false);
  $("input[name=price_order]").attr("checked", false);
  location.href = "/";
}

// jQuery in post_form

//For updating the post
if (document.getElementById("id_image") && document.getElementById("id_image").value == "") {
  console.log("hi");
  $("#image2").removeClass("image-hide");
  if (document.getElementById("id_image2").value != "") {
    $("#image3").removeClass("image-hide");
  }
}
// General conditions
$("#id_image").change(function () {
  console.log("hi");
  $("#image2").removeClass("image-hide");
});

$("#id_image2").change(function () {
  $("#image3").removeClass("image-hide");
});
