			var myFuncCalls=0;
			function selector(caller){
				var form = document.getElementById('Auflistung');
				var submit = document.createElement('input');
				var table = document.getElementById('Sign_table');
				var vorhanden=document.getElementById(caller.innerHTML);
				if (myFuncCalls<=0){
					submit.setAttribute('id', 'submit_btn');
					submit.setAttribute('class', 'Upload');
					submit.setAttribute('style', 'margin-top: 15px;');
					submit.setAttribute('value', 'Submit');
					submit.setAttribute('type', 'Submit');
					var row = table.insertRow(-1);
					var cell1 = row.insertCell(0);
					var cell2 = row.insertCell(1);
					cell1.innerHTML = caller.innerHTML + ': ';
					cell2.innerHTML = '<select name="cars">\
					<option value="1">1ms</option><option value="10">10ms</option><option value="100">100ms</option></select>\
					<a href=\'#\' onclick=\'deleteRow(this)\'> \
					<img src="Picture/delete.png" alt="Delete signal" style="width:34px;height:34px;border:0;vertical-align:middle;">\
					</a>';
					cell2.setAttribute('id',caller.innerHTML);
					table.style.visibility="visible";
					form.appendChild(submit);}
				else if (!vorhanden) {
					row = table.insertRow(-1);
					var cell1 = row.insertCell(0);
					var cell2 = row.insertCell(1);
					cell1.innerHTML = caller.innerHTML + ': ';
					cell2.innerHTML = '<select name="cars">\
					<option value="1">1ms</option><option value="10">10ms</option><option value="100">100ms</option></select>\
					<a href=\'#\' onclick=\'deleteRow(this)\'> \
					<img src="Picture/delete.png" alt="Delete signal" style="width:34px;height:34px;border:0;vertical-align:middle;">\
					</a>';
					cell2.setAttribute('id',caller.innerHTML);}
				myFuncCalls++;
			}
		function deleteRow(r) {
			var i = r.parentNode.parentNode.rowIndex;
			document.getElementById("Sign_table").deleteRow(i);			
		}
