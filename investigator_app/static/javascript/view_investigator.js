function save_investigator(id){
    fetch(`/save_investigator/${id}`)
}

async function copy_investigator(id){
    const ccfoliaText = await fetch(`/copy_investigator/${id}`);
    const text = await ccfoliaText.text();
    navigator.clipboard.writeText(text);
    // alert("コピーしました");
}