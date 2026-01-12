document.getElementById("generateBtn").addEventListener("click", () => {
    const celebrity = document.getElementById("celebrity").value;

    fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            course: "HTML",
            topic: "Introduction to HTML",
            celebrity: celebrity
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        alert("Lesson generation started. Check backend outputs folder.");
    });
});
