jQuery(document).ready(function($)
{
	var dados = {
		temperatura: 0,
		umidade: 0,
		luminosidade: 0
	}

	var id = $("#id_usuario").val();
	atualizarDados(id);
	setInterval(function(){
		atualizarDados(id);
	}, 60000);

	function atualizarDados (id) {
		$.ajax({
			url: "../php/get_last_measurement.php",
			type: "post",
			data: {id : id},
			dataType: "json",
			success: function (data) {
				dados.temperatura = data.temperatura;
				dados.umidade = data.umidade;
				dados.luminosidade = data.luminosidade;

				var opts_temp = {
					lineWidth: 0.23,
					radiusScale: 0.58,
					pointer: {
						length: 0.6,
						strokeWidth: 0.035, 
						color: '#000000'
					},
					percentColors: [[0.2, "#00ff00"], [0.70, "#ffff00"], [1.0, "#ff0000"]],
					strokeColor: '#E0E0E0',
					generateGradient: true,
					highDpiSupport: true,	  
				};
				g_temperatura = new Gauge(document.getElementById("temp"));
				g_temperatura.minValue = -10;
				g_temperatura.maxValue = 50;
				g_temperatura.animationSpeed = 30;
				g_temperatura.set(data.temperatura);
				g_temperatura.setTextField(document.getElementById("lbl_temp"));
				g_temperatura.setOptions(opts_temp);

				var opts_umid = {
					lineWidth: 0.23,
					radiusScale: 0.58,
					pointer: {
						length: 0.6,
						strokeWidth: 0.035,
						color: '#000000'
					},
					percentColors: [[0.0, "#00ff00"], [0.50, "#ffff00"], [1.0, "#ff0000"]],
					strokeColor: '#E0E0E0',
					generateGradient: true,
					highDpiSupport: true,
				};
				g_umidade = new Gauge(document.getElementById("umid"));
				g_umidade.minValue = 0;
				g_umidade.maxValue = 100;
				g_umidade.animationSpeed = 30;

				var opts_lumi = {
					lineWidth: 0.23,
					radiusScale: 0.58,
					pointer: {
						length: 0.6,
						strokeWidth: 0.035,
						color: '#000000'
					},
					percentColors: [[0.0, "#ffff00"], [0.50, "#ffff00"], [1.0, "#ffff00"]],
					strokeColor: '#E0E0E0',
					generateGradient: true,
					highDpiSupport: true,
					  
				};
				g_luminosidade = new Gauge(document.getElementById("lumi"));
				g_luminosidade.minValue = 0;
				g_luminosidade.maxValue = 1500
				g_luminosidade.animationSpeed = 30;
				g_luminosidade.set(data.luminosidade);
				g_luminosidade.setTextField(document.getElementById("lbl_lumi"));
				g_luminosidade.setOptions(opts_lumi);

				g_umidade.set(data.umidade);
				g_umidade.setTextField(document.getElementById("lbl_umid"));
				g_umidade.setOptions(opts_umid);

				avaliarSituacao(dados);
			}
		});
	}

	function avaliarSituacao (dados) {
		if (dados.temperatura >= 35) {
			$(".situacao h4").text("A temperatura está ficando muito alta!");
			$(".situacao h4").css({"color" : "#f00"});
		} else if (dados.umidade >= 55) {
			$(".situacao h4").text("A umidade está ficando muito alta!");
			$(".situacao h4").css({"color" : "#f00"});
		} else {
			$(".situacao h4").text("O ambiente está estável!");
			$(".situacao h4").css({"color" : "#0c0"});
		}
	}
});
