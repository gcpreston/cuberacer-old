var initial;
var timer;
var countdownTimer;
var status = 0; // 0 = stopped, 1 = inspecting, 2 = running, 3 = buffer

var countdownSecs;

function startCountdown() {
    document.getElementById("time").style.color = "red";
    document.getElementById("time").innerHTML = 15;
    countdownSecs = 14;
    countdownTimer = setInterval(updateCountdown, 1000);
}

function updateCountdown() {
    if (countdownSecs >= 1) {
        document.getElementById("time").innerHTML = countdownSecs;
    } else if (countdownSecs == 0 || countdownSecs == -1) {
        document.getElementById("time").innerHTML = "+2";
    } else {
        document.getElementById("time").innerHTML = "DNF";
        status = 0;
    }
    countdownSecs--;
}

function startTime() {
    window.clearInterval(countdownTimer);
    document.getElementById("time").style.color = "black";
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
    if (e.which == 32) {
        if (status == 0) {
            status = 1;
            startCountdown();
        } else if (status == 1) {
            status = 2;
            startTime();
        } else if (status == 3) {
            status = 0;
        }
    }
});

$(document).on('keydown', function(e) {
    if (e.which == 32 && status == 2) {
        stopTime();
        status = 3;
    }
});
