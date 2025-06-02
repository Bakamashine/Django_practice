const menuButtons = document.querySelectorAll(".menu-buttons")
console.log("menuButtons: ", menuButtons)

menuButtons.forEach(elem => {
	const button = elem.querySelector(".click")
	const modalWindow = elem.querySelector(".modal_window")
	
    button.addEventListener("click", () => {
      menuButtons.forEach((otherElem) => {
        const otherModal = otherElem.querySelector(".modal_window");
        if (otherModal !== modalWindow) {
		console.log("otherModal: ", otherModal)
	otherModal.classList.replace("show", "hidden")
//          otherModal.classList.remove("show");
//          otherModal.classList.add("hidden");
        }
      });
      const isActive = modalWindow.classList.contains("show");
      if (isActive) {
        modalWindow.classList.replace("show", "hidden");
      } else {
        modalWindow.classList.replace("hidden", "show");
      }
    });
  });
  document.addEventListener("click", (event) => {
    let clickedInsideModal = false;
    menuButtons.forEach((elem) => {
      if (elem.contains(event.target)) {
        clickedInsideModal = true;
      }
    });
    if (!clickedInsideModal) {
      menuButtons.forEach((elem) => {
        const modal = elem.querySelector(".modal_window");
        modal.classList.remove("show");
        modal.classList.add("hidden");
      });
    }
  });
 
