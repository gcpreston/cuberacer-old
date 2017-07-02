var initial;
var timer;
var running = false;
var buffer = false;

function startTime() {
    document.getElementById("time").innerHTML = 0;
    running = true;
    initial = new Date();
    timer = setInterval(updateTime, 1);
}

function updateTime() {
    document.getElementById("time").innerHTML = (new Date() - initial) / 1000;
}

function stopTime() {
    window.clearInterval(timer);
    running = false;
}

$(document).on('keyup', function(e) {
    if (e.which == 32 && !running && !buffer)
        startTime();
    else
        buffer = false;
});

$(document).on('keydown', function(e) {
    if (e.which == 32 && running) {
        stopTime();
        buffer = true;
    }
});