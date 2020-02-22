/**
 * Created by Asus on 09/02/2020.
 */
window.onload = function() {
    var latlng = new google.maps.LatLng(35.7509,51.4141);
    var map = new google.maps.Map(document.getElementById('map'), {
        center: latlng,
        zoom: 11,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: 'Set lat/lon values for this property',
        draggable: true
    });
    google.maps.event.addListener(marker, 'dragend', function (a) {
        console.log(a);
        var latitudes = document.getElementById('id_coordinate');
        latitudes.value = a.latLng.lat().toFixed(4) + '-' + a.latLng.lng().toFixed(4);
    });
};

jQuery(document).ready(function () {
        var counter = 1;
        jQuery("#addrow").on("click", function () {
            var newRow = jQuery("<tr>");
            var cols = "";
            // cols +='<td><label for="id_parent_residences"></label><select class="form-control" id="id_parent_residences" name="parent_residences"><option>name 1</option> <option>name 2</option><option>name 3</option> </select>'
            cols += '<td><label for="id_title' + counter + '"></label><input type="text" class="form-control" id="id_title' + counter + '" name="title' + counter + '" /></td>';
            cols += '<td><textarea cols="30" rows="3" id="id_description' + counter + '" name="description' + counter + '" class="form-control" /></td>';
            cols += '<td><label for="id_price' + counter + '"></label><input class="form-control" type="text" id="id_price' + counter + '" name="price' + counter + '"></td>';
            cols += '<td><label for="id_requestable' + counter + '" class="c-switch c-switch-label c-switch-pill c-switch-primary"><input class="c-switch-input" id="id_requestable' + counter + '" name="requestable' + counter + '" type="checkbox" checked=""><span class="c-switch-slider" data-checked="✓" data-unchecked="✕"></span></label></td>';
            // cols += '<input type="hidden" name="counter" id="counter" value="'+ counter +'" />';
            cols += '<td><button class="ibtnDel btn btn-danger cil-trash"></button></td>';
            newRow.append(cols);
            jQuery("table.dataTable").append(newRow);
            counter++;

        });
        jQuery("table.dataTable").on("click", ".ibtnDel", function (event) {
            jQuery(this).closest("tr").remove();
            counter -= 1
        });


    });
