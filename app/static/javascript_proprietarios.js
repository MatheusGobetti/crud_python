(function (win, doc) {
  "use strict";

  if (doc.querySelector(".btnDel")) {
    let btnDel = doc.querySelectorAll(".btnDel");
    for (let i = 0; i < btnDel.length; i++) {
      btnDel[i].addEventListener("click", function (event) {
        if (confirm("Deseja mesmo apagar este dado?")) {
          return true;
        } else {
          event.preventDefault();
        }
      });
    }
  }

  //Ajax do form
  if (doc.querySelector("#form_proprietarios")) {
    let form_proprietarios = doc.querySelector("#form_proprietarios");
    function sendForm(event) {
      event.preventDefault();
      let data = new FormData(form_proprietarios);
      let ajax = new XMLHttpRequest();
      let token = doc.querySelectorAll("input")[0].value;

      ajax.open("POST", form_proprietarios.action);
      ajax.setRequestHeader("X-CSRF-TOKEN", token);
      ajax.onreadystatechange = function () {
        if (ajax.status === 200 && ajax.readyState === 4) {
          let result = doc.querySelector("#result");
          result.innerHTML = "Cadastro efetivado!";
          result.classList.add("alert");
          result.classList.add("alert-success");
        }
      };
      ajax.send(data);
      form_proprietarios.reset();
    }
    form_proprietarios.addEventListener("submit", sendForm, false);
  }
})(window, document);
