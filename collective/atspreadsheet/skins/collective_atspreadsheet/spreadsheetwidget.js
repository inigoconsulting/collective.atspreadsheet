var JQSHEET_USE_HTML=false;
var JQSHEET_ACTIVATED=false;


var initJQSheet = function(objid,stitle,editable){
  jQuery(document).ready(function() {
    key = objid+"-jspreadsheet"
    if (!JQSHEET_ACTIVATED){
       jQuery(key).sheet({
            title:stitle,
            editable:editable,
            buildSheet:true,
            });
       JQSHEET_ACTIVATED=true;
    }
  });
  jQuery(document).submit(function() {
     if (!JQSHEET_USE_HTML) {
        jQuery(objid).val(jS.exportSheet.html().html());
     }
  });
}

var initToggleBtn = function(objid){
  jQuery(document).ready(function() {
     jQuery(objid).hide('fast');
     key = objid+'-toggle';
     jQuery(key).toggle(function() {
          jQuery(objid).show();
     },
     function() {
          jQuery(objid).hide();
     })
  })
}

