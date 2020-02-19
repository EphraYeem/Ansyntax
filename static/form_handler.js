var gen_btn = document.getElementById("generate_button");
gen_btn.addEventListener("click", function() {
    var elements = document.getElementById("module_form").elements;
    for (var i = 0, element; element = elements[i++];) {
        //checks and whatnot
    }
    var elms = document.getElementsByClassName("form_attribute")
    for (var j = 0, elm; elm = elms[j++];) {
        alert(elm.innerText)
    }
});
