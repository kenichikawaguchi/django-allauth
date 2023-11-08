
Date.prototype.getStr=function(){
  return this.getFullYear()
            + '/' + ('0' + (this.getMonth() + 1)).slice(-2)
            + '/' + ('0' + this.getDate()).slice(-2)
            + ' ' + ('0' + this.getHours()).slice(-2)
            + ':' + ('0' + this.getMinutes()).slice(-2)
            + ':' + ('0' + this.getSeconds()).slice(-2);
};

Date.prototype.getId=function(){
  if (this.getMinutes() < 30){
    tmp_minutes = 0;
  } else {
    tmp_minutes = 30;
  }
  return this.getFullYear()
            + '-' + ('0' + (this.getMonth() + 1)).slice(-2)
            + '-' + ('0' + this.getDate()).slice(-2)
            + '-' + ('0' + this.getHours()).slice(-2)
            + ':' + ('0' + tmp_minutes).slice(-2);
};

Date.prototype.getTimeOffset=function(){
  if (this.getMinutes() < 30){
    tmp_minutes = 0;
  } else {
    tmp_minutes = 30;
  }
  return Math.trunc(this.getHours()*2 + this.getMinutes() / 30) + 1;
};


const shortDayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
const DayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


Date.prototype.getShortDayName=function(){
  dayNumber = this.getDay();
  return shortDayNames[dayNumber];
}


Date.prototype.getDayName=function(){
  dayNumber = this.getDay();
  return DayNames[dayNumber];
}


function setDbgMsg(message=message, position="debug1"){
  const element = document.getElementById(position);
  tmp_li = document.createElement('li');
  tmp_li.innerText = message;
  element.appendChild(tmp_li);
}

window.onload = function(){

  let ct = document.getElementsByClassName("timetable-container")[0];
  let TimeTable = document.getElementById("timetable");

  if (typeof ct === 'undefined' || typeof TimeTable === 'undefined') {
    return;
  }

  try {
    ct.scrollLeft = TimeTable.rows[timeOffset + 1].cells[dateOffset + 1].offsetLeft - TimeTable.rows[1].cells[1].offsetLeft;
    ct.scrollTop = TimeTable.rows[timeOffset + 1].cells[dateOffset + 1].offsetTop - TimeTable.rows[1].cells[1].offsetTop;
  } catch(err) {
    console.log(err + currentHour);
  }
}

function scrollTable(e){
  ct1.scrollLeft = TimeTable1.rows[this.scrollDown].cells[this.scrollLeft].offsetLeft - TimeTable1.rows[1].cells[1].offsetLeft;
  ct1.scrollTop = TimeTable1.rows[this.scrollDown].cells[this.scrollLeft].offsetTop - TimeTable1.rows[1].cells[1].offsetTop;
};
