let iconPrise = test => {for (let i = 0; i<2; i++) {
    $(".icon-price").find("i").get(i).style.color = "rgba(255, 255, 255, 1)";
}};

function uncheckedInput(thisis, className, number) {
  $("input").checked = false;

  $('*').removeClass(className);
  thisis.checked = true;
  switch (number) {
    case 1: {
      thisis.parent().addClass(className);
      break;
    }
    case 2: {
      thisis.parent().find("i").addClass(className);
      break;
    }
    case 3: {
      thisis.parent().find(".icon-price").addClass("actives");
      $('input').show();
      thisis.hide();
      break;
    }
  }
  iconPrise()
}

$(".category").on('change','input[type=radio]',(function() {
    uncheckedInput($(this), "active", 1)
}));



$(".other-filter").on('change','input[type=radio]',(function() {
  if (this.id !== "price-low-up" && this.id !== "price-up-low") {
    uncheckedInput($(this), "actives", 2)
  }
}));

$("#filter-price").on('change','input[type=radio]',(function () {

  uncheckedInput($(this), "actives", 3)

  if (this.id == "price-low-up") {
    $(this).parent().find("i").get(0).style.color = "rgba(255, 255, 255, 0.6)";
  }else {
    $(this).parent().find("i").get(1).style.color = "rgba(255, 255, 255, 0.6)";
  }
}));

