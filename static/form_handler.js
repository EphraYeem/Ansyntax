Sortable.create(module_form, {
  handle: '.glyphicon-resize-vertical',
  animation: 150
});

var gen_btn = document.getElementById("generate_button");
gen_btn.addEventListener("click", function() {
    var all_info = {};
    all_info['site_url'] = window.location.href;
    var form_attributes = document.getElementById("module_form").children;
    for (let wrapped_attribute of form_attributes) {
        attribute = wrapped_attribute.children.namedItem('actual_form_attribute');
        if (attribute instanceof HTMLSelectElement) {
            all_info[attribute.id] = attribute.value;
        }
        else if (attribute instanceof HTMLDivElement) {
            all_info[attribute.id] = attribute.innerText;
        }
        else {
            //dunno exception or something
        }
    }
    $.ajax({
        type: "POST",
        url: "/desperate_times_call_for_desperate_housewives",
        data: JSON.stringify(all_info, null, 2),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data){alert(data);},
        failure: function(errMsg) {
            alert(errMsg);
    }
    });
});
