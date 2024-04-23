function makeHttpObject() {
    try {
        return new XMLHttpRequest();
    } catch (error) {
    }
    try {
        return new ActiveXObject("Msxml2.XMLHTTP");
    } catch (error) {
    }
    try {
        return new ActiveXObject("Microsoft.XMLHTTP");
    } catch (error) {
    }

    throw new Error("Could not create HTTP request object.");
}
const button = document.getElementById("submit"); //submit button element in html
button.addEventListener("click", e => { // click event listener
    const code = document.getElementById("code").value; // Get input value
    const url = "http://127.0.0.1:5000/search?code=" + code; // maek URL
    let request = makeHttpObject(); // Create XMLHttpRequest
    request.open("GET", url, true); // Open async GET request
    request.send(null); // Send request
    request.onreadystatechange = function () { // handle changes
        if (request.readyState == 4) // if success
            var text = request.responseText; // Store response text
        document.getElementById("text").innerHTML = text; // Update HTML content
    };
});