activateGroup = (evt, name) => {
  evt.currentTarget.value = name;
};

/* // save active tab to storage
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
} */

function viewComments(name) {
  let commentsDiv = document.getElementById(name);
  if (commentsDiv) {
    if (commentsDiv.style.display == "block") {
      commentsDiv.style.display = "none";
    } else {
      commentsDiv.style.display = "block";
    }
  }
}

function focusButton(name) {
  document.getElementById(name).focus();
  console.log(name);
  console.log(document.getElementById(name));
}

viewReplyForm = (comment_id) => {
  let reply_form = document.getElementById("comment-reply-form-" + comment_id);
  if (reply_form.style.display == "flex") {
    reply_form.style.display = "none";
    reply_form.blur();
  } else {
    reply_form.style.display = "flex";
    reply_form.focus();
  }
};

$(".reply-button").click(function () {
  console.log("reached");
  const form_number = $(this).val();
  $("#reply-form-" + form_number).submit(function (e) {
    e.preventDefault();
    // serialize the data for sending the form data.
    var serializedData = $(this).serialize();
    // make POST ajax call
    $.ajax({
      type: "POST",
      url: $(this).attr("data-href"),
      data: serializedData,
      success: function (response) {
        // on successfull creating object
        // 1. clear the form.
        $("#reply-form-" + form_number).trigger("reset");

        //Can onyl reply once!
        $(".comment-reply-" + form_number).css("display", "none");
        console.log($(".comment-reply-" + form_number));

        const instance = JSON.parse(response["instance"]);
        const reply = instance[0]["fields"];
        const user = instance[1]["fields"];
        const profile = instance[2]["fields"];
        const reply_model = instance[3];

        $("#replies-" + form_number).append(
          `<div id="reply-active" class="reply-container-active ml-4 mr-5">
          <div class="reply-subdir">
            <i class="material-icons">subdirectory_arrow_right</i>
          </div>
        <div class="card mt-2 w-100 border border-primary" style="flex-grow: 8;">
          <div class="card-header">
            <div class="justify-content-between row">
              <div>
                  <div class="profile-image-container">
                    <img class="rounded-circle img-fluid w-75" src="${profile.image}" />
                   </div>
                <div style="display:flex;align-items: center;">
                  <a href="/profile/">${user.username}</a>
                  <small class="ml-2">just now</small>
                </div>
              </div>
              <div class="">
                <!-- <a id="update-comment-button" href="reply/${reply_model.pk}/update">Update</a> -->
                <a id="delete-comment-button" style="color:red"
                  href="reply/${reply_model.pk}/delete">Delete</a>
              </div>
            </div>
          </div>
          <div class="ml-2 card-body">
            <p>${reply.content}</p>
          </div>
        </div>
        </div>`
        );
      },
      error: function (response) {
        // alert the error if any error occured
        alert(response["responseJSON"]["error"]);
      },
    });
  });
});

if (document.getElementsByClassName("reply-1")) {
  $(".reply-1").css("display", "flex");
  if (document.getElementsByClassName("reply-2")) {
    $(".reply-2").css("display", "flex");
  }
}
moreReplies = (end, comment_id) => {
  const moreReplyButton = $(".more-replies-" + comment_id);
  const buttonValue = parseInt(moreReplyButton.val());
  for (i = buttonValue; i < end + buttonValue; i++) {
    if (document.getElementsByClassName(`reply-${i}-${comment_id}`).length > 0) {
      $(`.reply-${i}-${comment_id}`).css("display", "flex");
      if (document.getElementsByClassName(`reply-${i + 1}-${comment_id}`).length === 0) {
        $(".more-replies-" + comment_id).css("display", "none");
      }
    } else {
      $(".more-replies-" + comment_id).css("display", "none");
    }
  }
  $(".more-replies-" + comment_id).val(buttonValue + Number(end));
  $(".more-replies-" + comment_id).blur();
};

// Clear filters in home
function clearFilters() {
  $("input[name=condition]").attr("checked", false);
  $("input[name=price_order]").attr("checked", false);
  location.href = "/";
}

// jQuery in post_form

//For updating the post
if (document.getElementById("div_id_image") && $("#div_id_image").find("a").length > 0) {
  $("#image2").removeClass("image-hide");
  if ($("#div_id_image2").find("a").length > 0) {
    $("#image3").removeClass("image-hide");
  }
}

// General conditions
$("#id_image").change(function () {
  $("#image2").removeClass("image-hide");
});

$("#id_image2").change(function () {
  $("#image3").removeClass("image-hide");
});

$("#thisForm").ajaxForm({
  url: "myscript.php", // or whatever
  dataType: "json",
  success: function (response) {
    alert("The server says: " + response);
  },
});
