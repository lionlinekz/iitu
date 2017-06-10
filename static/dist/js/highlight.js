function getSelectedText() {
  t = (document.all) ? document.selection.createRange().text : document.getSelection();

  return t;
}

$('.qazword').mouseup(function(){
    var selection = getSelectedText();
    var selection_text = selection.toString();
    
    // How do I add a span around the selected text?
    
    var span = document.createElement('em');
    span.textContent = selection_text;
    
    var range = selection.getRangeAt(0);
    range.deleteContents();
    range.insertNode(span);
});