const backInTable = document.getElementById("backInTable");
backInTable.addEventListener("click", () => {
  let ct = document.getElementsByClassName("timetable-container")[0];
  let TimeTable = document.getElementById("timetable");

  try {
    ct.scrollLeft = TimeTable.rows[timeOffset + 1].cells[dateOffset + 1].offsetLeft - TimeTable.rows[1].cells[1].offsetLeft;
    ct.scrollTop = TimeTable.rows[timeOffset + 1].cells[dateOffset + 1].offsetTop - TimeTable.rows[1].cells[1].offsetTop;
  } catch(err) {
  }
});
