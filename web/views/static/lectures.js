$(document).ready(function() {
    $('#lectureClass').on('change', function() {
        $.ajax({
            type: "GET",
            url: "lectures/get-class-pupils",
            data: { class: $(this).val() },
            dataType: "json",
            encode: true,
          }).done(function (data) {
            console.log(data);
            $('#pupilsList').empty();
            $('#lectureBtn').removeClass('disabled');
            data.pups.forEach(pupil => {
                $('#pupilsList').append(`
                <div class="row row-cols-2 d-flex flex-row flex-grow-1 align-items-stretch align-content-stretch align-self-stretch">
                    <div class="col-4 flex-grow-1 align-items-start"><span class="align-middle text-center">${ pupil.name } ${ pupil.surname }</span></div>
                    <div class="col-1 flex-grow-1 align-items-end">
                        <select type="text" class="form-control" id="${pupil.id}-frq" name="${pupil.id}-frq">
                            <option value="1">Present</option>
                            <option value="0">Absent</option>
                            <option value="2">Late</option>
                        </select>
                    </div>
                </div>
                `);
            });
          });
      });
})