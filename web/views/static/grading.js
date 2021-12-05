function editGrade(id) {
    $('input[name=gradeDate]').val( $(`#g-${id}-date`).text() );
    $('select[name=gradePupil]').val( $(`#g-${id}-pupilid`).text() );
    $('select[name=gradePupil]').prop("disabled", true);
    $('select[name=gradeSubject]').val( $(`#g-${id}-subject`).text() );
    $('select[name=gradeGrade]').val( $(`#g-${id}-grade`).text() );
    $('select[name=gradeWeight]').val( $(`#g-${id}-w`).text() );
    $('input[name=gradeDescription]').val( $(`#g-${id}-desc`).text() );
    $('input[name=gradeId]').attr("value", id);
    $('#delete').removeAttr("hidden");
    $('#modalForm').prop("action", "grading/update");
}
