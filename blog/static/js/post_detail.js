/**
 * Copyright (c) 2022 radiumatic
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 * the Software, and to permit persons to whom the Software is furnished to do so,
 * subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */



function ready(fn) {
    if (document.readyState != 'loading'){
        fn();
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
}
//equal to jquery method of sending a form 
function sendForm(form) {
    var xhr = new XMLHttpRequest();
    xhr.open(form.method, form.action, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            form = document.getElementById("comment-form");
            form.reset();
            json_result = JSON.parse(xhr.responseText);
            var comments = document.getElementsByClassName("comments")[0];
            var comment = document.createElement("div");
            comment.className = "comment";
            try{
                comments.insertBefore(comment, comments.firstChild);
            }
            catch{
                comments.appendChild(comment)
            }
            var username = document.createElement("p");
            username.className = "comments-text";
            username.innerText = json_result.comment.username;
            comment.appendChild(username);
            var comment_text = document.createElement("p");
            comment_text.className = "comments-text";
            comment_text.innerText = json_result.comment.comment;
            comment.appendChild(comment_text);
            var comment_date = document.createElement("p");
            comment_date.className = "comments-text date";
            comment_date.innerText = json_result.comment.created_date;
            comment.appendChild(comment_date);

        }
    };
    xhr.onerror = function () {
        //convert reponse to json
        var json = JSON.parse(xhr.responseText);
        //display error message
        alert(json.message);
    }
    var data = '';
    for (var i = 0; i < form.elements.length; i++) {
        var field = form.elements[i];
        if (field.name) {
            data += field.name + '=' + field.value + '&';   
        }
    }
    xhr.send(data);
}
var add_func = function() {
    request = new XMLHttpRequest();
    request.open("GET", "/api/add_like/" + post_id, true);
    request.withCredentials = true;
    request.onerror = function() {
        console.log(request.responseText)
        json_reponse = JSON.parse(request.responseText);
        alert(json_reponse.message);
    }
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
        else if (request.readyState == 4 && request.status == 400) {
            alert("shit")
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
    //on error
    request.on = function() {
        console.log(request.responseText)
        json_reponse = JSON.parse(request.responseText);
        alert(json_reponse.message);
    }
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
        else if (request.status == 400) {
            alert("shit")   
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
    comment_send = document.getElementById("comment-send");
    if (comment_send !== null) {
        comment_send.addEventListener("click", function() {
            form = document.getElementById("comment-form");
            sendForm(form);
        });
    }
    const txHeight = 16;
    const tx = document.getElementsByTagName("textarea");
    
    for (let i = 0; i < tx.length; i++) {
      if (tx[i].value == '') {
        tx[i].setAttribute("style", "height:" + txHeight + "px;overflow-y:hidden;");
      } else {
        tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
      }
      tx[i].addEventListener("input", OnInput, false);
    }
    
    function OnInput(e) {
      this.style.height = "auto";
      this.style.height = (this.scrollHeight) + "px";
    }
});
