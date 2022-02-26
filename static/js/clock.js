const clock = document.querySelector("h1#clock");

function getClock() {
    const date = new Date();

    const year = date.getFullYear();
    const month = date.getMonth()+1;
    const today = date.getDate();

    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");
    const seconds = String(date.getSeconds()).padStart(2, "0");
    clock.innerText = `${year} - ${month} - ${today} \n ${hours} : ${minutes} : ${seconds}`;
}

getClock();
setInterval(getClock, 1000);