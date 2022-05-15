let radios = document.forms["choices"].elements["choice_id"];
const btn = document.querySelector('#btn');
for(let i = 0, max = radios.length; i < max; i++) {
    radios[i].onclick = function() {
        btn.disabled = false;
    }
}
