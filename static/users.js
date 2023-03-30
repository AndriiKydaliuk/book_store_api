function add_record_to_table(data) {
    $('#users_table tr:last').after(
        '<tr>'+
        '<td class="id_cell">'+data['id']+'</td>'+
        '<td class="user_name_cell">'+data['first_name']+'</td>'+
        '<td class="login_cell">'+data['last_name']+'</td>'+
        '<td class="email_cell">'+data['login']+'</td>'+
        '<td class="address_cell">'+data['login']+'</td>'+
        '</tr>');
    $('#add_user').modal('hide');
};

function update_record_in_table(data) {
    $('#users_table td.id_cell:contains('+data['id']+')').parent().replaceWith(
        '<tr>'+
        '<td class="id_cell">'+data['id']+'</td>'+
        '<td class="user_name_cell">'+data['first_name']+'</td>'+
        '<td class="login_cell">'+data['last_name']+'</td>'+
        '<td class="email_cell">'+data['login']+'</td>'+
        '<td class="address_cell">'+data['login']+'</td>'+
        '</tr>');
    $('#edit_user').modal('hide');
};

function delete_record_from_table(id) {
    $('#users_table td.id_cell:contains('+id+')').parent().remove();
    $('#delete_user').modal('hide');
};

$(document).ready(function(){

    $('#users_table tbody tr').on("click", function() {
        $(this).addClass('bg-primary').siblings().removeClass('bg-primary');
    });

    $("#add_user_form").on("submit", function (e) {
        e.preventDefault();
        var data = {};
        data['name'] = $(this).find('#add_name').val()
        data['role'] = $(this).find('#add_role').val()
        data['email'] = $(this).find('#add_email').val()
        data['phone'] = $(this).find('#add_phone').val()
        data['address'] = $(this).find('#add_address').val()
        data['login'] = $(this).find('#add_login').val()
        data['password'] = $(this).find('#add_password').val()
        $.ajax('/api/user', {
            data: JSON.stringify(data),
            contentType: 'application/json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', `Bearer ${window.localStorage.getItem('AuthToken')}`);
            },
            type: 'POST',
            success: function(data) {
                add_record_to_table(data);
                $('#add_user').modal('hide');
            },
            error: function(request, status, error) {
                alert(request.responseText);
            }
        });
    });

    $("#edit_user").on("shown.bs.modal", function (e) {
        var data = {};
        var name = $('tr.bg-primary td:eq(0)').text();
        var role = $('tr.bg-primary td:eq(1)').text();
        var email = $('tr.bg-primary td:eq(2)').text();
        var phone = $('tr.bg-primary td:eq(3)').text();
        var address = $('tr.bg-primary td:eq(4)').text();
        var login = $('tr.bg-primary td:eq(5)').text();
        var password = $('tr.bg-primary td:eq(6)').text();
        $(this).find('#edit_name').val(name);
        $(this).find('#edit_role').val(role);
        $(this).find('#edit_email').val(email);
        $(this).find('#edit_phone').val(phone);
        $(this).find('#edit_address').val(address);
        $(this).find('#edit_login ').val(login);
        $(this).find('#edit_password').val(password);
    });

    $("#edit_user_form").on("submit", function (e) {
        e.preventDefault();
        var data = {};
        data['name'] = $(this).find('#edit_name').val()
        data['role'] = $(this).find('#edit_role').val()
        data['email'] = $(this).find('#edit_email').val()
        data['phone'] = $(this).find('#edit_phone').val()
        data['address'] = $(this).find('#edit_address').val()
        data['login'] = $(this).find('#edit_login').val()
        data['password'] = $(this).find('#edit_password').val()
        $.ajax('/api/user/'+data['id'], {
            data: JSON.stringify(data),
            contentType: 'application/json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', `Bearer ${window.localStorage.getItem('AuthToken')}`);
            },
            type: 'PUT',
            success: function(data) {
                update_record_in_table(data);
                $('#edit_user').modal('hide');
            }
        });
    });

    $("#delete_user_form").on("submit", function (e) {
        e.preventDefault();
        var id = $(this).find('#delete_id').val()
        $.ajax('/api/user/'+id, {
            contentType: 'application/json',
            type: 'DELETE',
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', `Bearer ${window.localStorage.getItem('AuthToken')}`);
            },
            success: function(data) {
                delete_record_from_table(id);
                $('#delete_user').modal('hide');
            }
        });
    });

    $("#delete_user").on("shown.bs.modal", function (e) {
        var id = $('tr.bg-primary td:eq(0)').text();
        $(this).find('#delete_id').val(id);
    });
});
