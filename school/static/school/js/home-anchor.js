let abc_wrapper = document.getElementsByClassName("letters-block__content")[0],
    lettersWrapper = document.getElementsByClassName("letters-block")[0];


    function clicOnkButton (item) {
        let click_event = new CustomEvent('click'),
            findTitle = document.getElementsByClassName("find-title");

        setTimeout(findTitle[1].dispatchEvent(click_event), 100);
        setTimeout(lettersWrapper.children[item].dispatchEvent(click_event), 1000);
    }

    for (let i=0; i < abc_wrapper.children.length; i++) {
        abc_wrapper.children[i].onclick = function () {
            scrollTo(0,  1340);
            clicOnkButton(i);
        }
    }
