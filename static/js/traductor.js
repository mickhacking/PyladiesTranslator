/*
author: Mick Hacking
*/

window.addEventListener('DOMContentLoaded', () => {
    const spanish = document.getElementById("spanish");
    const english = document.getElementById("english");
    spanish.value = "";
    english.value = "";
    spanish.addEventListener("input", (e) => {
        if (e.target.value.leght != 0) {
            fetch("/translator", {
                method: "post",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({"text": e.target.value})
            })
            .then((response, err) => {
                if (response.ok) {
                    return response.json()
                }
                throw err
            })
            .then(data => {
                english.value = data.translate;
            })
        }
    })
});