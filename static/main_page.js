// $('#delete_btn').on('click', function(){
//     let confirmation = confirm("Are you sure you want to remove the post?");
//     if (confirmation) {
//         let object_id = $(this).attr('data-object-id');
//         let url = `delete/${object_id}/`;
//         $.ajax({
//             url: "example.html/my/example",
//             data: {'csrfmiddlewaretoken': "{{ csrf_token }}"},
//             type: "DELETE",
//             dataType: "json"
//         }).done(
//             function(){alert("Deleted");}
//             ).fail(function(){alert("Error");})
//        });
//     }
// })