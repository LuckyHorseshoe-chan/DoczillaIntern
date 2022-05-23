function ShowToday(){
	let today = String(getDate()) + '-' + String(getMonth()) + '-' + String(getYear());
	var todo_dates = document.getElementsByClassName('date');
	for (let i = 0; i < todo_dates.length; i++){
		if(todo_dates[i].textContent != today){
			todo_dates[i].parentElement.style.display = 'none';
		} else{
			todo_dates[i].parentElement.style.display = 'block';
		};
	};
};
document.getElementById('today_but').onclick = () => {
	ShowToday();
	};