jQuery(document).ready(function($){

  // LOGIN

  $("#formlogin").submit(function(e){
    e.preventDefault();
    
    var email = $("#email").val();
    var senha = $("#senha").val();
    
    if (email == ""){
      $("#msglogin").show();
      $("#msglogin").text("Insira seu e-mail!");
    } else if (senha == ""){
      $("#msglogin").show();
      $("#msglogin").text("Insira sua senha!");
    } else {
      $.ajax({
        url: "../php/validar_login.php",
        type: "post",
        data: {email : email, senha : senha},
        success: function (result)
        {
          if(result=="sucesso"){
            location.href = "index.php";
          } else {
            $("#msglogin").show();
            $("#msglogin").text("E-mail ou senha incorretos!");
          }
        }
      });
    }
    return false;
  });
});
