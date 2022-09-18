let inputWrapper = document.getElementsByClassName("search__form")[0],
    input = document.getElementById("search__field"),
    searchResult = document.getElementById("search__result"),
    delayInMilliseconds = 200, // 0.20 second
    abcBlock = document.getElementsByClassName("search__letters")[0],
    abcWrapper = document.getElementsByClassName("search__letters-block")[0];



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
        wrapper = document.getElementById("search__result"),
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