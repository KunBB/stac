$(document).on('ready', function() {

    $(document).on('click', '#datos', function() {

        var test = $('#test').val();
        var alpha = $('#alpha').val();
        var tipo = $('#tipo').val();

		var url;
		if(alpha != "no" & tipo !="no")
			url = "http://localhost:8080/"+test+"/"+alpha+"/"+tipo;
		else if(alpha != "no")
			url = "http://localhost:8080/"+test+"/"+alpha;
		else if(tipo != "no")
			url = "http://localhost:8080/"+test+"/"+tipo;
		else
			url = "http://localhost:8080/"+test

        $.ajax({
            type: "get",
            url: url,
            dataType: "json",
            success : function(data) {
                salida = "<p>Resultado test:</p>";
                $.each(data, function(key, val) {
                    salida = salida + "<p>" + key + " = " + val + "</p>";
                });
                $("#resultado").html(salida);
            },
            error : function(e) {
                alert('Error: ' + e);
            }
        });

    });

	//No funciona correctamente.
	$(document).on('submit', '#subida_fichero', function () {
		
		$.ajax({
		    type: "post",
		   	url: "http://localhost:8080/subir",
		    dataType: "json",
		    success : function(data) {
		        salida = "<p>Lista ficheros:</p>";
		        $.each(data, function(key, val) {
		            salida = salida + "<p>" + key + " = " + val + "</p>";
		        });
		        $("#lista_ficheros").html(salida);
		    },
		    error : function(e) {
		        alert('Error: ' + e);
		    }
    	});
	});

});