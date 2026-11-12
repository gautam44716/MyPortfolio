/* =====================================================
   Stopwatch logic
   Uses Date.now() so the time stays accurate.
   ===================================================== */

const minutesEl = document.getElementById("minutes");
const secondsEl = document.getElementById("seconds");
const millisEl = document.getElementById("millis");

const startBtn = document.getElementById("startBtn");
const lapBtn = document.getElementById("lapBtn");
const resetBtn = document.getElementById("resetBtn");
const lapList = document.getElementById("lapList");

let timerId = null;       // id of the running setInterval
let startTime = 0;        // moment when we last pressed Start
let elapsedBefore = 0;    // time collected before the last pause (ms)
let lapCount = 0;

/* ---------- Helpers ---------- */

// Add a leading zero: 5 -> "05"
function pad(number) {
  return String(number).padStart(2, "0");
}

// Convert milliseconds into "mm:ss.cc" parts
function splitTime(totalMs) {
  return {
    minutes: pad(Math.floor(totalMs / 60000)),
    seconds: pad(Math.floor((totalMs % 60000) / 1000)),
    millis: pad(Math.floor((totalMs % 1000) / 10))
  };
}

// Total time passed right now
function currentTime() {
  return elapsedBefore + (Date.now() - startTime);
}

// Show time on the screen
function render(totalMs) {
  const time = splitTime(totalMs);
  minutesEl.textContent = time.minutes;
  secondsEl.textContent = time.seconds;
  millisEl.textContent = time.millis;
}

/* ---------- Button actions ---------- */

function startStopwatch() {
  startTime = Date.now();
  timerId = setInterval(function () {
    render(currentTime());
  }, 10);

  startBtn.textContent = "Pause";
  startBtn.classList.add("running");
  lapBtn.disabled = false;
}

function pauseStopwatch() {
  clearInterval(timerId);
  timerId = null;
  elapsedBefore = currentTime();

  startBtn.textContent = "Resume";
  startBtn.classList.remove("running");
  lapBtn.disabled = true;
}

function resetStopwatch() {
  clearInterval(timerId);
  timerId = null;
  elapsedBefore = 0;
  lapCount = 0;

  render(0);
  lapList.innerHTML = "";
  startBtn.textContent = "Start";
  startBtn.classList.remove("running");
  lapBtn.disabled = true;
}

function addLap() {
  lapCount++;
  const time = splitTime(currentTime());

  const item = document.createElement("li");
  item.innerHTML =
    "<span>Lap " + lapCount + "</span>" +
    "<span>" + time.minutes + ":" + time.seconds + "." + time.millis + "</span>";

  // Newest lap on top
  lapList.prepend(item);
}

/* ---------- Events ---------- */

startBtn.addEventListener("click", function () {
  if (timerId === null) {
    startStopwatch();
  } else {
    pauseStopwatch();
  }
});

lapBtn.addEventListener("click", addLap);
resetBtn.addEventListener("click", resetStopwatch);

/* Keyboard: Space = start/pause, L = lap, R = reset */
document.addEventListener("keydown", function (event) {
  if (event.code === "Space") {
    event.preventDefault();
    startBtn.click();
  } else if (event.key.toLowerCase() === "l" && !lapBtn.disabled) {
    addLap();
  } else if (event.key.toLowerCase() === "r") {
    resetStopwatch();
  }
});
