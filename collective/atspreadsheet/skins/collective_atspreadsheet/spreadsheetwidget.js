var JQSHEET_USE_HTML=false;
var JQSHEET_ACTIVATED=false;


var initJQSheet = function(objid,stitle,editable){
  jQuery(document).ready(function() {
    key = objid+"-jspreadsheet"

    if (typeof editable == "undefined"){
       editable=true;
    }

    if (!JQSHEET_ACTIVATED){
      if (editable == true){
        jQuery(key).sheet({
            title:stitle,
            editable:true,
            buildSheet:true,
            inlineMenu: jQuery('#inlineMenu').html(),
            newColumnWidth: '200px',
            });
      } else {
        jQuery(key).sheet({
            title:stitle,
            editable:false,
            buildSheet:true,
            newColumnWidth: '200px',
            });
      };
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

