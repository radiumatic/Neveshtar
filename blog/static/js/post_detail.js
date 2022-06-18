function ready(fn) {
    if (document.readyState != 'loading'){
        fn();
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
}
var add_func = function() {
    request = new XMLHttpRequest();
    request.open("GET", "/api/add_like/" + post_id, true);
    request.withCredentials = true;
    var done_function = function() {
        if (request.readyState == 4 && request.status == 200) {
            like_count = document.getElementById("like-count");
            //add one to likes count
            like_count.innerHTML = parseInt(like_count.innerHTML) + 1;
            like_icon.src = "/static/icons/like-fill.svg";
            like_icon.id = "remove-like";
            like_icon.removeEventListener("click", add_func);
            like_icon.addEventListener("click", remove_func);
        }
    }
    request.onerror = function() {
        if(request.status == 456){
        }
        else{
            console.log(request.responseText)
            json_reponse = JSON.parse(request.responseText);
            alert("ارور باوکم:\n" + json_reponse.message);
        }
    }
    request.onreadystatechange = done_function;
    request.send();
    //on error
    
}
var remove_func = function() {
    request = new XMLHttpRequest();
    request.open("GET", "/api/remove_like/" + post_id, true);
    request.withCredentials = true;
    var done_function = function() {
        if (request.readyState == 4 && request.status == 200) {
            console.log(request.responseText);
            like_count = document.getElementById("like-count");
            //remove one like from the count
            like_count.innerHTML = parseInt(like_count.innerHTML) - 1;
            like_icon.src = "/static/icons/like-outline.svg";
            like_icon.id = "add-like";
            like_icon.removeEventListener("click", remove_func);
            like_icon.addEventListener("click", add_func);

        }
    }
    //on error
    request.onerror = function() {
        if (request.status = 456){    
            console.log(request.responseText) 
        }
        else{
            console.log(request.responseText)
            json_reponse = JSON.parse(request.responseText);
            alert("ارور باوکم:\n" + json_reponse.message);
        }
    }
    request.onreadystatechange = done_function;
    request.send();
    
}


ready(function() {
    like_icon=document.getElementById("add-like")
    if (like_icon === null) {
        like_icon = document.getElementById("remove-like")
        like_icon.addEventListener("click", remove_func);
    }else{
        like_icon = document.getElementById("add-like")
        like_icon.addEventListener("click", add_func);
        }
});
