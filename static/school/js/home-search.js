let inputWrapper = document.getElementsByClassName("home-search")[0]
    input = document.getElementById("home-search"),
    searchResult = document.getElementById("search-result");


    inputWrapper.onclick = function(){
    if (input === document.activeElement) {
        searchResult.style.display = "block";
    } else {
        searchResult.style.display = "none";
    }};


function homeSearch() {

    let filter = input.value.toUpperCase(),
        wrapper = document.getElementById("search-result"),
        item = wrapper.children;



    for (let i = 0; i < item.length; i++) {
        let nameSchool = item[i].getElementsByClassName("school-name")[0],
            nameSchoolValue = nameSchool.textContent,
            nameCity = item[i].getElementsByClassName("school-city")[0],
            nameCityValue = nameCity.textContent,
            codeCity = item[i].getElementsByClassName("city-code")[0],
            codeCityValue = codeCity.textContent;

        if (nameSchoolValue.trim().toUpperCase().indexOf(filter) > -1 ||
            nameCityValue.trim().toUpperCase().indexOf(filter) > -1 ||
            codeCityValue.trim().toUpperCase().indexOf(filter) > -1) {
            item[i].style.display = "";
        } else {
            item[i].style.display = "none";
        }
    }
}