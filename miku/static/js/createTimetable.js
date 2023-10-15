const now = new Date();
setDbgMsg("Database Time: " + now);
setDbgMsg("Local Time: " + now.getStr());

const currentHour = now.getHours();
const currentMinutes = now.getMinutes();

const timeOffset = Math.trunc(currentHour * 2 + currentMinutes / 30);

const currentYear = now.getFullYear();
const currentMonth = now.getMonth() + 1;
const currentDay = now.getDate();

const timetable = document.getElementById('timetable');

let dateOffset = 0;


function generateDatesForOneMonth() {
    const todaysDate = new Date();
    const startDate = new Date();
    const endDate = new Date(startDate);
    endDate.setMonth(endDate.getMonth() + 1); // Calculate the date one month from now
    startDate.setMonth(startDate.getMonth() - 1);
    dateOffset = (now - startDate) / 86400000;
    console.log("todaysDate: "+ todaysDate + " dateoffset:" + (todaysDate - startDate) / 86400000);
    console.log("now: "+ now + " dateoffset:" + (now - startDate) / 86400000);
    dateOffset = Math.round(dateOffset);
    //console.log(dateOffset);

    const dates = [];
    let currentDate = new Date(startDate);

    while (currentDate <= endDate) {
        const year = currentDate.getFullYear();
        const month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // Display month with 2 digits
        const day = currentDate.getDate().toString().padStart(2, '0'); // Display day with 2 digits
        const formattedDate = `${year}-${month}-${day}`;
        dates.push(formattedDate);

        currentDate.setDate(currentDate.getDate() + 1); // Move to the next day
    }

    return dates;
}

// Generate dates for one month starting from today
const dates = generateDatesForOneMonth();


function generateTimesFor24Hours() {
    const times = [];
    for (let hour = 0; hour < 24; hour++) {
        for (let minute = 0; minute < 60; minute += 30) {
            const formattedHour = hour.toString().padStart(2, '0'); // Display hour with 2 digits
            const formattedMinute = minute.toString().padStart(2, '0'); // Display minute with 2 digits
            const formattedTime = `${formattedHour}:${formattedMinute}`;
            times.push(formattedTime);
        }
    }
    return times;
}

// Generate 24 hours of time in 30-minute intervals
const times = generateTimesFor24Hours();

const dateRow = document.createElement('tr');
dateRow.classList.add('table-light');
dateRow.innerHTML = '<th></th>';
for (const date of dates) {
    const th = document.createElement('th');
    th.textContent = date;
    th.setAttribute('id', date);
    th.setAttribute('data-date', date);
    dateRow.appendChild(th);
}

const dateHead = document.createElement('thead');
dateHead.appendChild(dateRow);
timetable.appendChild(dateHead);

const dateBody = document.createElement('tbody');
timetable.appendChild(dateBody);

for (const time of times) {
    const tr = document.createElement('tr');
    const timeCell = document.createElement('th');
    timeCell.textContent = time;
    timeCell.setAttribute('id', time);
    timeCell.setAttribute('data-time', time);
    tr.appendChild(timeCell);
    for (const date of dates) {
        const td = document.createElement('td');
        td.setAttribute('id', date+"-"+time);
        td.setAttribute('data-date', date);
        td.setAttribute('data-time', time);
        td.textContent = date.substring(5) + " " + time;
        tr.appendChild(td);
    }
    dateBody.appendChild(tr);
}




const currentDate = `${currentYear}-${currentMonth.toString().padStart(2, '0')}-${currentDay.toString().padStart(2, '0')}`;
console.log(currentDate);
console.log(currentMinutes);
let currentTime;
if (currentMinutes < 30) {
  currentTime = `${currentHour.toString().padStart(2, '0')}:00`;
  console.log(currentTime);
} else {
  currentTime = `${currentHour.toString().padStart(2, '0')}:30`;
  console.log(currentTime);
}

const currentTimeCell = document.querySelector(`td[data-time="${currentHour}:${currentMinutes.toString().padStart(2, '0')}"]`);
if (currentTimeCell) {
    currentTimeCell.classList.add('current-time');
}

const dateHeaderCells = document.querySelectorAll('th[data-date], td[data-date]');
dateHeaderCells.forEach((cell) => {
    if (cell.dataset.date === currentDate) {
        cell.classList.add('today-column');
    }
});

const timeHeaderCells = document.querySelectorAll('th[data-time], td[data-time], th[data-date], td[data-date]');
timeHeaderCells.forEach((cell) => {
    if (cell.dataset.time === currentTime) {
        cell.classList.add('today-row');
        if (cell.dataset.date === currentDate) {
            cell.classList.add('today-column');
            cell.classList.add('current-time');
        }
    }
    else if (cell.dataset.date === currentDate) {
        cell.classList.add('today-column');
    }
});

const TimeTable1 = document.getElementById("timetable");
const ct1 = document.getElementsByClassName("timetable-container")[0];


