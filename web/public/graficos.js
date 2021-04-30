jQuery(document).ready(function($){

  var id = $("#id_usuario").val();

  // GERAR GRÁFICOS

  $.ajax({
    url: "../php/get_data.php",
    type: "post",
    data: {id : id},
    dataType: "json",
    success: function (dados)
    {
      console.log(dados);
      var tempo = [];
      var temperatura = [];
      var umidade = [];
      var luminosidade = [];

      for (var i in dados){
        tempo.push(formatarData(new Date(dados[i].hora)));
        temperatura.push(dados[i].temperatura);
        umidade.push(dados[i].umidade);
        luminosidade.push(dados[i].luminosidade);
      }
      
      var graf_temp = new Chart(document.getElementsByClassName("graf-temp"), {
        type: 'line',
        data: {
          labels: tempo.reverse(),
          datasets: [{
            label: "Temperatura (C)",
            data: temperatura,
            borderWidth: 3,
            borderColor: 'rgba(255, 100, 100, 1)',
            backgroundColor: 'rgba(127, 1, 1, 0.3)',
            pointRadius: 3,
            pointHoverRadius: 3
          }]
        },
        options: {
          title: {
            display: true,
            fontSize: 20,
            text: "Temperatura ao decorrer das horas"
          },
          hover: {
              animationDuration: 0,
          },
          responsiveAnimationDuration: 0,
        }
      });

      var graf_umid = new Chart(document.getElementsByClassName("graf-umid"), {
        type: 'line',
        data: {
          labels: tempo.reverse(),
          datasets: [{
            label: "Umidade (%)",
            data: umidade,
            borderWidth: 3,
            borderColor: 'rgba(100, 100, 255, 1)',
            backgroundColor: 'rgba(1, 1, 127, 0.3)'
          }]
        },
        options: {
          title: {
            display: true,
            fontSize: 20,
            text: "Umidade ao decorrer das horas"
          },
        }
      });

      var graf_lumi = new Chart(document.getElementsByClassName("graf-lumi"), {
        type: 'line',
        data: {
          labels: tempo.reverse(),
          datasets: [{
            label: "Luminosidade (lux)",
            data: luminosidade,
            borderWidth: 3,
            borderColor: 'rgba(255, 245, 100, 1)',
            backgroundColor: 'rgba(127, 125, 1, 0.3)'
          }]
        },
        options: {
          title: {
            display: true,
            fontSize: 20,
            text: "Luminosidade ao decorrer das horas"
          },
        }
      });
    }
  });

  function formatarData(data){
    var data_raw = new Date(data);
    var data_formatada = "";

    data_formatada = data_raw.getDate() + "/" + (data_raw.getMonth() + 1) + " - " + (data_raw.getHours() - 2) + "h";
    return data_formatada;
  }
});
