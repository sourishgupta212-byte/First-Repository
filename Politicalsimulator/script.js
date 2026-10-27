    let month = 0
    let year = 1936
    let months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
];

function nextmonth() {
    month = month + 1;
    if (month === 12) {
        month = 0;
        year = year + 1;
    }
    document.getElementById("month").textContent =
        months[month] + " " + year;
}