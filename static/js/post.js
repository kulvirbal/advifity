$(document).ready(function(){
    editor = CKEDITOR.replace( 'description' );
    editor.on( 'change', function( evt ) {
        $('#description').val(evt.editor.getData());
    });
    /*
    * Initialize form validation on the add post form
    */
    $("#post-form").validate({
        // Specify validation rules
        rules: {
            title: {
                required: true,
                minlength: 3,
                maxlength: 120,
                accept: "[a-zA-Z0-9]+"
            },
            organization: {
                required: true,
                minlength: 3,
                maxlength: 100,
                accept: "[a-zA-Z0-9]+"
            },
            hourly_rate: {
                required: true,
                maxlength: 20
            },
            address: {
                required: true
            },
            description:{
                required: true
            },
            job_type:{
                required: true
            }
        },
        messages: {
            
        },
        submitHandler: function(form) {
            
            $("#post-form").submit();
        }
    });
});
function deletePost(id) {
    if (confirm("Are you sure you want to delete this post?")) {
        $.ajax({
            url: "/deletepost/",
            data:{'id':id},
            success: function(result){
                location.reload();
            }
        });
    }
    return false;
}