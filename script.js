function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const status = document.getElementById("status");
    const tableBody = document.querySelector("#resultTable tbody");

    if (!fileInput.files.length) {
        alert("Please select a file first!");
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    status.innerText = "Uploading... Running Spark Word Count...";

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) throw new Error("Server error " + response.status);
        return response.json();
    })
    .then(data => {
        if (data.error) {
            status.innerText = data.error;
            return;
        }

        status.innerText = "File processed successfully!";
        tableBody.innerHTML = "";

        const sortedWords = Object.entries(data.wordcount)
            .sort((a, b) => b[1] - a[1]);

        sortedWords.forEach(([word, count]) => {
            const row = document.createElement("tr");
            row.innerHTML = `<td>${word}</td><td>${count}</td>`;
            tableBody.appendChild(row);
        });
    })
    .catch(err => {
        status.innerText = "Error processing file!";
        console.error(err);
    });
}
