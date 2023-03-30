function setEditModal(e){
    var product = $(e.currentTarget).parent().parent();
    $('#edit_product #edit_name').val(product.find('.name_cell').text());
    $('#edit_product #edit_id').val(product.find('.id_cell').text());
    $('#edit_product #edit_description').val(product.find('.description_cell').text());
    $('#edit_product #edit_author').val(product.find('.author_cell').text());
    $('#edit_product #edit_price').val(product.find('.price_cell').text());
    $('#edit_product #edit_image').val(product.find('.image').text());
};
function setDeleteModal(e){
    var product = $(e.currentTarget).parent().parent();
    $('#delete_product #delete_id').val(product.find('.id_cell').text());
};

$(document).ready(function(){
    $("#add_product_form").on("submit", function (e) {
        e.preventDefault();
        var data = {};
        data['name'] = $(this).find('#add_name').val();
        data['description'] = $(this).find('#add_description').val();
        data['author'] = $(this).find('#add_author').val();
        data['price'] = parseFloat($(this).find('#add_price').val());
        data['image_path'] = $(this).find('#add_image_path').val();
        $.ajax('/api/product', {
            data: JSON.stringify(data),
            contentType: 'application/json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', `Bearer ${window.localStorage.getItem('AuthToken')}`);
            },
            type: 'POST',
            success: function(data) {
                window.location.reload();
                $('#add_product').modal('hide');
            },
            error: function(request, status, error) {
                alert(request.responseText);
            }
        });
    });

    $("#edit_product_form").on("submit", function (e) {
        e.preventDefault();
        var data = {};
        data['name'] = $(this).find('#edit_name').val()
        data['id'] = parseInt($(this).find('#edit_id').val())
        data['description'] = $(this).find('#edit_description').val()
        data['author'] = $(this).find('#edit_author').val()
        data['price'] = parseFloat($(this).find('#edit_price').val())
        data['image_path'] = $(this).find('#edit_image').val()
        $.ajax('/api/product/'+data['id'], {
            data: JSON.stringify(data),
            contentType: 'application/json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', `Bearer ${window.localStorage.getItem('AuthToken')}`);
            },
            type: 'PUT',
            success: function(data) {
                window.location.reload();
                $('#edit_product').modal('hide');
            }
        });
    });

    $("#delete_product_form").on("submit", function (e) {
        e.preventDefault();
        var id = $(this).find('#delete_id').val()
        $.ajax('/api/product/'+id, {
            contentType: 'application/json',
            type: 'DELETE',
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', `Bearer ${window.localStorage.getItem('AuthToken')}`);
            },
            success: function(data) {
                window.location.reload();
                $('#delete_product').modal('hide');
            }
        });
    });
});