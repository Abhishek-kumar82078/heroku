$('.btn').click(function(event){
    event.preventDefault();

    var form = $('#form_id')[0];
        
        var data = new FormData(form);
        // console.log(hello'); 
        var ajxreq=$.ajax({ 
            type: "GET",
            enctype: 'multipart/form-data',
            url: "https://fastapi-deploymen.herokuapp.com/messsage",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
        });

        ajxreq.success( function (data) {
            console.log("Done");
            dat=data
            document.getElementById("para").innerHTML=dat
            return true;
    });
    ajxreq.error( function (e) {
            console.log("Error")
            return false;
    })
});
