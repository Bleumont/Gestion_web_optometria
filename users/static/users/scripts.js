document.addEventListener('DOMContentLoaded', (e) => {
  hamburguerMenu();
  collapseTables();
  checkLente();
});

function collapseTables() {
  let $checkHTML = document.querySelector('.content');
  if ($checkHTML) {
    const $col = document.getElementsByClassName('content');
    [].forEach.call($col, function (tab) {
      tab.style.display = 'none';
    });
    document.addEventListener('click', (e) => {
      e.stopPropagation();
      let tar = e.target;
      if (tar.matches('.collapsible')) {
        if (tar.nextElementSibling.style.display === 'block') {
          tar.nextElementSibling.style.display = 'none';
        } else {
          tar.nextElementSibling.style.display = 'block';
        }
      }
    });
  }
}

function checkLente() {
  let $checkHTML = document.querySelector('#id_es_lente');
  if ($checkHTML) {
    const $formulario = document.getElementById('camposLente'),
      $checkBox = document.getElementById('id_es_lente');
    $checkBox.setAttribute('onclick', 'checkLente()');

    if ($checkBox.checked == true) {
      $formulario.style.display = 'block';
    } else {
      $formulario.style.display = 'none';
    }
  }
}

function hamburguerMenu() {
  let $checkHTML = document.querySelector('#menu-toggle');
  if ($checkHTML) {
    document.addEventListener('click', (e) => {
      if (e.target.matches('#menu-toggle')) {
        e.preventDefault();
        document.querySelector('#wrapper').classList.toggle('toggled');
      }
    });
  }
}
