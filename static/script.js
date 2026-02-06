setTimeout(() =>{
    let alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert =>{
        alert.style.opacity = "0";
        setTimeout(() => alert.remove(),500);
    });

}, 3000);

document.addEventListener("DOMContentLoaded", ()=>{
    const progressBar =document.querySelector(".progress-bar");
    if (progressBar){
        let value = progressBar.getAttribute("aria-valuenow");
        progressBar.style.width = "0%";
        setTimeout(() =>{
            progressBar.style.width = value + "%";
        },200);
    }
});

function validateWorkspaceForm(){
    const textarea = document.querySelector("textarea[name='answer']");
    if (textarea && textarea.value.trim() === ""){
        alert("please write your answer before submitting!");
        return false;
    }
    return true;
}