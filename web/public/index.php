<!DOCTYPE html>
<?php
	session_start();
	require_once("../php/conexao_bd.php");
?>
<html>
	<head>
		<title>Projeto F</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
  		<meta http-equiv="X-UA-Compatible" content="ie=edge">

  		<!--bootstrap-->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

        <!--interno-->
		<link rel="stylesheet" type="text/css" href="style.css">
		<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.0/normalize.min.css">
		<script type="text/javascript" src="moment.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
		<script type="text/javascript" src="settings.js"></script>
		<script src="jquery.js"></script>
	</head>
	<body>
		<nav class="navbar navbar-inverse">
			<ul class="nav navbar-nav navbar-left">
				<div class="navbar-header">
			        <a href="index.php" class="navbar-brand">
			            <h1 class="nome-site">Lens Saver</h1>
			        </a>
	    		</div>
	    	</ul>
    		<?php if (isset($_SESSION["id_usuario"])){ ?>
			<ul class="nav navbar-nav navbar-right">
				<li><a href="../php/logout.php" id="logout">Sair</a></li>
			</ul>
			<?php } ?>
		</nav>	

		<?php if (isset($_SESSION["id_usuario"])){ ?>

		<div class="container-fluid">
			<div class="status card">
				<div class="card-header">
					<h2 class="title-situacao">Situação atual do ambiente</h2>
				</div>
				<div class="card-body situacao">
				    <h4> </h4>
				</div>
			</div>

			<div class="card monitoramento container-fluid">
				<input type="hidden" class="id_usuario" id="id_usuario" value="<?php if (isset($_SESSION["id_usuario"])) {echo $_SESSION["id_usuario"];} ?>">
				<div class="card-header">
					<h2 class="title-medicoes">Últimas medições</h2>
				</div>			
				<div class="cord-body">
					<div class="row medidores">	
						<div class="medidor col-sm-4">
							<canvas id="temp" width="200px" height="200px"></canvas>
							<h3 class="lbl_medidor">Temperatura <br> (℃)</h3>
							<h3 class="g_label" id="lbl_temp"> </h3>
						</div>
						<div class="medidor col-sm-4">
							<canvas id="umid" width="200px" height="200px"></canvas>
							<h3 class="lbl_medidor">Umidade <br> (%)</h3>
							<h3 class="g_label" id="lbl_umid"> </h3>		
						</div>
						<div class="medidor col-sm-4">
							<canvas id="lumi" width="200px" height="200px"></canvas>
							<h3 class="lbl_medidor">Luminosidade <br> (Lux)</h3>
							<h3 class="g_label" id="lbl_lumi"> </h3>
						</div>
					</div>
				</div>	
			</div>

			<div class="graficos panel with-nav-tabs panel-default">
                <div class="panel-heading">
                    <ul class="nav nav-tabs">
                        <li class="active"><a class="temp" href="#grafico-temp" data-toggle="tab">Temperatura</a></li>
                        <li><a class="umid" href="#grafico-umid" data-toggle="tab">Umidade</a></li>
                        <li><a class="lumi" href="#grafico-lumi" data-toggle="tab">Luminosidade</a></li>
                    </ul>
                </div>
                <div class="panel-body">
                    <div class="tab-content">
                    	<div class="grafico tab-pane fade in active" id="grafico-temp">
							<canvas class ="graf-temp"></canvas>
						</div>
						<div class="grafico tab-pane fade" id="grafico-umid">
							<canvas class ="graf-umid"></canvas>
						</div>
                        <div class="grafico tab-pane fade" id="grafico-lumi">
							<canvas class ="graf-lumi"></canvas>
						</div>
                    </div>
                </div>
            </div>
		</div>
		<script type="text/javascript" src="gauge.min.js"></script>
		<script type="text/javascript" src="medidores.js"></script>
		<script type="text/javascript" src="graficos.js"></script>

		<?php } else { ?>

		<div class="card">
			<div class="card-body formulario">
			    <form id="formlogin">	
					<h2 class="titulo"> Login de usuário </h2>	
					<label for="email">E-mail</label>	
					<input type="email" id="email" name="email" maxlength="50">	
					<label for="senha">Senha</label>					
					<input type="password" id="senha" name="senha" maxlength="10">
					<p id="msglogin"> </p>
					<button type="submit" class="btn btn-primary" id="login">Login</button>
				</form>	
			</div>
		</div>
		<?php } ?>
	</body>
</html>

<?php mysqli_close($conexao); ?>
