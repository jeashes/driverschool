const allCategory  = document.getElementsByClassName("category")[0];
const categoryLabels = allCategory.getElementsByTagName("label");



const removeAllActive = () => {
    return [...categoryLabels].map(
        element => element.className = ""
    )
};

const chooseCategory = () => {
  [...categoryLabels].map(
      element => element.onclick = function () {
        removeAllActive();
        localStorage.setItem('chooseCategory', element.htmlFor);
        return element.className = "active"
      }
  )
}

const lastChooseCategory = () => {
    if (window.location.href.includes("filtered")) {
        [...categoryLabels].map(
            element => element.htmlFor ===
            getCategory
                ?
                element.className = "active"
                :
                element.className = ""
        )
    }
}



let iconPrise = test => { for (let i = 0; i<2; i++) {
    $(".icon-price").find("i").get(i).style.color = "rgba(255, 255, 255, 1)";
  }};

function uncheckedInput(thisis, className, number) {
    $('*').removeClass(className);
    switch (number) {
        case 1: {
            thisis.parent().find("i").addClass(className);
            break;
        }
        case 2: {
            thisis.parent().find(".icon-price").addClass("actives");
            $('input').show();
            thisis.hide();
            break;
        }
    }
    iconPrise()
}

$(".other-filter").on('change','input[type=radio]',(function() {
  if (this.id !== "price-low-up" && this.id !== "price-up-low") {
    uncheckedInput($(this), "actives", 1)
  }
}));



$("#filter-price").on('change','input[type=radio]',(function () {

  uncheckedInput($(this), "actives", 2)

  if (this.id == "price-low-up") {
    $(this).parent().find("i").get(0).style.color = "rgba(255, 255, 255, 0.6)";
  }else {
    $(this).parent().find("i").get(1).style.color = "rgba(255, 255, 255, 0.6)";
  }
}));



chooseCategory();
lastChooseCategory();
if (getCategory === null) {
    let getCategory = 'B-B1'
}
else{
    let getCategory = localStorage.getItem('chooseCategory');
}
