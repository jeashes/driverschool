
    function showModal (i) {

        let modalWrapper = $(".modal-wrapper"),
            modalLength = modalWrapper.length;

        $("body")[0].style.overflow = "hidden";

        for (let k = 0; k<modalLength; k++ ) {
            modalWrapper[k].style.display = "none";
        }

        i === 0 ? modalWrapper[0].style.display = "block" : modalWrapper[1].style.display = "block";
    }


    function hideModal(modalWrapper, event ,i) {

            if (event.target === modalWrapper[i]) {
                modalWrapper[i].style.display = "none";
            }

            $("body")[0].style.overflow = "auto";
    }


    function clickOnButton(buttons) {
        let modalWrapper = $(".modal-wrapper"),
            modalButton = $(".button--modal");

        for (let i = 0; i < 2; i++) {
            if (buttons[i] === modalButton[i]) {
                buttons[i].onclick = function () {
                    showModal(i);
                                modalWrapper[i].onclick = function(event) {
                hideModal(modalWrapper, event, i);
            }
                }
            } else {
                for (let k = 0; k < buttons[0].children.length; k++) {
                buttons[0].children[k].onclick = function () {
                    showModal(k);
                                modalWrapper[k].onclick = function(event) {
                hideModal(modalWrapper, event, k);
            }
                }

                }

            }


        }
    }

    clickOnButton($(".button--modal"));

