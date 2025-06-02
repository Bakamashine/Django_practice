const menu_button = document.querySelectorAll("#menu-button");
menu_button.forEach((elem) => {
  /**
   * @type {HTMLButtonElement}
   */
  let button = elem.children["click"];

  /**
   * @type {HTMLElement}
   */
  let modal_window = elem.children["modal_window"];

  console.log("button: ", button);
  console.log("modal_window", modal_window);
  console.log("elem_children", elem.children);

  button.addEventListener("click", () => {
    let isActive = modal_window.classList.contains("show");
    isActive
      ? modal_window.classList.replace("show", "hidden")
      : modal_window.classList.replace("hidden", "show");
  });
});
