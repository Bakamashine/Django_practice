const buttons = document.querySelectorAll("#menu-button");
const modalWindows = document.querySelectorAll('#menu-modalwindow');
console.log(buttons);



/**
 * 
 * @param {boolean} visible 
 * @param {HTMLElement} win
 */
function open_or_close(visible, win) {
    visible
    ? win.classList.replace("show", 'hidden')
    : win.classList.replace("hidden", 'show')
}

function all_close(modal) {
    modalWindows.forEach(elem => {
        modal != elem &&
            elem.classList.remove("show")
            elem.classList.add("hidden");
    });
}

buttons.forEach(button => {
    const modalWindow = button.querySelector('#menu-modalwindow');

    button.addEventListener("click", () => {
        
        all_close(modalWindow);
        let isVisible = modalWindow.classList.contains("show");
        console.log("isVisible: " , isVisible)
        open_or_close(isVisible, modalWindow);
        
    });
});