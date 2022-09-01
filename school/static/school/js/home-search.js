let inputWrapper = document.getElementsByClassName("home-search")[0],
    input = document.getElementById("home-search"),
    searchResult = document.getElementById("search-result"),
    delayInMilliseconds = 110, // 0.11 second
    abcBlock = document.getElementsByClassName("abc-icon-wrapper")[0],
    abcWrapper = document.getElementsByClassName("abc-block-wrapper")[0];



abcBlock.onclick = function(){
    console.table("work");
    abcWrapper.classList.toggle("active-abc");
}


inputWrapper.onclick = function(){
    if (input === document.activeElement) {
        searchResult.classList.add("active-result");
    }};

input.onblur = function () {
    setTimeout(function() {
        searchResult.classList.remove("active-result");
    }, delayInMilliseconds);
};


function homeSearch() {

    let filter = input.value.toLowerCase(),
        wrapper = document.getElementById("search-result"),
        item = wrapper.children;

    for (let i = 0; i < item.length; i++) {
        let school = item[i].getElementsByClassName("school-info")[0],
            schoolName = school.children[0].textContent.toLowerCase(),
            schoolCityName = school.children[1].textContent.split(" - ")[0].toLowerCase(),
            schoolCityCode = school.children[1].textContent.match(/\d/g).join("");

        if (schoolName.includes(filter) || schoolCityName.includes(filter) || schoolCityCode.includes(filter)) {
            item[i].style.display = "flex";
        } else {
            item[i].style.display = "none";
        }
    }
}