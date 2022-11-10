

function showModalError() {
    const fullUrls = window.location.href;
    const urls = fullUrls.split("/");
    const urlPage = urls[urls.length - 1];
    const indexModul = parseInt(localStorage.getItem('numberModul'));

    if (urlPage === "create_driver_app" || urlPage === "create_partnership_app" ||  urlPage === "school_page_app") {
        setTimeout(function () {
            showModal(indexModul)
        }, 10);
    }
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


function ApplicationForm() {
    const currentApplication = document.getElementById("counter-application").textContent;
    const oldApplication = parseInt(localStorage.getItem("application"));

    localStorage.setItem("application", currentApplication)

    if (oldApplication < parseInt(currentApplication)) {
        alert("Форма успішно відправлено")
        localStorage.removeItem("application")
    }
}

function PartnershipForm() {

    const currentPartnership = document.getElementById("counter-partnership").textContent;
    const oldPartnership = parseInt(localStorage.getItem("partnership"));


    localStorage.setItem("partnership", currentPartnership)


    if (oldPartnership < parseInt(currentPartnership)) {
        alert("Форма успішно відправлено")
        localStorage.removeItem("partnership")
    }

}

function Autocomplete(course_id) {
    document.getElementById('id_school_page_city').value = parseInt(document.getElementById('autocomplete_city').textContent);
    document.getElementById('id_school_page_driverschoolunit').value = parseInt(document.getElementById('autocomplete_school').textContent);
    document.getElementById('id_school_page_course').value = course_id;
}

showModalError()
ApplicationForm()
PartnershipForm()
