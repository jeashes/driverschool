function getCurrentURL () {
  return window.location.href
}

const url = getCurrentURL().split("/");
const urlPage = url[url.length - 1];
const indexModul = localStorage.getItem('numberModul');
const currentApplication = document.getElementById("counter-application").textContent;
const oldApplication = parseInt(localStorage.getItem("application"));
const currentPartnership = document.getElementById("counter-partnership").textContent;
const oldPartnership = parseInt(localStorage.getItem("partnership"));


if (urlPage === "create_driver_app" || urlPage === "create_partnership_app") {
    setTimeout(function () {
        showModal(indexModul)
    }, 10);
}

function showModal (index) {
    const body = document.getElementsByTagName("body")[0];
    const modalWrapper = document.getElementsByClassName("modal-wrapper");

    modalWrapper[index].style.display = "block";
    body.style.overflow = "hidden";

    return localStorage.setItem('numberModul', index);
}

function hideModal(index) {
    const body = document.getElementsByTagName("body")[0];
    const modalWrapper = document.getElementsByClassName("modal-wrapper");
    const buttons = document.getElementsByClassName("button--close-modal")

    window.onclick = function (event) {
        if (event.target === modalWrapper[index]) {
            modalWrapper[index].style.display = "none";
            body.style.overflow = "auto";
            return localStorage.removeItem('numberModul');
        }
    }

    buttons[index].onclick = function () {
        modalWrapper[index].style.display = "none";
        body.style.overflow = "auto";
        return localStorage.removeItem('numberModul');
    }

}

localStorage.setItem("application", currentApplication)
localStorage.setItem("partnership", currentPartnership)

if (oldApplication < parseInt(currentApplication)) {
    alert("Форма успішно відправлено")
    localStorage.removeItem("application")

}

if (oldPartnership < parseInt(currentPartnership)) {
    alert("Форма успішно відправлено")
    localStorage.removeItem("partnership")
}