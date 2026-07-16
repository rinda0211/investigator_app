const dropArea = document.getElementById("drop-area");

dropArea.addEventListener("dragover", function(e) {
    e.preventDefault();
    dropArea.classList.add("dragover");
});

dropArea.addEventListener("dragleave", function() {
    dropArea.classList.remove("dragover");
});

dropArea.addEventListener("drop", function(e) {

    e.preventDefault();
    dropArea.classList.remove("dragover");

    const file = e.dataTransfer.files[0];

    if (!file.name.endsWith(".json")) {
        alert("JSONファイルを選択してください。");
        return;
    }

    const formData = new FormData();
    formData.append("json_file", file);

    fetch("/load_session", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
    });
});