$.ajax({
  url: "https://s3.amazonaws.com/lambda-site-alura/dados.json",
  dataType: "json",
  crossDomain: true,
  success: function (dados) {
    console.log(dados);
    montaTabela(dados);
  },
});

function montaTabela(dados) {
  var img = document.querySelector("#imgAnalise");
  img.src = "https://lambda-imagens-alura.s3.amazonaws.com/_analise.jpg";

  for (var dados of dados) {
    var trTabela = document.createElement("tr");

    var tdInfoFoto = document.createElement("td");
    var tdInfoNome = document.createElement("td");
    var tdInfoFaceMatch = document.createElement("td");

    tdInfoNome.textContent = dados.nome;
    tdInfoFaceMatch.textContent = dados.faceMatch;
    tdInfoFoto = document.createElement("img");
    tdInfoFoto.height = 100;
    tdInfoFoto.width = 68;
    tdInfoFoto.src =
      "https://lambda-imagens-alura.s3.amazonaws.com/" + dados.nome + ".jpg";

    trTabela.appendChild(tdInfoFoto);
    trTabela.appendChild(tdInfoNome);
    trTabela.appendChild(tdInfoFaceMatch);

    var tabela = document.querySelector("#tabela-site");

    tabela.appendChild(trTabela);
  }
}
