//*************************************************
//Add one row to the signal-specification-list
//*************************************************
var myFuncCalls=0;
function selector(caller){
	var form = document.getElementById('Auflistung');
	var submit = document.createElement('input');
	var table = document.getElementById('Sign_table');
	var vorhanden=document.getElementById(caller.innerHTML);
	if (!vorhanden){
		if (myFuncCalls<=0){
			submit.setAttribute('id', 'submit_btn');
			submit.setAttribute('class', 'Upload');
			submit.setAttribute('style', 'margin-top: 15px;');
			submit.setAttribute('value', 'Submit');
			submit.setAttribute('type', 'Submit');
			form.appendChild(submit);}
		table.style.visibility="visible";
		row = table.insertRow(-1);
		var cell1 = row.insertCell(0);
		var cell2 = row.insertCell(1);
		var cell3 = row.insertCell(2);
		var cell4 = row.insertCell(3);
		var cell5 = row.insertCell(4);
		cell1.innerHTML = caller.innerHTML + ': ';
		cell2.innerHTML = '<select name="samplerates" class="sampleselection">\
		<option value="1">1ms</option><option value="10">10ms</option><option value="100">100ms</option></select>';
		cell2.setAttribute('id',caller.innerHTML);
		cell3.setAttribute('id','test');
		cell3.innerHTML = ' <input type="radio" name="condition" value='+caller.innerHTML+'>';
		cell4.style.visibility='hidden';
		cell4.innerHTML = '<input type="text" name="start" class= "startcon">';
		cell5.innerHTML = '<a href=\'#\' onclick=\'deleteRow(this)\'> \
		<img src="Picture/delete.png" alt="Delete signal" style="width:34px;height:34px;border:0;vertical-align:middle;"></a>';}
	myFuncCalls++;
}
//*************************************************
//Delete a row of the signal specification-list
//*************************************************
function deleteRow(r) {
var i = r.parentNode.parentNode.rowIndex;
document.getElementById("Sign_table").deleteRow(i);		
}

//*************************************************
//jQuery-function to set the Start/Stop Input Field
//*************************************************
$(document).ready(function () {
$('#Auflistung').on('change','input:radio', function() {
$('table tbody tr').each(function() {
		$(this).find("td").eq(3).css('visibility', 'hidden');
		$(this).find("td").eq(3).find("input").val('');})
	if ($('input[name=condition]:checked', '#Auflistung')){
		$(this).closest("td").next().css('visibility', 'visible');}

   })
});

function saver(){
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//Wichtig für Speichern der Webpage
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
var Samplerates="";
var StartVal= "";
$(".startcon").each(function() {
    StartVal=StartVal.concat($(this).val());
	StartVal=StartVal.concat(',');	
});
StartVal = StartVal.substring(0, StartVal.length - 1);
$(".sampleselection").each(function() {
    Samplerates=Samplerates.concat($(this).val());
	Samplerates=Samplerates.concat(',');
});
Samplerates = Samplerates.substring(0, Samplerates.length - 1);
var html_site = ($( 'body' ).html().toString());
//<head muss manuell hinzugefügt werden>
$("#webpage").val(html_site);
$("#SampleRates").val(Samplerates);
$("#StartVal").val(StartVal);
}



	

		
		

