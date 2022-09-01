let iconFirst =  $(".icon-price").find("i").get(0),
    iconSecond =  $(".icon-price").find("i").get(1);

function checkFilters( variable, thisIs) {
    $("input").removeAttr('checked');
    $('*').removeClass("actives").removeClass("active");
    thisIs.checked();
    thisIs.parents().find($('i')).addClass(variable);
    iconFirst.style.color = "rgba(255, 255, 255, 1)";
    iconSecond.style.color = "rgba(255, 255, 255, 1)";
}

$(".category").on('change','input[type=radio]',(function() {
    checkFilters("active", this);
}));

$(".other-filter").on('change','input[type=radio]',(function() {
  if (this.id !== "price-low-up" ) {
    if (this.id !== "price-up-low") {
      checkFilters("actives", this);
    }
  }
}));

$("#filter-price").on('change','input[type=radio]',(function () {
  checkFilters("actives", this);
  $('input').show();
  $(this).hide();

  if (this.id === "price-low-up") {
    iconFirst.style.color = "rgba(255, 255, 255, 0.6)";
  }else {
    iconSecond.style.color = "rgba(255, 255, 255, 0.6)";
  }
}));

