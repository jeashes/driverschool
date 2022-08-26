$(".category").on('change','input[type=radio]',(function() {
  $("input").checked = false;
  $('*').removeClass("actives").removeClass("active");
  $(this).checked = true;
  $(this).parent().addClass('active');
  $(".icon-price").find("i").get(0).style.color = "rgba(255, 255, 255, 1)";
  $(".icon-price").find("i").get(1).style.color = "rgba(255, 255, 255, 1)";
}));



$(".other-filter").on('change','input[type=radio]',(function() {
  console.log(this.id);
  if (this.id != "price-low-up" ) {
    if (this.id != "price-up-low") {
            console.table(this.id);

    $("input").checked = false;
    $('*').removeClass("actives").removeClass("active");
    $(this).checked = true;
    $(this).parent().find('i').addClass('actives');
    $(".icon-price").find("i").get(0).style.color = "rgba(255, 255, 255, 1)";
    $(".icon-price").find("i").get(1).style.color = "rgba(255, 255, 255, 1)";
    }
  }
}));

$("#filter-price").on('change','input[type=radio]',(function () {
    console.log(this.id);

  $("input").checked = false;
  $('*').removeClass("actives").removeClass("active");
  $(this).checked = true;
  $(this).parent().find(".icon-price").addClass("actives");
  $('input').show();
  $(this).hide();
  $(this).parent().find("i").get(0).style.color = "rgba(255, 255, 255, 1)";
  $(this).parent().find("i").get(1).style.color = "rgba(255, 255, 255, 1)";

  if (this.id == "price-low-up") {
    $(this).parent().find("i").get(0).style.color = "rgba(255, 255, 255, 0.6)";
  }else {
        $(this).parent().find("i").get(1).style.color = "rgba(255, 255, 255, 0.6)";
  }
}));

