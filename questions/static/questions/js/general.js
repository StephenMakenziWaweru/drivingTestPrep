$(document).ready(() => {
    $('button#toggleAnswer').click(() => {
        if ($('button#toggleAnswer').html() === '<i class="fa fa-eye-slash" aria-hidden="true"></i> hide all answers') {
            $('button#toggleAnswer').html('<i class="fa fa-eye" aria-hidden="true"></i> show all answers');
            $('small').hide();
        } else {
            $('button#toggleAnswer').html('<i class="fa fa-eye-slash" aria-hidden="true"></i> hide all answers');
            $('small').show();
        }
        
    });
    $('#notes-table').DataTable();
});
