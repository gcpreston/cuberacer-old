var initial = new Date();

function startTime() {
    var timer = setInterval(updateTime, 1);
}

function updateTime() {
    document.getElementById("time").innerHTML = new Date() - initial;
}

function stopTime() {
    window.clearInterval(timer);
}