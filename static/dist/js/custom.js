 $('.editor').wysiwyg();
 $('.editor').cleanHtml()
function loadVal(id){
	des = $("#ruseditor"+id).html();
	$("#rus"+id).val(des);
	desc = $("#editor"+id).html();
	$("#qaz"+id).val(desc);
	}
