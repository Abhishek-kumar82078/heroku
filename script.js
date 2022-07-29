$('.btn').click(function(event){
    event.preventDefault();

    var form = $('#fileUploadForm')[0];
        console.log("Entered js")
        var data = new FormData(form);
        console.log(data)
        var ajxreq=$.ajax({ 
            type: "POST",
            enctype: 'multipart/form-data',
            url: "https://fastapi-deploymen.herokuapp.com/message",
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
            console.log(e)
            return false;
    })
});
