const fullUrls = window.location.href;
const urls = fullUrls.split("/");
const urlPage = urls[urls.length - 1];

let footerWrapper = document.getElementsByClassName("footer__areas")[0],
    areaWrapper = document.getElementsByClassName("areas-block")[0];

    function clickButton(item) {
        let click_event = new CustomEvent('click'),
            findTitle = document.getElementsByClassName("find-title");

        setTimeout(findTitle[0].dispatchEvent(click_event), 100);
        setTimeout(areaWrapper.children[item].dispatchEvent(click_event), 1000)
    }

    for (let i=0; i < footerWrapper.children.length; i++) {
        footerWrapper.children[i].onclick = function () {
            scrollTo(0,  1340);
            clickButton(i);
        }
    }
