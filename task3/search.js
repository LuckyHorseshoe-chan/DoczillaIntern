function Search(){
	let name = document.getElementById('search').value;
	var todo_names = document.getElementsByClassName('todo_name')
	for (let i = 0; i < todo_names.length; i++){
		if(todo_names[i].textContent != name){
			todo_names[i].parentElement.style.display = 'none';
		} else{
			todo_names[i].parentElement.style.display = 'block';
		}
	};
};
document.getElementById('search').onkeydown = (event) => {
	if (event.code === 'Enter') { Search() };
	};